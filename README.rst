============
derex.runner
============


.. image:: https://dev.azure.com/abstract-technology/derex.demo/_apis/build/status/Abstract-Tech.derex.demo?branchName=master
        :target: https://dev.azure.com/abstract-technology/derex.demo/_build

Demo plugin for derex.runner

Quickstart
----------

When this package is installed the derex.runner ddc-ironwood command loads an additional docker-compose configuration file.
The plugin is discovered through setuptools entrypoint.

Development setup
-----------------

Make sure you have direnv installed and configured. Also, set up git pre commit hooks. ::

    direnv allow
    pip install pre-commit
    pre-commit install --install-hooks
