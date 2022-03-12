# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.194.3/containers/dotnet/.devcontainer/base.Dockerfile

FROM python:3-bullseye

# Copy library scripts to execute
COPY library-scripts/*.sh /tmp/library-scripts/

# [Option] Install zsh
ARG INSTALL_ZSH="true"
# [Option] Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="true"
# Install needed packages and setup non-root user. Use a separate RUN statement to add your own dependencies.
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "true" "true"

# Remove library scripts for final image
RUN rm -rf /tmp/library-scripts

# install any other tools I want
RUN apt-get install -y tree coreutils vim

# install precompiled python packages
RUN apt-get install -y python3-numpy

# upgrade pip
RUN pip install --upgrade pip

# clean up cache
RUN apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

USER vscode

# install pip packages as user
RUN pip install --no-cache-dir --user matplotlib pandas cpi
