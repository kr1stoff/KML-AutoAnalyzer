from dataclasses import dataclass
from pathlib import Path


@dataclass
class Arguments:
    run_id: str
    bcls_dir: str
    samplesheet: str
    output_dir_str: str
    interval: int
    barocode_mismatchs: int
    threads: int

    def __post_init__(self):
        self.output_dir = Path(self.output_dir_str)
        self.output_dir.mkdir(parents=True, exist_ok=True)
