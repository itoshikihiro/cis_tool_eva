# Use Ubuntu as the base image
FROM ubuntu:22.04

# Set environment variables to non-interactive (this prevents prompts during package installation)
ENV DEBIAN_FRONTEND=noninteractive

# copy current folder to the docker container
COPY . /test
WORKDIR /test

# Update and install dependencies
RUN apt update && \
    apt install -y git build-essential cmake libxml2-dev wget


# Download the Miniconda installer script for ARM
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh -O /miniconda.sh

# Run the Miniconda installer
RUN bash /miniconda.sh -b -p /miniconda && \
    rm /miniconda.sh

# Add Miniconda to the PATH
ENV PATH="/miniconda/bin:${PATH}"

# Initialize Conda
RUN conda init bash
