# KML-AutoAnalyzer

- ilmn_bcl2fastq: 运行 bcl2fastq 命令, 校验 fastq md5sum  

    ```text
    Usage: python -m src.kml_autoanalyzer.ilmn_bcl2fastq [OPTIONS]

    Options:
    --run-id TEXT                 测序批次编号  [required]
    --bcls-dir TEXT               Illumina 测序仪下机数据存放目录  [required]
    --samplesheet TEXT            样本信息表  [required]
    --output-dir TEXT             输出 fastq 目录  [required]
    --interval INTEGER            检查间隔时间，单位为秒  [default: 300]
    --barocode-mismatchs INTEGER  barcode 允许的错配数  [default: 1]
    --threads INTEGER             线程数  [default: 32]
    --help                        显示帮助信息
    ```

  - 例子  
    参数 mismatch 0

    ```bash
    poetry run python -m src.kml_autoanalyzer.ilmn_bcl2fastq --runfolder-dir /data/rawdata/illumina/NEXTseq500/251217_NB501947_0957_AHCLYFAFXC  --samplesheet /data/mengxf/Project/KML251217_HAOBOHBV_AHCLYFAFXC/251217_NB501947_0957_AHCLYFAFXC-samplesheet.csv --output-dir /data/mengxf/Project/KML251217_HAOBOHBV_AHCLYFAFXC/FASTQ --barocode-mismatchs 0
    ```
