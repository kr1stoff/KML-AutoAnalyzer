# KML-AutoAnalyzer

- ilmn_bcl2fastq: 运行 bcl2fastq 命令, 校验 fastq md5sum  
    *1. 核对 RUN-ID;*  
    *2. 核对 samplesheet*

    ```bash
    poetry run python -m src.kml_autoanalyzer.ilmn_bcl2fastq --run-id 251126_NB501947_0953_AHCLYCAFXC --bcls-dir /data/rawdata/illumina/NEXTseq500 --samplesheet /data/mengxf/Project/KML251126-HAOBOHBV-HCLYCAFXC/251126-HCLYCAFXC-samplesheet.csv --output-dir /data/mengxf/Project/KML251126-HAOBOHBV-HCLYCAFXC/FASTQ
    ```
