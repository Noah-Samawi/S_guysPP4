FROM gitpod/workspace-full

RUN wget -qO- https://cli-assets.heroku.com/install-linux | sh && \
    echo 'export PATH="/app/.heroku/client:$PATH"' >> ~/.bashrc && \
    echo 'export PATH="/app/.heroku/client:$PATH"' >> ~/.zshrc