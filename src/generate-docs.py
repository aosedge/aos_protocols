import json
import os.path
import subprocess

import click

from cloud_common.protocols.unit import base
from cloud_common.schemas.service_config.aos_config import AosConfigSchema
from cloud_common.schemas.unit_update.aos_update import AosUpdateSchema
from cloud_common.protocols.unit.unit_config import UnitConfig

DOCS_BASE_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..',
    'unit-cloud',
))

def generate_unitconfig_schema() -> str:
    schema = UnitConfig.model_json_schema()
    schema_filename = os.path.join(DOCS_BASE_DIR, 'aos-unit-config.schema.json')
    with open(schema_filename, 'wt') as file_handler:
        file_handler.write(json.dumps(schema, indent=4))
        file_handler.write('\n')
    print(f'Schema generated at {schema_filename}')

    return schema_filename


def generate_schema() -> str:
    schema = base.AosUnitMessage.model_json_schema()
    schema_filename = os.path.join(DOCS_BASE_DIR, 'aos-unit-messages.schema.json')
    with open(schema_filename, 'wt') as file_handler:
        file_handler.write(json.dumps(schema, indent=4))
        file_handler.write('\n')
    print(f'Schema generated at {schema_filename}')

    return schema_filename


def generate_service_schema() -> str:
    schema = AosConfigSchema.model_json_schema()
    schema_filename = os.path.join(DOCS_BASE_DIR, 'aos-service-config.schema.json')
    with open(schema_filename, 'wt') as file_handler:
        file_handler.write(json.dumps(schema, indent=4))
        file_handler.write('\n')
    print(f'Schema generated at {schema_filename}')

    return schema_filename


def generate_update_schema() -> str:
    schema = AosUpdateSchema.model_json_schema()
    schema_filename = os.path.join(DOCS_BASE_DIR, 'aos-update.schema.json')
    with open(schema_filename, 'wt') as file_handler:
        file_handler.write(json.dumps(schema, indent=4))
        file_handler.write('\n')
    print(f'Schema generated at {schema_filename}')

    return schema_filename

@click.group()
def cli():
    """Entry point for the CLI."""


@cli.command()
def html():
    schema_filename = generate_schema()

    subprocess.run([
        'generate-schema-doc',
        '--config-file',
        os.path.join(DOCS_BASE_DIR, 'config-html.yaml'),
        schema_filename,
        os.path.join(DOCS_BASE_DIR, 'html'),
    ])


@cli.command()
def md():
    schema_filename = generate_schema()

    subprocess.run([
        'generate-schema-doc',
        '--config-file',
        os.path.join(DOCS_BASE_DIR, 'config-md.yaml'),
        schema_filename,
        os.path.join(DOCS_BASE_DIR, 'md'),
    ])


@cli.command()
def both():
    schema_filename = generate_schema()

    subprocess.run([
        'generate-schema-doc',
        '--config-file',
        os.path.join(DOCS_BASE_DIR, 'config-html.yaml'),
        schema_filename,
        os.path.join(DOCS_BASE_DIR, 'html'),
    ])

    subprocess.run([
        'generate-schema-doc',
        '--config-file',
        os.path.join(DOCS_BASE_DIR, 'config-md.yaml'),
        schema_filename,
        os.path.join(DOCS_BASE_DIR, 'md'),
    ])


@cli.command()
def schemas():
    schema_filenames = [
#        generate_service_schema(),
#        generate_update_schema(),
        generate_unitconfig_schema(),
    ]

    for schema_filename in schema_filenames:
        subprocess.run([
            'generate-schema-doc',
            '--config-file',
            os.path.join(DOCS_BASE_DIR, 'config-html.yaml'),
            schema_filename,
            os.path.join(DOCS_BASE_DIR, 'html'),
        ])

        subprocess.run([
            'generate-schema-doc',
            '--config-file',
            os.path.join(DOCS_BASE_DIR, 'config-md.yaml'),
            schema_filename,
            os.path.join(DOCS_BASE_DIR, 'md'),
        ])


if __name__ == '__main__':
    cli()
