## Introduction
This simple assembler was done as part of Project 6 of my [nand2tetris](https://github.com/paudsu01/nand2tetris) course. This assembler translates HACK assembly language into the binary instructions and creates a `.hack` file

## Prerequisites
* Need `python` installed
* Clone the repo: `git clone git@github.com:paudsu01/Nand2TetrisAssembler.git ~/Nand2TetrisAssembler`

## How to run the assembler
* Open terminal and `cd ~/Nand2TetrisAssembler`
*  Run the assembler with `python assembler.py path/to/asmFile.asm`

#### Assembling a sample .asm file (`pong.asm`)
*  Assemble the `pong.asm` inside the `sample_files` directory with `python assembler.py sample_files/pong.asm`.
*  This will produce `pong.hack` file inside the `sample_files` directory
  
## Asssumptions
* It assumes the `asm` file provided is error-free.
