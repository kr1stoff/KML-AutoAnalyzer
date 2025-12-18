import click
import logging
import time
import subprocess
from pathlib import Path

from src.kml_autoanalyzer.args import Arguments
from src.kml_autoanalyzer.system import get_default_threads
from src.config.software import BCL2FASTQ

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


@click.command()
# [20251218 芯片号->批次号->完整路径]
@click.option("--runfolder-dir", required=True, help="下机数据 BCL 目录")
@click.option("--samplesheet", required=True, help="样本信息表")
@click.option("--output-dir", required=True, help="输出 FASTQ 目录")
@click.option("--interval", default=300, type=int, show_default=True, help="检查间隔时间，单位为秒")
@click.option("--barocode-mismatchs", default=1, type=int, show_default=True, help=" barcode 允许的错配数")
@click.option("--threads", default=get_default_threads(), type=int, show_default=True, help="线程数")
@click.help_option("--help", help="显示帮助信息")
def main(runfolder_dir, samplesheet, output_dir, interval, barocode_mismatchs, threads):
    logging.info("开启 bcl2fastq bcl 自动拆分")
    logging.info(f"参数:\nBCL 目录: {runfolder_dir}\n样本信息表: {samplesheet}\n输出目录: {output_dir}\n"
                 f"检查间隔: {interval}\nbarcode 允许的错配数: {barocode_mismatchs}\n线程数: {threads}")
    args = Arguments(runfolder_dir, samplesheet, output_dir, interval, barocode_mismatchs, threads)
    ilmn_bcl2fastq(args)
    logging.info("bcl2fastq bcl 自动拆分完成")


def ilmn_bcl2fastq(args: Arguments):
    while True:
        # 检查 bcl 文件是否存在
        if args.runfolder_dir.exists():
            logging.info(f"发现 bcl 文件: {args.runfolder_dir}")
            # 检查是否测序完成
            if args.runfolder_dir.joinpath("CopyComplete.txt").exists():
                logging.info(f"测序完成: {args.runfolder_dir}")
                # bcl2fastq
                with open(args.output_dir / "auto-analyzor.log", "w") as f:
                    cmd = f"""
{BCL2FASTQ} --no-lane-splitting --barcode-mismatches {args.barocode_mismatchs} \
    --processing-threads {args.threads} \
    --runfolder-dir {args.runfolder_dir} \
    --input-dir {args.runfolder_dir}/Data/Intensities/BaseCalls \
    --sample-sheet {args.samplesheet} \
    --output-dir {args.output_dir}
"""
                    logging.debug(f"运行 bcl2fastq 命令: {cmd}")
                    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                    f.write(res.stdout + "\n" + res.stderr + "\n")
                    # 删除 Undetermined fastq
                    # * 后续如果有单端测序, 再改下面代码
                    logging.info("删除 Undetermined fastq")
                    (args.output_dir / "Undetermined_S0_R1_001.fastq.gz").unlink()
                    (args.output_dir / "Undetermined_S0_R2_001.fastq.gz").unlink()
                    # md5sum 校验
                    logging.info("校验 fastq md5sum")
                    cmd = f"cd {args.output_dir} && md5sum *fastq.gz > md5sum.txt"
                    logging.debug(f"运行 md5sum 命令: {cmd}")
                    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                    f.write(res.stdout + "\n" + res.stderr + "\n")
                break
            else:
                logging.info(f"测序中: {args.runfolder_dir}")
        else:
            logging.info(f"未发现 BCL 文件目录: {args.runfolder_dir}")
        time.sleep(args.interval)
        continue


if __name__ == "__main__":
    main()
