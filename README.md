# GeneWeaver
## GPU-Accelerated CRISPR Alignment Engine

GeneWeaver is a Python-based project designed to identify potential CRISPR off-target sites through DNA sequence alignment and mismatch analysis.

The project aims to combine CPU-based alignment, GPU acceleration, and distributed processing to improve the performance of large-scale genomic sequence analysis.

## Planned Features

- FASTA genome sequence parsing using Biopython.
- DNA sequence preprocessing and cleaning.
- CPU-based alignment as a performance baseline.
- GPU-accelerated alignment using Numba CUDA.
- Distributed processing using Dask.
- PAM sequence validation.
- Mismatch analysis and off-target risk scoring.
- Interactive terminal dashboard using Textual.
- Performance monitoring and benchmarking.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Biopython | FASTA parsing |
| NumPy | Numerical operations |
| Numba | CPU/GPU acceleration |
| Dask | Distributed processing |
| Textual | Terminal dashboard |
| Pytest | Automated testing |

## Hardware Note

Local development and CPU testing will be performed on a Windows laptop. Actual CUDA execution and GPU performance benchmarking will require access to a compatible NVIDIA GPU.

## Project Status

**Current phase:** Day 1 – Environment and project structure setup.

The features listed above are planned and will be implemented progressively.

## Disclaimer

GeneWeaver is an educational computational biology project. Its off-target predictions are computational estimates and must not be treated as clinically validated results.
