import json
import os.path
import subprocess
import uuid
from typing import Dict, Any

import click

from cloud_common.protocols.unit import base
from cloud_common.protocols.unit.v7.message import AosUnitMessageV7
from cloud_common.protocols.unit.v7.common import AosIdentity
from cloud_common.schemas.service_config.aos_config import AosConfigSchema
from cloud_common.schemas.unit_update.aos_update import AosUpdateSchema
from cloud_common.protocols.unit.unit_config import UnitConfig
from cloud_common.schemas.v2.cloud_income import AosUploadMetaConfig

DOCS_BASE_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..',
    'unit-cloud',
))


def generate_schema_file(schema: Dict[str, Any], filename: str) -> str:
    schema_filename = os.path.join(DOCS_BASE_DIR, filename)
    with open(schema_filename, 'wt') as file_handler:
        file_handler.write(json.dumps(schema, indent=4))
        file_handler.write('\n')
    print(f'Schema generated at {schema_filename}')

    return schema_filename


def generate_cloud_income_schema() -> str:
    return generate_schema_file(AosUploadMetaConfig.model_json_schema(), 'aos-cloud-income.schema.json')


def generate_unitconfig_schema() -> str:
    return generate_schema_file(UnitConfig.model_json_schema(), 'aos-unit-config.schema.json')


def generate_schema() -> str:
    schema = base.AosUnitMessage.model_json_schema()
    schema_filename = os.path.join(DOCS_BASE_DIR, 'aos-unit-messages.schema.json')
    with open(schema_filename, 'wt') as file_handler:
        file_handler.write(json.dumps(schema, indent=4))
        file_handler.write('\n')
    print(f'Schema generated at {schema_filename}')

    return schema_filename


def generate_schema_v7() -> str:
    schema = AosUnitMessageV7.model_json_schema()
    schema_filename = os.path.join(DOCS_BASE_DIR, 'aos-unit-messages-v7.schema.json')
    with open(schema_filename, 'wt') as file_handler:
        file_handler.write(json.dumps(schema, indent=4))
        file_handler.write('\n')
    print(f'Schema V7 generated at {schema_filename}')

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
    subprocess.run([
        'generate-schema-doc',
        '--config-file',
        os.path.join(DOCS_BASE_DIR, 'config-html.yaml'),
        generate_schema(),
        os.path.join(DOCS_BASE_DIR, 'html'),
    ])

    subprocess.run([
        'generate-schema-doc',
        '--config-file',
        os.path.join(DOCS_BASE_DIR, 'config-html.yaml'),
        generate_schema_v7(),
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
        # generate_service_schema(),
        # generate_update_schema(),
        # generate_unitconfig_schema(),
        generate_cloud_income_schema(),
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
    id_ = AosIdentity(id=uuid.uuid4(), codename='codename')
    json_ = id_.model_dump(mode='json', by_alias=True, exclude_none=True)
    print(json_)
    print(AosIdentity.model_validate(json_))

    id_ = AosIdentity()
    print(id_.model_dump(mode='json', by_alias=True, exclude_none=True))

    cli()
