# KML-AutoAnalyzer

- ilmn_bcl2fastq: 运行 bcl2fastq 命令, 校验 fastq md5sum

    ```bash
    poetry run python -m src.kml_autoanalyzer.ilmn_bcl2fastq \
      --flow-cell-id HWV3CAFX7 \
      --bcls-dir /data/mengxf/Project/KML251030-AUTO-BCL2FASTQ/test-bcl \
      --samplesheet /data/mengxf/Project/KML251030-AUTO-BCL2FASTQ/samplesheet.csv \
      --output-dir /data/mengxf/Project/KML251030-AUTO-BCL2FASTQ/FASTQ
    ```
