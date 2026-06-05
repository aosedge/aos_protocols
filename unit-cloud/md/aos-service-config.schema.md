# AosConfigSchema

- [![Required](https://img.shields.io/badge/Required-blue) Property `AosConfigSchema > created`](#created)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > author`](#author)
  - [Property `AosConfigSchema > author > anyOf > item 0`](#author_anyOf_i0)
  - [Property `AosConfigSchema > author > anyOf > item 1`](#author_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > skipResourceLimits`](#skipResourceLimits)
  - [Property `AosConfigSchema > skipResourceLimits > anyOf > item 0`](#skipResourceLimits_anyOf_i0)
  - [Property `AosConfigSchema > skipResourceLimits > anyOf > item 1`](#skipResourceLimits_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > balancingPolicy`](#balancingPolicy)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > hostname`](#hostname)
  - [Property `AosConfigSchema > hostname > anyOf > item 0`](#hostname_anyOf_i0)
  - [Property `AosConfigSchema > hostname > anyOf > item 1`](#hostname_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > runners`](#runners)
  - [Property `AosConfigSchema > runners > anyOf > item 0`](#runners_anyOf_i0)
    - [AosConfigSchema > runners > anyOf > item 0 > item 0 items](#runners_anyOf_i0_items)
  - [Property `AosConfigSchema > runners > anyOf > item 1`](#runners_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > runParameters`](#runParameters)
  - [Property `AosConfigSchema > runParameters > anyOf > RunParameters`](#runParameters_anyOf_i0)
    - [Property `AosConfigSchema > runParameters > anyOf > RunParameters > startInterval`](#runParameters_anyOf_i0_startInterval)
      - [Property `AosConfigSchema > runParameters > anyOf > RunParameters > startInterval > anyOf > item 0`](#runParameters_anyOf_i0_startInterval_anyOf_i0)
      - [Property `AosConfigSchema > runParameters > anyOf > RunParameters > startInterval > anyOf > item 1`](#runParameters_anyOf_i0_startInterval_anyOf_i1)
    - [Property `AosConfigSchema > runParameters > anyOf > RunParameters > startBurst`](#runParameters_anyOf_i0_startBurst)
      - [Property `AosConfigSchema > runParameters > anyOf > RunParameters > startBurst > anyOf > item 0`](#runParameters_anyOf_i0_startBurst_anyOf_i0)
      - [Property `AosConfigSchema > runParameters > anyOf > RunParameters > startBurst > anyOf > item 1`](#runParameters_anyOf_i0_startBurst_anyOf_i1)
    - [Property `AosConfigSchema > runParameters > anyOf > RunParameters > restartInterval`](#runParameters_anyOf_i0_restartInterval)
      - [Property `AosConfigSchema > runParameters > anyOf > RunParameters > restartInterval > anyOf > item 0`](#runParameters_anyOf_i0_restartInterval_anyOf_i0)
      - [Property `AosConfigSchema > runParameters > anyOf > RunParameters > restartInterval > anyOf > item 1`](#runParameters_anyOf_i0_restartInterval_anyOf_i1)
  - [Property `AosConfigSchema > runParameters > anyOf > item 1`](#runParameters_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > offlineTTL`](#offlineTTL)
  - [Property `AosConfigSchema > offlineTTL > anyOf > item 0`](#offlineTTL_anyOf_i0)
  - [Property `AosConfigSchema > offlineTTL > anyOf > item 1`](#offlineTTL_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > devices`](#devices)
  - [Property `AosConfigSchema > devices > anyOf > UnitDevice`](#devices_anyOf_i0)
    - [Property `AosConfigSchema > devices > anyOf > UnitDevice > name`](#devices_anyOf_i0_name)
    - [Property `AosConfigSchema > devices > anyOf > UnitDevice > permissions`](#devices_anyOf_i0_permissions)
  - [Property `AosConfigSchema > devices > anyOf > item 1`](#devices_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > resources`](#resources)
  - [Property `AosConfigSchema > resources > anyOf > item 0`](#resources_anyOf_i0)
    - [AosConfigSchema > resources > anyOf > item 0 > item 0 items](#resources_anyOf_i0_items)
  - [Property `AosConfigSchema > resources > anyOf > item 1`](#resources_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > allowedConnections`](#allowedConnections)
  - [Property `AosConfigSchema > allowedConnections > anyOf > item 0`](#allowedConnections_anyOf_i0)
    - [AosConfigSchema > allowedConnections > anyOf > item 0 > item 0 items](#allowedConnections_anyOf_i0_items)
  - [Property `AosConfigSchema > allowedConnections > anyOf > item 1`](#allowedConnections_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > quotas`](#quotas)
  - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas`](#quotas_anyOf_i0)
    - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > cpuLimit`](#quotas_anyOf_i0_cpuLimit)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > cpuLimit > anyOf > item 0`](#quotas_anyOf_i0_cpuLimit_anyOf_i0)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > cpuLimit > anyOf > item 1`](#quotas_anyOf_i0_cpuLimit_anyOf_i1)
    - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > cpuDmipsLimit`](#quotas_anyOf_i0_cpuDmipsLimit)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > cpuDmipsLimit > anyOf > item 0`](#quotas_anyOf_i0_cpuDmipsLimit_anyOf_i0)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > cpuDmipsLimit > anyOf > item 1`](#quotas_anyOf_i0_cpuDmipsLimit_anyOf_i1)
    - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > ramLimit`](#quotas_anyOf_i0_ramLimit)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > ramLimit > anyOf > item 0`](#quotas_anyOf_i0_ramLimit_anyOf_i0)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > ramLimit > anyOf > item 1`](#quotas_anyOf_i0_ramLimit_anyOf_i1)
    - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > storageLimit`](#quotas_anyOf_i0_storageLimit)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > storageLimit > anyOf > item 0`](#quotas_anyOf_i0_storageLimit_anyOf_i0)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > storageLimit > anyOf > item 1`](#quotas_anyOf_i0_storageLimit_anyOf_i1)
    - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > stateLimit`](#quotas_anyOf_i0_stateLimit)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > stateLimit > anyOf > item 0`](#quotas_anyOf_i0_stateLimit_anyOf_i0)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > stateLimit > anyOf > item 1`](#quotas_anyOf_i0_stateLimit_anyOf_i1)
    - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > tmpLimit`](#quotas_anyOf_i0_tmpLimit)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > tmpLimit > anyOf > item 0`](#quotas_anyOf_i0_tmpLimit_anyOf_i0)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > tmpLimit > anyOf > item 1`](#quotas_anyOf_i0_tmpLimit_anyOf_i1)
    - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > uploadSpeed`](#quotas_anyOf_i0_uploadSpeed)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > uploadSpeed > anyOf > item 0`](#quotas_anyOf_i0_uploadSpeed_anyOf_i0)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > uploadSpeed > anyOf > item 1`](#quotas_anyOf_i0_uploadSpeed_anyOf_i1)
    - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > downloadSpeed`](#quotas_anyOf_i0_downloadSpeed)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > downloadSpeed > anyOf > item 0`](#quotas_anyOf_i0_downloadSpeed_anyOf_i0)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > downloadSpeed > anyOf > item 1`](#quotas_anyOf_i0_downloadSpeed_anyOf_i1)
    - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > noFileLimit`](#quotas_anyOf_i0_noFileLimit)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > noFileLimit > anyOf > item 0`](#quotas_anyOf_i0_noFileLimit_anyOf_i0)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > noFileLimit > anyOf > item 1`](#quotas_anyOf_i0_noFileLimit_anyOf_i1)
    - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > pidsLimit`](#quotas_anyOf_i0_pidsLimit)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > pidsLimit > anyOf > item 0`](#quotas_anyOf_i0_pidsLimit_anyOf_i0)
      - [Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > pidsLimit > anyOf > item 1`](#quotas_anyOf_i0_pidsLimit_anyOf_i1)
  - [Property `AosConfigSchema > quotas > anyOf > item 1`](#quotas_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > requestedResources`](#requestedResources)
  - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources`](#requestedResources_anyOf_i0)
    - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > cpu`](#requestedResources_anyOf_i0_cpu)
      - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > cpu > anyOf > item 0`](#requestedResources_anyOf_i0_cpu_anyOf_i0)
      - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > cpu > anyOf > item 1`](#requestedResources_anyOf_i0_cpu_anyOf_i1)
    - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > ram`](#requestedResources_anyOf_i0_ram)
      - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > ram > anyOf > item 0`](#requestedResources_anyOf_i0_ram_anyOf_i0)
      - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > ram > anyOf > item 1`](#requestedResources_anyOf_i0_ram_anyOf_i1)
    - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > storage`](#requestedResources_anyOf_i0_storage)
      - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > storage > anyOf > item 0`](#requestedResources_anyOf_i0_storage_anyOf_i0)
      - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > storage > anyOf > item 1`](#requestedResources_anyOf_i0_storage_anyOf_i1)
    - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > state`](#requestedResources_anyOf_i0_state)
      - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > state > anyOf > item 0`](#requestedResources_anyOf_i0_state_anyOf_i0)
      - [Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > state > anyOf > item 1`](#requestedResources_anyOf_i0_state_anyOf_i1)
  - [Property `AosConfigSchema > requestedResources > anyOf > item 1`](#requestedResources_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > alertRules`](#alertRules)
  - [Property `AosConfigSchema > alertRules > anyOf > AlertRules`](#alertRules_anyOf_i0)
    - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram`](#alertRules_anyOf_i0_ram)
      - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents`](#alertRules_anyOf_i0_ram_anyOf_i0)
        - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > minTimeout`](#alertRules_anyOf_i0_ram_anyOf_i0_minTimeout)
          - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > minTimeout > anyOf > item 0`](#alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i0)
          - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > minTimeout > anyOf > item 1`](#alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i1)
        - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > minThreshold`](#alertRules_anyOf_i0_ram_anyOf_i0_minThreshold)
          - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > minThreshold > anyOf > item 0`](#alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i0)
          - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > minThreshold > anyOf > item 1`](#alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i1)
        - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > maxThreshold`](#alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold)
          - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > maxThreshold > anyOf > item 0`](#alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i0)
          - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > maxThreshold > anyOf > item 1`](#alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i1)
      - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > item 1`](#alertRules_anyOf_i0_ram_anyOf_i1)
    - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > cpu`](#alertRules_anyOf_i0_cpu)
      - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > cpu > anyOf > AlertRulePercents`](#alertRules_anyOf_i0_cpu_anyOf_i0)
      - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > cpu > anyOf > item 1`](#alertRules_anyOf_i0_cpu_anyOf_i1)
    - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > storage`](#alertRules_anyOf_i0_storage)
      - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > storage > anyOf > AlertRulePercents`](#alertRules_anyOf_i0_storage_anyOf_i0)
      - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > storage > anyOf > item 1`](#alertRules_anyOf_i0_storage_anyOf_i1)
    - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload`](#alertRules_anyOf_i0_upload)
      - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints`](#alertRules_anyOf_i0_upload_anyOf_i0)
        - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > minTimeout`](#alertRules_anyOf_i0_upload_anyOf_i0_minTimeout)
          - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > minTimeout > anyOf > item 0`](#alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i0)
          - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > minTimeout > anyOf > item 1`](#alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i1)
        - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > minThreshold`](#alertRules_anyOf_i0_upload_anyOf_i0_minThreshold)
          - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > minThreshold > anyOf > item 0`](#alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i0)
          - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > minThreshold > anyOf > item 1`](#alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i1)
        - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > maxThreshold`](#alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold)
          - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > maxThreshold > anyOf > item 0`](#alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i0)
          - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > maxThreshold > anyOf > item 1`](#alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i1)
      - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > item 1`](#alertRules_anyOf_i0_upload_anyOf_i1)
    - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > download`](#alertRules_anyOf_i0_download)
      - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > download > anyOf > AlertRulePoints`](#alertRules_anyOf_i0_download_anyOf_i0)
      - [Property `AosConfigSchema > alertRules > anyOf > AlertRules > download > anyOf > item 1`](#alertRules_anyOf_i0_download_anyOf_i1)
  - [Property `AosConfigSchema > alertRules > anyOf > item 1`](#alertRules_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > permissions`](#permissions)
  - [Property `AosConfigSchema > permissions > anyOf > item 0`](#permissions_anyOf_i0)
    - [Property `AosConfigSchema > permissions > anyOf > item 0 > additionalProperties`](#permissions_anyOf_i0_additionalProperties)
      - [Property `AosConfigSchema > permissions > anyOf > item 0 > additionalProperties > additionalProperties`](#permissions_anyOf_i0_additionalProperties_additionalProperties)
  - [Property `AosConfigSchema > permissions > anyOf > item 1`](#permissions_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > sysctl`](#sysctl)
  - [Property `AosConfigSchema > sysctl > anyOf > item 0`](#sysctl_anyOf_i0)
    - [Property `AosConfigSchema > sysctl > anyOf > item 0 > additionalProperties`](#sysctl_anyOf_i0_additionalProperties)
  - [Property `AosConfigSchema > sysctl > anyOf > item 1`](#sysctl_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > dependencies`](#dependencies)
  - [Property `AosConfigSchema > dependencies > anyOf > item 0`](#dependencies_anyOf_i0)
    - [AosConfigSchema > dependencies > anyOf > item 0 > AosDependency](#dependencies_anyOf_i0_items)
      - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier`](#dependencies_anyOf_i0_items_identifier)
        - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > id`](#dependencies_anyOf_i0_items_identifier_id)
          - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > id > anyOf > item 0`](#dependencies_anyOf_i0_items_identifier_id_anyOf_i0)
          - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > id > anyOf > item 1`](#dependencies_anyOf_i0_items_identifier_id_anyOf_i1)
        - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > type`](#dependencies_anyOf_i0_items_identifier_type)
          - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > type > anyOf > AosIdentityType`](#dependencies_anyOf_i0_items_identifier_type_anyOf_i0)
          - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > type > anyOf > item 1`](#dependencies_anyOf_i0_items_identifier_type_anyOf_i1)
        - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > codename`](#dependencies_anyOf_i0_items_identifier_codename)
          - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > codename > anyOf > item 0`](#dependencies_anyOf_i0_items_identifier_codename_anyOf_i0)
          - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > codename > anyOf > item 1`](#dependencies_anyOf_i0_items_identifier_codename_anyOf_i1)
        - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > title`](#dependencies_anyOf_i0_items_identifier_title)
          - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > title > anyOf > item 0`](#dependencies_anyOf_i0_items_identifier_title_anyOf_i0)
          - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > title > anyOf > item 1`](#dependencies_anyOf_i0_items_identifier_title_anyOf_i1)
        - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > description`](#dependencies_anyOf_i0_items_identifier_description)
          - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > description > anyOf > item 0`](#dependencies_anyOf_i0_items_identifier_description_anyOf_i0)
          - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > description > anyOf > item 1`](#dependencies_anyOf_i0_items_identifier_description_anyOf_i1)
        - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > urn`](#dependencies_anyOf_i0_items_identifier_urn)
          - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > urn > anyOf > item 0`](#dependencies_anyOf_i0_items_identifier_urn_anyOf_i0)
          - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > urn > anyOf > item 1`](#dependencies_anyOf_i0_items_identifier_urn_anyOf_i1)
      - [Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > condition`](#dependencies_anyOf_i0_items_condition)
  - [Property `AosConfigSchema > dependencies > anyOf > item 1`](#dependencies_anyOf_i1)

**Title:** AosConfigSchema

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** Aos service config schema.

This schema describes the specification of the `aosService` layer in a service.

| Property                                     | Pattern | Type             | Deprecated | Definition | Title/Description                           |
| -------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------------------------------- |
| + [created](#created )                       | No      | string           | No         | -          | Created                                     |
| - [author](#author )                         | No      | Combination      | No         | -          | Author                                      |
| - [skipResourceLimits](#skipResourceLimits ) | No      | Combination      | No         | -          | Skipresourcelimits                          |
| - [balancingPolicy](#balancingPolicy )       | No      | enum (of string) | No         | -          | Balancingpolicy                             |
| - [hostname](#hostname )                     | No      | Combination      | No         | -          | Hostname                                    |
| - [runners](#runners )                       | No      | Combination      | No         | -          | Runners                                     |
| - [runParameters](#runParameters )           | No      | Combination      | No         | -          | Run parameters for the Aos service.         |
| - [offlineTTL](#offlineTTL )                 | No      | Combination      | No         | -          | Offlinettl                                  |
| - [devices](#devices )                       | No      | Combination      | No         | -          | List of needed or requested devices.        |
| - [resources](#resources )                   | No      | Combination      | No         | -          | Resources                                   |
| - [allowedConnections](#allowedConnections ) | No      | Combination      | No         | -          | Allowedconnections                          |
| - [quotas](#quotas )                         | No      | Combination      | No         | -          | Quotas for the service.                     |
| - [requestedResources](#requestedResources ) | No      | Combination      | No         | -          | Requested Resources (CPU, RAM and Storage). |
| - [alertRules](#alertRules )                 | No      | Combination      | No         | -          | Alert rules for the service.                |
| - [permissions](#permissions )               | No      | Combination      | No         | -          | Permissions                                 |
| - [sysctl](#sysctl )                         | No      | Combination      | No         | -          | Sysctl                                      |
| - [dependencies](#dependencies )             | No      | Combination      | No         | -          | Dependencies                                |

## <a name="created"></a>![Required](https://img.shields.io/badge/Required-blue) Property `AosConfigSchema > created`

**Title:** Created

|            |             |
| ---------- | ----------- |
| **Type**   | `string`    |
| **Format** | `date-time` |

**Description:** Timestamp when Aos service was created.

## <a name="author"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > author`

**Title:** Author

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos service author.

| Any of(Option)             |
| -------------------------- |
| [item 0](#author_anyOf_i0) |
| [item 1](#author_anyOf_i1) |

### <a name="author_anyOf_i0"></a>Property `AosConfigSchema > author > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="author_anyOf_i1"></a>Property `AosConfigSchema > author > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="skipResourceLimits"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > skipResourceLimits`

**Title:** Skipresourcelimits

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Use resource limits or not in pre-release versions.

| Any of(Option)                         |
| -------------------------------------- |
| [item 0](#skipResourceLimits_anyOf_i0) |
| [item 1](#skipResourceLimits_anyOf_i1) |

### <a name="skipResourceLimits_anyOf_i0"></a>Property `AosConfigSchema > skipResourceLimits > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `boolean` |

### <a name="skipResourceLimits_anyOf_i1"></a>Property `AosConfigSchema > skipResourceLimits > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="balancingPolicy"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > balancingPolicy`

**Title:** Balancingpolicy

|             |                    |
| ----------- | ------------------ |
| **Type**    | `enum (of string)` |
| **Default** | `"enabled"`        |

**Description:** Balancing type. `disabled` means total prohibition from balancing to other nodes.`

Must be one of:
* "enabled"
* "disabled"

## <a name="hostname"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > hostname`

**Title:** Hostname

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** The hostname of the Aos service. The FQDN is {hostname].{service_provider}.

| Any of(Option)               |
| ---------------------------- |
| [item 0](#hostname_anyOf_i0) |
| [item 1](#hostname_anyOf_i1) |

### <a name="hostname_anyOf_i0"></a>Property `AosConfigSchema > hostname > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="hostname_anyOf_i1"></a>Property `AosConfigSchema > hostname > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="runners"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > runners`

**Title:** Runners

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos service allowed runner types. Absense means ["runc", "crun"].

| Any of(Option)              |
| --------------------------- |
| [item 0](#runners_anyOf_i0) |
| [item 1](#runners_anyOf_i1) |

### <a name="runners_anyOf_i0"></a>Property `AosConfigSchema > runners > anyOf > item 0`

|          |                             |
| -------- | --------------------------- |
| **Type** | `array of enum (of string)` |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 0 items](#runners_anyOf_i0_items) | -           |

#### <a name="runners_anyOf_i0_items"></a>AosConfigSchema > runners > anyOf > item 0 > item 0 items

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

Must be one of:
* "runc"
* "crun"
* "xrun"

### <a name="runners_anyOf_i1"></a>Property `AosConfigSchema > runners > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="runParameters"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > runParameters`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Run parameters for the Aos service.

| Any of(Option)                           |
| ---------------------------------------- |
| [RunParameters](#runParameters_anyOf_i0) |
| [item 1](#runParameters_anyOf_i1)        |

### <a name="runParameters_anyOf_i0"></a>Property `AosConfigSchema > runParameters > anyOf > RunParameters`

**Title:** RunParameters

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/RunParameters                                                       |

**Description:** Schema for startup parameters.

| Property                                                      | Pattern | Type        | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [startInterval](#runParameters_anyOf_i0_startInterval )     | No      | Combination | No         | -          | Startinterval     |
| - [startBurst](#runParameters_anyOf_i0_startBurst )           | No      | Combination | No         | -          | Startburst        |
| - [restartInterval](#runParameters_anyOf_i0_restartInterval ) | No      | Combination | No         | -          | Restartinterval   |

#### <a name="runParameters_anyOf_i0_startInterval"></a>Property `AosConfigSchema > runParameters > anyOf > RunParameters > startInterval`

**Title:** Startinterval

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** The duration in ISO8601 format to wait service start.

**Examples:**

```json
"PT10S"
```

```json
"PT1M"
```

| Any of(Option)                                           |
| -------------------------------------------------------- |
| [item 0](#runParameters_anyOf_i0_startInterval_anyOf_i0) |
| [item 1](#runParameters_anyOf_i0_startInterval_anyOf_i1) |

##### <a name="runParameters_anyOf_i0_startInterval_anyOf_i0"></a>Property `AosConfigSchema > runParameters > anyOf > RunParameters > startInterval > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

##### <a name="runParameters_anyOf_i0_startInterval_anyOf_i1"></a>Property `AosConfigSchema > runParameters > anyOf > RunParameters > startInterval > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="runParameters_anyOf_i0_startBurst"></a>Property `AosConfigSchema > runParameters > anyOf > RunParameters > startBurst`

**Title:** Startburst

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Service which are started more than burst times within an interval time span are not permitted to start any more.
Use `startInterval` to configure the checking interval and `startBurst`
to configure how many starts per interval are allowed.

**Examples:**

```json
3
```

```json
10
```

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [item 0](#runParameters_anyOf_i0_startBurst_anyOf_i0) |
| [item 1](#runParameters_anyOf_i0_startBurst_anyOf_i1) |

##### <a name="runParameters_anyOf_i0_startBurst_anyOf_i0"></a>Property `AosConfigSchema > runParameters > anyOf > RunParameters > startBurst > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="runParameters_anyOf_i0_startBurst_anyOf_i1"></a>Property `AosConfigSchema > runParameters > anyOf > RunParameters > startBurst > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="runParameters_anyOf_i0_restartInterval"></a>Property `AosConfigSchema > runParameters > anyOf > RunParameters > restartInterval`

**Title:** Restartinterval

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** The duration in ISO8601 format to wait before service restart.

**Examples:**

```json
"PT1S"
```

```json
"PT1M"
```

| Any of(Option)                                             |
| ---------------------------------------------------------- |
| [item 0](#runParameters_anyOf_i0_restartInterval_anyOf_i0) |
| [item 1](#runParameters_anyOf_i0_restartInterval_anyOf_i1) |

##### <a name="runParameters_anyOf_i0_restartInterval_anyOf_i0"></a>Property `AosConfigSchema > runParameters > anyOf > RunParameters > restartInterval > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

##### <a name="runParameters_anyOf_i0_restartInterval_anyOf_i1"></a>Property `AosConfigSchema > runParameters > anyOf > RunParameters > restartInterval > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="runParameters_anyOf_i1"></a>Property `AosConfigSchema > runParameters > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="offlineTTL"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > offlineTTL`

**Title:** Offlinettl

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** TTL (allowed time) to run service when unit in offline mode.
If value is absent service will live on an unit forever.
Format: ISO8601 duration.

**Examples:**

```json
"PT1M"
```

```json
"PT7D"
```

| Any of(Option)                 |
| ------------------------------ |
| [item 0](#offlineTTL_anyOf_i0) |
| [item 1](#offlineTTL_anyOf_i1) |

### <a name="offlineTTL_anyOf_i0"></a>Property `AosConfigSchema > offlineTTL > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

### <a name="offlineTTL_anyOf_i1"></a>Property `AosConfigSchema > offlineTTL > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="devices"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > devices`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** List of needed or requested devices.

| Any of(Option)                  |
| ------------------------------- |
| [UnitDevice](#devices_anyOf_i0) |
| [item 1](#devices_anyOf_i1)     |

### <a name="devices_anyOf_i0"></a>Property `AosConfigSchema > devices > anyOf > UnitDevice`

**Title:** UnitDevice

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/UnitDevice                                                          |

**Description:** Schema for the `device` info structure.

| Property                                        | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [name](#devices_anyOf_i0_name )               | No      | string | No         | -          | Name              |
| + [permissions](#devices_anyOf_i0_permissions ) | No      | string | No         | -          | Permissions       |

#### <a name="devices_anyOf_i0_name"></a>Property `AosConfigSchema > devices > anyOf > UnitDevice > name`

**Title:** Name

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The name of the systems device.

**Examples:**

```json
"camera0"
```

```json
"mic0"
```

#### <a name="devices_anyOf_i0_permissions"></a>Property `AosConfigSchema > devices > anyOf > UnitDevice > permissions`

**Title:** Permissions

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The needed access permissions for the device.

**Examples:**

```json
"r"
```

```json
"rw"
```

```json
"w"
```

### <a name="devices_anyOf_i1"></a>Property `AosConfigSchema > devices > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="resources"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > resources`

**Title:** Resources

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** List of needed resources.

**Examples:**

```json
"bluetooth"
```

```json
"system-dbus"
```

| Any of(Option)                |
| ----------------------------- |
| [item 0](#resources_anyOf_i0) |
| [item 1](#resources_anyOf_i1) |

### <a name="resources_anyOf_i0"></a>Property `AosConfigSchema > resources > anyOf > item 0`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [item 0 items](#resources_anyOf_i0_items) | -           |

#### <a name="resources_anyOf_i0_items"></a>AosConfigSchema > resources > anyOf > item 0 > item 0 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="resources_anyOf_i1"></a>Property `AosConfigSchema > resources > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="allowedConnections"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > allowedConnections`

**Title:** Allowedconnections

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** List of allowed network connections.
Format of connection string: {service_uid}/[port|port_range]/[tcp|udp]

**Examples:**

```json
"9931560c-be75-4f60-9abf-08297d905332/8087:8088/tcp"
```

```json
"9931560c-be75-4f60-9abf-08297d905332/1515/udp"
```

| Any of(Option)                         |
| -------------------------------------- |
| [item 0](#allowedConnections_anyOf_i0) |
| [item 1](#allowedConnections_anyOf_i1) |

### <a name="allowedConnections_anyOf_i0"></a>Property `AosConfigSchema > allowedConnections > anyOf > item 0`

|          |                   |
| -------- | ----------------- |
| **Type** | `array of object` |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                    | Description |
| -------------------------------------------------- | ----------- |
| [item 0 items](#allowedConnections_anyOf_i0_items) | -           |

#### <a name="allowedConnections_anyOf_i0_items"></a>AosConfigSchema > allowedConnections > anyOf > item 0 > item 0 items

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

### <a name="allowedConnections_anyOf_i1"></a>Property `AosConfigSchema > allowedConnections > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="quotas"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > quotas`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Quotas for the service.

| Any of(Option)                    |
| --------------------------------- |
| [ServiceQuotas](#quotas_anyOf_i0) |
| [item 1](#quotas_anyOf_i1)        |

### <a name="quotas_anyOf_i0"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas`

**Title:** ServiceQuotas

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/ServiceQuotas                                                       |

**Description:** Schema for possible quotas for a service.

| Property                                           | Pattern | Type        | Deprecated | Definition | Title/Description |
| -------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [cpuLimit](#quotas_anyOf_i0_cpuLimit )           | No      | Combination | No         | -          | Cpulimit          |
| - [cpuDmipsLimit](#quotas_anyOf_i0_cpuDmipsLimit ) | No      | Combination | No         | -          | Cpudmipslimit     |
| - [ramLimit](#quotas_anyOf_i0_ramLimit )           | No      | Combination | No         | -          | Ramlimit          |
| - [storageLimit](#quotas_anyOf_i0_storageLimit )   | No      | Combination | No         | -          | Storagelimit      |
| - [stateLimit](#quotas_anyOf_i0_stateLimit )       | No      | Combination | No         | -          | Statelimit        |
| - [tmpLimit](#quotas_anyOf_i0_tmpLimit )           | No      | Combination | No         | -          | Tmplimit          |
| - [uploadSpeed](#quotas_anyOf_i0_uploadSpeed )     | No      | Combination | No         | -          | Uploadspeed       |
| - [downloadSpeed](#quotas_anyOf_i0_downloadSpeed ) | No      | Combination | No         | -          | Downloadspeed     |
| - [noFileLimit](#quotas_anyOf_i0_noFileLimit )     | No      | Combination | No         | -          | Nofilelimit       |
| - [pidsLimit](#quotas_anyOf_i0_pidsLimit )         | No      | Combination | No         | -          | Pidslimit         |

#### <a name="quotas_anyOf_i0_cpuLimit"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > cpuLimit`

**Title:** Cpulimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** CPU limit in percents

| Any of(Option)                               |
| -------------------------------------------- |
| [item 0](#quotas_anyOf_i0_cpuLimit_anyOf_i0) |
| [item 1](#quotas_anyOf_i0_cpuLimit_anyOf_i1) |

##### <a name="quotas_anyOf_i0_cpuLimit_anyOf_i0"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > cpuLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_cpuLimit_anyOf_i1"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > cpuLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_cpuDmipsLimit"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > cpuDmipsLimit`

**Title:** Cpudmipslimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** CPU limit in DMIPs

| Any of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#quotas_anyOf_i0_cpuDmipsLimit_anyOf_i0) |
| [item 1](#quotas_anyOf_i0_cpuDmipsLimit_anyOf_i1) |

##### <a name="quotas_anyOf_i0_cpuDmipsLimit_anyOf_i0"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > cpuDmipsLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_cpuDmipsLimit_anyOf_i1"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > cpuDmipsLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_ramLimit"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > ramLimit`

**Title:** Ramlimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** RAM limit in bytes

| Any of(Option)                               |
| -------------------------------------------- |
| [item 0](#quotas_anyOf_i0_ramLimit_anyOf_i0) |
| [item 1](#quotas_anyOf_i0_ramLimit_anyOf_i1) |

##### <a name="quotas_anyOf_i0_ramLimit_anyOf_i0"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > ramLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_ramLimit_anyOf_i1"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > ramLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_storageLimit"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > storageLimit`

**Title:** Storagelimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Storage limit in bytes

| Any of(Option)                                   |
| ------------------------------------------------ |
| [item 0](#quotas_anyOf_i0_storageLimit_anyOf_i0) |
| [item 1](#quotas_anyOf_i0_storageLimit_anyOf_i1) |

##### <a name="quotas_anyOf_i0_storageLimit_anyOf_i0"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > storageLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_storageLimit_anyOf_i1"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > storageLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_stateLimit"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > stateLimit`

**Title:** Statelimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** State limit in bytes

| Any of(Option)                                 |
| ---------------------------------------------- |
| [item 0](#quotas_anyOf_i0_stateLimit_anyOf_i0) |
| [item 1](#quotas_anyOf_i0_stateLimit_anyOf_i1) |

##### <a name="quotas_anyOf_i0_stateLimit_anyOf_i0"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > stateLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_stateLimit_anyOf_i1"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > stateLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_tmpLimit"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > tmpLimit`

**Title:** Tmplimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Temporary storage limit in bytes

| Any of(Option)                               |
| -------------------------------------------- |
| [item 0](#quotas_anyOf_i0_tmpLimit_anyOf_i0) |
| [item 1](#quotas_anyOf_i0_tmpLimit_anyOf_i1) |

##### <a name="quotas_anyOf_i0_tmpLimit_anyOf_i0"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > tmpLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_tmpLimit_anyOf_i1"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > tmpLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_uploadSpeed"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > uploadSpeed`

**Title:** Uploadspeed

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Upload limit in bytes per second

| Any of(Option)                                  |
| ----------------------------------------------- |
| [item 0](#quotas_anyOf_i0_uploadSpeed_anyOf_i0) |
| [item 1](#quotas_anyOf_i0_uploadSpeed_anyOf_i1) |

##### <a name="quotas_anyOf_i0_uploadSpeed_anyOf_i0"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > uploadSpeed > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_uploadSpeed_anyOf_i1"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > uploadSpeed > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_downloadSpeed"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > downloadSpeed`

**Title:** Downloadspeed

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Upload limit in bytes per second

| Any of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#quotas_anyOf_i0_downloadSpeed_anyOf_i0) |
| [item 1](#quotas_anyOf_i0_downloadSpeed_anyOf_i1) |

##### <a name="quotas_anyOf_i0_downloadSpeed_anyOf_i0"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > downloadSpeed > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_downloadSpeed_anyOf_i1"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > downloadSpeed > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_noFileLimit"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > noFileLimit`

**Title:** Nofilelimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Limit of opened files

| Any of(Option)                                  |
| ----------------------------------------------- |
| [item 0](#quotas_anyOf_i0_noFileLimit_anyOf_i0) |
| [item 1](#quotas_anyOf_i0_noFileLimit_anyOf_i1) |

##### <a name="quotas_anyOf_i0_noFileLimit_anyOf_i0"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > noFileLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_noFileLimit_anyOf_i1"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > noFileLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_pidsLimit"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > pidsLimit`

**Title:** Pidslimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Limit of PIDs

| Any of(Option)                                |
| --------------------------------------------- |
| [item 0](#quotas_anyOf_i0_pidsLimit_anyOf_i0) |
| [item 1](#quotas_anyOf_i0_pidsLimit_anyOf_i1) |

##### <a name="quotas_anyOf_i0_pidsLimit_anyOf_i0"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > pidsLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_pidsLimit_anyOf_i1"></a>Property `AosConfigSchema > quotas > anyOf > ServiceQuotas > pidsLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="quotas_anyOf_i1"></a>Property `AosConfigSchema > quotas > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="requestedResources"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > requestedResources`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Requested Resources (CPU, RAM and Storage).

| Any of(Option)                                     |
| -------------------------------------------------- |
| [RequestedResources](#requestedResources_anyOf_i0) |
| [item 1](#requestedResources_anyOf_i1)             |

### <a name="requestedResources_anyOf_i0"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources`

**Title:** RequestedResources

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/RequestedResources                                                  |

**Description:** Schema for requested resources.

| Property                                           | Pattern | Type        | Deprecated | Definition | Title/Description |
| -------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [cpu](#requestedResources_anyOf_i0_cpu )         | No      | Combination | No         | -          | Cpu               |
| - [ram](#requestedResources_anyOf_i0_ram )         | No      | Combination | No         | -          | Ram               |
| - [storage](#requestedResources_anyOf_i0_storage ) | No      | Combination | No         | -          | Storage           |
| - [state](#requestedResources_anyOf_i0_state )     | No      | Combination | No         | -          | State             |

#### <a name="requestedResources_anyOf_i0_cpu"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > cpu`

**Title:** Cpu

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** CPU requested resource (against cpuLimit)

| Any of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#requestedResources_anyOf_i0_cpu_anyOf_i0) |
| [item 1](#requestedResources_anyOf_i0_cpu_anyOf_i1) |

##### <a name="requestedResources_anyOf_i0_cpu_anyOf_i0"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > cpu > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="requestedResources_anyOf_i0_cpu_anyOf_i1"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > cpu > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="requestedResources_anyOf_i0_ram"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > ram`

**Title:** Ram

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** RAM requested resource (against ramLimit)

| Any of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#requestedResources_anyOf_i0_ram_anyOf_i0) |
| [item 1](#requestedResources_anyOf_i0_ram_anyOf_i1) |

##### <a name="requestedResources_anyOf_i0_ram_anyOf_i0"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > ram > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="requestedResources_anyOf_i0_ram_anyOf_i1"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > ram > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="requestedResources_anyOf_i0_storage"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > storage`

**Title:** Storage

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Storage requested resource (against storageLimit)

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#requestedResources_anyOf_i0_storage_anyOf_i0) |
| [item 1](#requestedResources_anyOf_i0_storage_anyOf_i1) |

##### <a name="requestedResources_anyOf_i0_storage_anyOf_i0"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > storage > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="requestedResources_anyOf_i0_storage_anyOf_i1"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > storage > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="requestedResources_anyOf_i0_state"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > state`

**Title:** State

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** State requested resource (against stateLimit)

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [item 0](#requestedResources_anyOf_i0_state_anyOf_i0) |
| [item 1](#requestedResources_anyOf_i0_state_anyOf_i1) |

##### <a name="requestedResources_anyOf_i0_state_anyOf_i0"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > state > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="requestedResources_anyOf_i0_state_anyOf_i1"></a>Property `AosConfigSchema > requestedResources > anyOf > RequestedResources > state > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="requestedResources_anyOf_i1"></a>Property `AosConfigSchema > requestedResources > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="alertRules"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > alertRules`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Alert rules for the service.

| Any of(Option)                     |
| ---------------------------------- |
| [AlertRules](#alertRules_anyOf_i0) |
| [item 1](#alertRules_anyOf_i1)     |

### <a name="alertRules_anyOf_i0"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules`

**Title:** AlertRules

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AlertRules                                                          |

**Description:** Schema for all possible alert rules.

| Property                                     | Pattern | Type        | Deprecated | Definition | Title/Description        |
| -------------------------------------------- | ------- | ----------- | ---------- | ---------- | ------------------------ |
| - [ram](#alertRules_anyOf_i0_ram )           | No      | Combination | No         | -          | RAM alert settings.      |
| - [cpu](#alertRules_anyOf_i0_cpu )           | No      | Combination | No         | -          | CPU alert settings.      |
| - [storage](#alertRules_anyOf_i0_storage )   | No      | Combination | No         | -          | Storage alert settings.  |
| - [upload](#alertRules_anyOf_i0_upload )     | No      | Combination | No         | -          | Upload alert settings.   |
| - [download](#alertRules_anyOf_i0_download ) | No      | Combination | No         | -          | Download alert settings. |

#### <a name="alertRules_anyOf_i0_ram"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** RAM alert settings.

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [AlertRulePercents](#alertRules_anyOf_i0_ram_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_ram_anyOf_i1)            |

##### <a name="alertRules_anyOf_i0_ram_anyOf_i0"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents`

**Title:** AlertRulePercents

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AlertRulePercents                                                   |

**Description:** Schema alert triggering procedure in percents.

| Property                                                          | Pattern | Type        | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [minTimeout](#alertRules_anyOf_i0_ram_anyOf_i0_minTimeout )     | No      | Combination | No         | -          | Mintimeout        |
| + [minThreshold](#alertRules_anyOf_i0_ram_anyOf_i0_minThreshold ) | No      | Combination | No         | -          | Minthreshold      |
| + [maxThreshold](#alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold ) | No      | Combination | No         | -          | Maxthreshold      |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_minTimeout"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > minTimeout`

**Title:** Mintimeout

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** The duration in ISO8601 for a time window to check alert rule.

**Examples:**

```json
"PT10S"
```

```json
"PT1M"
```

| Any of(Option)                                                  |
| --------------------------------------------------------------- |
| [item 0](#alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i1) |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i0"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > minTimeout > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i1"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > minTimeout > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_minThreshold"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > minThreshold`

**Title:** Minthreshold

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** The minimum threshold to stop alert.

| Any of(Option)                                                    |
| ----------------------------------------------------------------- |
| [item 0](#alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i1) |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i0"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > minThreshold > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `number` |

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i1"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > minThreshold > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > maxThreshold`

**Title:** Maxthreshold

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** The maximum threshold value to start alert.

| Any of(Option)                                                    |
| ----------------------------------------------------------------- |
| [item 0](#alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i1) |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i0"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > maxThreshold > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `number` |

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i1"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > AlertRulePercents > maxThreshold > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="alertRules_anyOf_i0_ram_anyOf_i1"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > ram > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="alertRules_anyOf_i0_cpu"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > cpu`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** CPU alert settings.

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [AlertRulePercents](#alertRules_anyOf_i0_cpu_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_cpu_anyOf_i1)            |

##### <a name="alertRules_anyOf_i0_cpu_anyOf_i0"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > cpu > anyOf > AlertRulePercents`

**Title:** AlertRulePercents

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Same definition as**    | [AlertRulePercents](#alertRules_anyOf_i0_ram_anyOf_i0)                      |

**Description:** Schema alert triggering procedure in percents.

##### <a name="alertRules_anyOf_i0_cpu_anyOf_i1"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > cpu > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="alertRules_anyOf_i0_storage"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > storage`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Storage alert settings.

| Any of(Option)                                             |
| ---------------------------------------------------------- |
| [AlertRulePercents](#alertRules_anyOf_i0_storage_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_storage_anyOf_i1)            |

##### <a name="alertRules_anyOf_i0_storage_anyOf_i0"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > storage > anyOf > AlertRulePercents`

**Title:** AlertRulePercents

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Same definition as**    | [AlertRulePercents](#alertRules_anyOf_i0_ram_anyOf_i0)                      |

**Description:** Schema alert triggering procedure in percents.

##### <a name="alertRules_anyOf_i0_storage_anyOf_i1"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > storage > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="alertRules_anyOf_i0_upload"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Upload alert settings.

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [AlertRulePoints](#alertRules_anyOf_i0_upload_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_upload_anyOf_i1)          |

##### <a name="alertRules_anyOf_i0_upload_anyOf_i0"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints`

**Title:** AlertRulePoints

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AlertRulePoints                                                     |

**Description:** Schema alert triggering procedure.

| Property                                                             | Pattern | Type        | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [minTimeout](#alertRules_anyOf_i0_upload_anyOf_i0_minTimeout )     | No      | Combination | No         | -          | Mintimeout        |
| + [minThreshold](#alertRules_anyOf_i0_upload_anyOf_i0_minThreshold ) | No      | Combination | No         | -          | Minthreshold      |
| + [maxThreshold](#alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold ) | No      | Combination | No         | -          | Maxthreshold      |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_minTimeout"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > minTimeout`

**Title:** Mintimeout

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** The duration in ISO8601 for a time window to check alert rule.

**Examples:**

```json
"PT10S"
```

```json
"PT1M"
```

| Any of(Option)                                                     |
| ------------------------------------------------------------------ |
| [item 0](#alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i1) |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i0"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > minTimeout > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i1"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > minTimeout > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_minThreshold"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > minThreshold`

**Title:** Minthreshold

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** The minimum threshold to stop alert.

| Any of(Option)                                                       |
| -------------------------------------------------------------------- |
| [item 0](#alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i1) |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i0"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > minThreshold > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i1"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > minThreshold > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > maxThreshold`

**Title:** Maxthreshold

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** The maximum threshold value to start alert.

| Any of(Option)                                                       |
| -------------------------------------------------------------------- |
| [item 0](#alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i1) |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i0"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > maxThreshold > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i1"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > AlertRulePoints > maxThreshold > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="alertRules_anyOf_i0_upload_anyOf_i1"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > upload > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="alertRules_anyOf_i0_download"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > download`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Download alert settings.

| Any of(Option)                                            |
| --------------------------------------------------------- |
| [AlertRulePoints](#alertRules_anyOf_i0_download_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_download_anyOf_i1)          |

##### <a name="alertRules_anyOf_i0_download_anyOf_i0"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > download > anyOf > AlertRulePoints`

**Title:** AlertRulePoints

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Same definition as**    | [AlertRulePoints](#alertRules_anyOf_i0_upload_anyOf_i0)                     |

**Description:** Schema alert triggering procedure.

##### <a name="alertRules_anyOf_i0_download_anyOf_i1"></a>Property `AosConfigSchema > alertRules > anyOf > AlertRules > download > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="alertRules_anyOf_i1"></a>Property `AosConfigSchema > alertRules > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="permissions"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > permissions`

**Title:** Permissions

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Service permissions to access resources.

**Example:**

```json
{
    "vis": {
        "Attributes.Vehicle.Vin": "r",
        "Signal.Doors.*": "rw"
    }
}
```

| Any of(Option)                  |
| ------------------------------- |
| [item 0](#permissions_anyOf_i0) |
| [item 1](#permissions_anyOf_i1) |

### <a name="permissions_anyOf_i0"></a>Property `AosConfigSchema > permissions > anyOf > item 0`

|                           |                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                          |
| **Additional properties** | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#permissions_anyOf_i0_additionalProperties) |

| Property                                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [](#permissions_anyOf_i0_additionalProperties ) | No      | object | No         | -          | -                 |

#### <a name="permissions_anyOf_i0_additionalProperties"></a>Property `AosConfigSchema > permissions > anyOf > item 0 > additionalProperties`

|                           |                                                                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                               |
| **Additional properties** | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#permissions_anyOf_i0_additionalProperties_additionalProperties) |

| Property                                                               | Pattern | Type             | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| - [](#permissions_anyOf_i0_additionalProperties_additionalProperties ) | No      | enum (of string) | No         | -          | -                 |

##### <a name="permissions_anyOf_i0_additionalProperties_additionalProperties"></a>Property `AosConfigSchema > permissions > anyOf > item 0 > additionalProperties > additionalProperties`

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

Must be one of:
* "r"
* "rw"
* "w"

### <a name="permissions_anyOf_i1"></a>Property `AosConfigSchema > permissions > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="sysctl"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > sysctl`

**Title:** Sysctl

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Kernel parameters to be modified at runtime for the container.

**Example:**

```json
{
    "net.core.somaxconn": "256",
    "net.ipv4.ip_forward": "1"
}
```

| Any of(Option)             |
| -------------------------- |
| [item 0](#sysctl_anyOf_i0) |
| [item 1](#sysctl_anyOf_i1) |

### <a name="sysctl_anyOf_i0"></a>Property `AosConfigSchema > sysctl > anyOf > item 0`

|                           |                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                     |
| **Additional properties** | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#sysctl_anyOf_i0_additionalProperties) |

| Property                                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [](#sysctl_anyOf_i0_additionalProperties ) | No      | string | No         | -          | -                 |

#### <a name="sysctl_anyOf_i0_additionalProperties"></a>Property `AosConfigSchema > sysctl > anyOf > item 0 > additionalProperties`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="sysctl_anyOf_i1"></a>Property `AosConfigSchema > sysctl > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="dependencies"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchema > dependencies`

**Title:** Dependencies

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** List of dependencies.

| Any of(Option)                   |
| -------------------------------- |
| [item 0](#dependencies_anyOf_i0) |
| [item 1](#dependencies_anyOf_i1) |

### <a name="dependencies_anyOf_i0"></a>Property `AosConfigSchema > dependencies > anyOf > item 0`

|          |         |
| -------- | ------- |
| **Type** | `array` |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be               | Description |
| --------------------------------------------- | ----------- |
| [AosDependency](#dependencies_anyOf_i0_items) | -           |

#### <a name="dependencies_anyOf_i0_items"></a>AosConfigSchema > dependencies > anyOf > item 0 > AosDependency

**Title:** AosDependency

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosDependency                                                       |

| Property                                                 | Pattern | Type             | Deprecated | Definition             | Title/Description |
| -------------------------------------------------------- | ------- | ---------------- | ---------- | ---------------------- | ----------------- |
| + [identifier](#dependencies_anyOf_i0_items_identifier ) | No      | object           | No         | In #/$defs/AosIdentity | AosIdentity       |
| + [condition](#dependencies_anyOf_i0_items_condition )   | No      | enum (of string) | No         | -                      | Condition         |

##### <a name="dependencies_anyOf_i0_items_identifier"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier`

**Title:** AosIdentity

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosIdentity                                                         |

**Description:** Identifier of the AOS object.

| Property                                                              | Pattern | Type        | Deprecated | Definition | Title/Description                                    |
| --------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ---------------------------------------------------- |
| - [id](#dependencies_anyOf_i0_items_identifier_id )                   | No      | Combination | No         | -          | Aos object UUID identifier. Unique per Aos instance. |
| - [type](#dependencies_anyOf_i0_items_identifier_type )               | No      | Combination | No         | -          | Aos object type.                                     |
| - [codename](#dependencies_anyOf_i0_items_identifier_codename )       | No      | Combination | No         | -          | Aos object codename.                                 |
| - [title](#dependencies_anyOf_i0_items_identifier_title )             | No      | Combination | No         | -          | Aos object title.                                    |
| - [description](#dependencies_anyOf_i0_items_identifier_description ) | No      | Combination | No         | -          | Aos object description.                              |
| - [urn](#dependencies_anyOf_i0_items_identifier_urn )                 | No      | Combination | No         | -          | Aos object URN.                                      |

###### <a name="dependencies_anyOf_i0_items_identifier_id"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > id`

**Title:** Aos object UUID identifier. Unique per Aos instance.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object unique per Aos instance UUID.

| Any of(Option)                                                |
| ------------------------------------------------------------- |
| [item 0](#dependencies_anyOf_i0_items_identifier_id_anyOf_i0) |
| [item 1](#dependencies_anyOf_i0_items_identifier_id_anyOf_i1) |

###### <a name="dependencies_anyOf_i0_items_identifier_id_anyOf_i0"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > id > anyOf > item 0`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `uuid`   |

###### <a name="dependencies_anyOf_i0_items_identifier_id_anyOf_i1"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > id > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="dependencies_anyOf_i0_items_identifier_type"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > type`

**Title:** Aos object type.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object type. E.g.: AosService, AosComponent

| Any of(Option)                                                           |
| ------------------------------------------------------------------------ |
| [AosIdentityType](#dependencies_anyOf_i0_items_identifier_type_anyOf_i0) |
| [item 1](#dependencies_anyOf_i0_items_identifier_type_anyOf_i1)          |

###### <a name="dependencies_anyOf_i0_items_identifier_type_anyOf_i0"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > type > anyOf > AosIdentityType`

**Title:** AosIdentityType

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `enum (of string)`      |
| **Defined in** | #/$defs/AosIdentityType |

Must be one of:
* "component"
* "service"
* "layer"
* "subject"
* "oem"
* "sp"
* "fleet"
* "node"
* "node-subject"
* "runtime"

###### <a name="dependencies_anyOf_i0_items_identifier_type_anyOf_i1"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > type > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="dependencies_anyOf_i0_items_identifier_codename"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > codename`

**Title:** Aos object codename.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object codename. Uniqueness depends on object type.

| Any of(Option)                                                      |
| ------------------------------------------------------------------- |
| [item 0](#dependencies_anyOf_i0_items_identifier_codename_anyOf_i0) |
| [item 1](#dependencies_anyOf_i0_items_identifier_codename_anyOf_i1) |

###### <a name="dependencies_anyOf_i0_items_identifier_codename_anyOf_i0"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > codename > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="dependencies_anyOf_i0_items_identifier_codename_anyOf_i1"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > codename > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="dependencies_anyOf_i0_items_identifier_title"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > title`

**Title:** Aos object title.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object title.

| Any of(Option)                                                   |
| ---------------------------------------------------------------- |
| [item 0](#dependencies_anyOf_i0_items_identifier_title_anyOf_i0) |
| [item 1](#dependencies_anyOf_i0_items_identifier_title_anyOf_i1) |

###### <a name="dependencies_anyOf_i0_items_identifier_title_anyOf_i0"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > title > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="dependencies_anyOf_i0_items_identifier_title_anyOf_i1"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > title > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="dependencies_anyOf_i0_items_identifier_description"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > description`

**Title:** Aos object description.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object description.

| Any of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [item 0](#dependencies_anyOf_i0_items_identifier_description_anyOf_i0) |
| [item 1](#dependencies_anyOf_i0_items_identifier_description_anyOf_i1) |

###### <a name="dependencies_anyOf_i0_items_identifier_description_anyOf_i0"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > description > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="dependencies_anyOf_i0_items_identifier_description_anyOf_i1"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > description > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="dependencies_anyOf_i0_items_identifier_urn"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > urn`

**Title:** Aos object URN.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object URN. Globally unique.

| Any of(Option)                                                 |
| -------------------------------------------------------------- |
| [item 0](#dependencies_anyOf_i0_items_identifier_urn_anyOf_i0) |
| [item 1](#dependencies_anyOf_i0_items_identifier_urn_anyOf_i1) |

###### <a name="dependencies_anyOf_i0_items_identifier_urn_anyOf_i0"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > urn > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="dependencies_anyOf_i0_items_identifier_urn_anyOf_i1"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > identifier > urn > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="dependencies_anyOf_i0_items_condition"></a>Property `AosConfigSchema > dependencies > anyOf > item 0 > AosDependency > condition`

**Title:** Condition

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

**Description:** Condition for dependency of the AOS object.

Must be one of:
* "started"
* "healthy"
* "completed"
* "before"
* "after"

### <a name="dependencies_anyOf_i1"></a>Property `AosConfigSchema > dependencies > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2026-06-05 at 13:49:28 +0300
