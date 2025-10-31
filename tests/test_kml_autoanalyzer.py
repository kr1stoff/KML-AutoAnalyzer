from src.kml_autoanalyzer.ilmn_bcl2fastq import ilmn_bcl2fastq
from src.kml_autoanalyzer.args import Arguments

# 250806_NB501947_0944_AHWV3CAFX7
# rsync -auvP --exclude 'CopyComplete.txt' /data/rawdata/illumina/NEXTseq500/250806_NB501947_0944_AHWV3CAFX7/ /data/mengxf/Project/KML251030-AUTO-BCL2FASTQ/test-bcl/250806_NB501947_0944_AHWV3CAFX7/
# cp /data/rawdata/illumina/NEXTseq500/250806_NB501947_0944_AHWV3CAFX7/CopyComplete.txt /data/mengxf/Project/KML251030-AUTO-BCL2FASTQ/test-bcl/250806_NB501947_0944_AHWV3CAFX7/

flow_cell_id = "HWV3CAFX7"
bcls_dir = "/data/mengxf/Project/KML251030-AUTO-BCL2FASTQ/test-bcl"
samplesheet = "/data/mengxf/Project/KML251030-AUTO-BCL2FASTQ/samplesheet.csv"
output_dir = "/data/mengxf/Project/KML251030-AUTO-BCL2FASTQ/FASTQ"
interval = 5
threads = 32

args = Arguments(flow_cell_id, bcls_dir, samplesheet, output_dir, interval, threads)

ilmn_bcl2fastq(args)
