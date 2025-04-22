import subprocess
import sys
from pathlib import Path


def main():
    argv = sys.argv[1:]
    fastqc_path = Path(__file__).resolve().parent.parent.joinpath("fastqc_lib")
    fastqc_path_str = str(fastqc_path).replace("\\", "/")
    classpath = ".;./sam-1.103.jar;./jbzip2-0.9.jar".replace(".", fastqc_path_str)
    subprocess.Popen(
        f"java -Xmx250m -classpath {classpath} uk.ac.babraham.FastQC.FastQCApplication "
        + " ".join(argv),
        shell=True,
    )


if __name__ == "__main__":
    main()
