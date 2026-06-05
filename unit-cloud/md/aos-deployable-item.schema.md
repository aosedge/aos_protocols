# AosConfigSchemaV2

- [![Required](https://img.shields.io/badge/Required-blue) Property `AosConfigSchemaV2 > created`](#created)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > author`](#author)
  - [Property `AosConfigSchemaV2 > author > anyOf > item 0`](#author_anyOf_i0)
  - [Property `AosConfigSchemaV2 > author > anyOf > item 1`](#author_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > skipResourceLimits`](#skipResourceLimits)
  - [Property `AosConfigSchemaV2 > skipResourceLimits > anyOf > item 0`](#skipResourceLimits_anyOf_i0)
  - [Property `AosConfigSchemaV2 > skipResourceLimits > anyOf > item 1`](#skipResourceLimits_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > balancingPolicy`](#balancingPolicy)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > hostname`](#hostname)
  - [Property `AosConfigSchemaV2 > hostname > anyOf > item 0`](#hostname_anyOf_i0)
  - [Property `AosConfigSchemaV2 > hostname > anyOf > item 1`](#hostname_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > runtimes`](#runtimes)
  - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0`](#runtimes_anyOf_i0)
    - [AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity](#runtimes_anyOf_i0_items)
      - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > id`](#runtimes_anyOf_i0_items_id)
        - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > id > anyOf > item 0`](#runtimes_anyOf_i0_items_id_anyOf_i0)
        - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > id > anyOf > item 1`](#runtimes_anyOf_i0_items_id_anyOf_i1)
      - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > type`](#runtimes_anyOf_i0_items_type)
        - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > type > anyOf > AosIdentityType`](#runtimes_anyOf_i0_items_type_anyOf_i0)
        - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > type > anyOf > item 1`](#runtimes_anyOf_i0_items_type_anyOf_i1)
      - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > codename`](#runtimes_anyOf_i0_items_codename)
        - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > codename > anyOf > item 0`](#runtimes_anyOf_i0_items_codename_anyOf_i0)
        - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > codename > anyOf > item 1`](#runtimes_anyOf_i0_items_codename_anyOf_i1)
      - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > title`](#runtimes_anyOf_i0_items_title)
        - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > title > anyOf > item 0`](#runtimes_anyOf_i0_items_title_anyOf_i0)
        - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > title > anyOf > item 1`](#runtimes_anyOf_i0_items_title_anyOf_i1)
      - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > description`](#runtimes_anyOf_i0_items_description)
        - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > description > anyOf > item 0`](#runtimes_anyOf_i0_items_description_anyOf_i0)
        - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > description > anyOf > item 1`](#runtimes_anyOf_i0_items_description_anyOf_i1)
      - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > urn`](#runtimes_anyOf_i0_items_urn)
        - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > urn > anyOf > item 0`](#runtimes_anyOf_i0_items_urn_anyOf_i0)
        - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > urn > anyOf > item 1`](#runtimes_anyOf_i0_items_urn_anyOf_i1)
  - [Property `AosConfigSchemaV2 > runtimes > anyOf > item 1`](#runtimes_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > runParameters`](#runParameters)
  - [Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters`](#runParameters_anyOf_i0)
    - [Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > startInterval`](#runParameters_anyOf_i0_startInterval)
      - [Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > startInterval > anyOf > item 0`](#runParameters_anyOf_i0_startInterval_anyOf_i0)
      - [Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > startInterval > anyOf > item 1`](#runParameters_anyOf_i0_startInterval_anyOf_i1)
    - [Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > startBurst`](#runParameters_anyOf_i0_startBurst)
      - [Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > startBurst > anyOf > item 0`](#runParameters_anyOf_i0_startBurst_anyOf_i0)
      - [Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > startBurst > anyOf > item 1`](#runParameters_anyOf_i0_startBurst_anyOf_i1)
    - [Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > restartInterval`](#runParameters_anyOf_i0_restartInterval)
      - [Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > restartInterval > anyOf > item 0`](#runParameters_anyOf_i0_restartInterval_anyOf_i0)
      - [Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > restartInterval > anyOf > item 1`](#runParameters_anyOf_i0_restartInterval_anyOf_i1)
  - [Property `AosConfigSchemaV2 > runParameters > anyOf > item 1`](#runParameters_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > offlineTTL`](#offlineTTL)
  - [Property `AosConfigSchemaV2 > offlineTTL > anyOf > item 0`](#offlineTTL_anyOf_i0)
  - [Property `AosConfigSchemaV2 > offlineTTL > anyOf > item 1`](#offlineTTL_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > resources`](#resources)
  - [Property `AosConfigSchemaV2 > resources > anyOf > item 0`](#resources_anyOf_i0)
    - [AosConfigSchemaV2 > resources > anyOf > item 0 > AosResourceAccess](#resources_anyOf_i0_items)
      - [Property `AosConfigSchemaV2 > resources > anyOf > item 0 > AosResourceAccess > name`](#resources_anyOf_i0_items_name)
      - [Property `AosConfigSchemaV2 > resources > anyOf > item 0 > AosResourceAccess > mode`](#resources_anyOf_i0_items_mode)
  - [Property `AosConfigSchemaV2 > resources > anyOf > item 1`](#resources_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > allowedConnections`](#allowedConnections)
  - [Property `AosConfigSchemaV2 > allowedConnections > anyOf > item 0`](#allowedConnections_anyOf_i0)
  - [Property `AosConfigSchemaV2 > allowedConnections > anyOf > item 1`](#allowedConnections_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > quotas`](#quotas)
  - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas`](#quotas_anyOf_i0)
    - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > cpuLimit`](#quotas_anyOf_i0_cpuLimit)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > cpuLimit > anyOf > item 0`](#quotas_anyOf_i0_cpuLimit_anyOf_i0)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > cpuLimit > anyOf > item 1`](#quotas_anyOf_i0_cpuLimit_anyOf_i1)
    - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > cpuDmipsLimit`](#quotas_anyOf_i0_cpuDmipsLimit)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > cpuDmipsLimit > anyOf > item 0`](#quotas_anyOf_i0_cpuDmipsLimit_anyOf_i0)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > cpuDmipsLimit > anyOf > item 1`](#quotas_anyOf_i0_cpuDmipsLimit_anyOf_i1)
    - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > ramLimit`](#quotas_anyOf_i0_ramLimit)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > ramLimit > anyOf > item 0`](#quotas_anyOf_i0_ramLimit_anyOf_i0)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > ramLimit > anyOf > item 1`](#quotas_anyOf_i0_ramLimit_anyOf_i1)
    - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > storageLimit`](#quotas_anyOf_i0_storageLimit)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > storageLimit > anyOf > item 0`](#quotas_anyOf_i0_storageLimit_anyOf_i0)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > storageLimit > anyOf > item 1`](#quotas_anyOf_i0_storageLimit_anyOf_i1)
    - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > stateLimit`](#quotas_anyOf_i0_stateLimit)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > stateLimit > anyOf > item 0`](#quotas_anyOf_i0_stateLimit_anyOf_i0)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > stateLimit > anyOf > item 1`](#quotas_anyOf_i0_stateLimit_anyOf_i1)
    - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > tmpLimit`](#quotas_anyOf_i0_tmpLimit)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > tmpLimit > anyOf > item 0`](#quotas_anyOf_i0_tmpLimit_anyOf_i0)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > tmpLimit > anyOf > item 1`](#quotas_anyOf_i0_tmpLimit_anyOf_i1)
    - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > uploadSpeed`](#quotas_anyOf_i0_uploadSpeed)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > uploadSpeed > anyOf > item 0`](#quotas_anyOf_i0_uploadSpeed_anyOf_i0)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > uploadSpeed > anyOf > item 1`](#quotas_anyOf_i0_uploadSpeed_anyOf_i1)
    - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > downloadSpeed`](#quotas_anyOf_i0_downloadSpeed)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > downloadSpeed > anyOf > item 0`](#quotas_anyOf_i0_downloadSpeed_anyOf_i0)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > downloadSpeed > anyOf > item 1`](#quotas_anyOf_i0_downloadSpeed_anyOf_i1)
    - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > noFileLimit`](#quotas_anyOf_i0_noFileLimit)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > noFileLimit > anyOf > item 0`](#quotas_anyOf_i0_noFileLimit_anyOf_i0)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > noFileLimit > anyOf > item 1`](#quotas_anyOf_i0_noFileLimit_anyOf_i1)
    - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > pidsLimit`](#quotas_anyOf_i0_pidsLimit)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > pidsLimit > anyOf > item 0`](#quotas_anyOf_i0_pidsLimit_anyOf_i0)
      - [Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > pidsLimit > anyOf > item 1`](#quotas_anyOf_i0_pidsLimit_anyOf_i1)
  - [Property `AosConfigSchemaV2 > quotas > anyOf > item 1`](#quotas_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > requestedResources`](#requestedResources)
  - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources`](#requestedResources_anyOf_i0)
    - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > cpu`](#requestedResources_anyOf_i0_cpu)
      - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > cpu > anyOf > item 0`](#requestedResources_anyOf_i0_cpu_anyOf_i0)
      - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > cpu > anyOf > item 1`](#requestedResources_anyOf_i0_cpu_anyOf_i1)
    - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > ram`](#requestedResources_anyOf_i0_ram)
      - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > ram > anyOf > item 0`](#requestedResources_anyOf_i0_ram_anyOf_i0)
      - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > ram > anyOf > item 1`](#requestedResources_anyOf_i0_ram_anyOf_i1)
    - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > storage`](#requestedResources_anyOf_i0_storage)
      - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > storage > anyOf > item 0`](#requestedResources_anyOf_i0_storage_anyOf_i0)
      - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > storage > anyOf > item 1`](#requestedResources_anyOf_i0_storage_anyOf_i1)
    - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > state`](#requestedResources_anyOf_i0_state)
      - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > state > anyOf > item 0`](#requestedResources_anyOf_i0_state_anyOf_i0)
      - [Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > state > anyOf > item 1`](#requestedResources_anyOf_i0_state_anyOf_i1)
  - [Property `AosConfigSchemaV2 > requestedResources > anyOf > item 1`](#requestedResources_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > alertRules`](#alertRules)
  - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules`](#alertRules_anyOf_i0)
    - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram`](#alertRules_anyOf_i0_ram)
      - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents`](#alertRules_anyOf_i0_ram_anyOf_i0)
        - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minTimeout`](#alertRules_anyOf_i0_ram_anyOf_i0_minTimeout)
          - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minTimeout > anyOf > item 0`](#alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i0)
          - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minTimeout > anyOf > item 1`](#alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i1)
        - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minThreshold`](#alertRules_anyOf_i0_ram_anyOf_i0_minThreshold)
          - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minThreshold > anyOf > item 0`](#alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i0)
          - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minThreshold > anyOf > item 1`](#alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i1)
        - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > maxThreshold`](#alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold)
          - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > maxThreshold > anyOf > item 0`](#alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i0)
          - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > maxThreshold > anyOf > item 1`](#alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i1)
      - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > item 1`](#alertRules_anyOf_i0_ram_anyOf_i1)
    - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > cpu`](#alertRules_anyOf_i0_cpu)
      - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > cpu > anyOf > AosAlertRulePercents`](#alertRules_anyOf_i0_cpu_anyOf_i0)
      - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > cpu > anyOf > item 1`](#alertRules_anyOf_i0_cpu_anyOf_i1)
    - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > storage`](#alertRules_anyOf_i0_storage)
      - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > storage > anyOf > AosAlertRulePercents`](#alertRules_anyOf_i0_storage_anyOf_i0)
      - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > storage > anyOf > item 1`](#alertRules_anyOf_i0_storage_anyOf_i1)
    - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload`](#alertRules_anyOf_i0_upload)
      - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints`](#alertRules_anyOf_i0_upload_anyOf_i0)
        - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minTimeout`](#alertRules_anyOf_i0_upload_anyOf_i0_minTimeout)
          - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minTimeout > anyOf > item 0`](#alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i0)
          - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minTimeout > anyOf > item 1`](#alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i1)
        - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minThreshold`](#alertRules_anyOf_i0_upload_anyOf_i0_minThreshold)
          - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minThreshold > anyOf > item 0`](#alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i0)
          - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minThreshold > anyOf > item 1`](#alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i1)
        - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > maxThreshold`](#alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold)
          - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > maxThreshold > anyOf > item 0`](#alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i0)
          - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > maxThreshold > anyOf > item 1`](#alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i1)
      - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > item 1`](#alertRules_anyOf_i0_upload_anyOf_i1)
    - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > download`](#alertRules_anyOf_i0_download)
      - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > download > anyOf > AosAlertRulePoints`](#alertRules_anyOf_i0_download_anyOf_i0)
      - [Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > download > anyOf > item 1`](#alertRules_anyOf_i0_download_anyOf_i1)
  - [Property `AosConfigSchemaV2 > alertRules > anyOf > item 1`](#alertRules_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > permissions`](#permissions)
  - [Property `AosConfigSchemaV2 > permissions > anyOf > item 0`](#permissions_anyOf_i0)
    - [Property `AosConfigSchemaV2 > permissions > anyOf > item 0 > additionalProperties`](#permissions_anyOf_i0_additionalProperties)
      - [Property `AosConfigSchemaV2 > permissions > anyOf > item 0 > additionalProperties > additionalProperties`](#permissions_anyOf_i0_additionalProperties_additionalProperties)
  - [Property `AosConfigSchemaV2 > permissions > anyOf > item 1`](#permissions_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > sysctl`](#sysctl)
  - [Property `AosConfigSchemaV2 > sysctl > anyOf > item 0`](#sysctl_anyOf_i0)
    - [Property `AosConfigSchemaV2 > sysctl > anyOf > item 0 > additionalProperties`](#sysctl_anyOf_i0_additionalProperties)
  - [Property `AosConfigSchemaV2 > sysctl > anyOf > item 1`](#sysctl_anyOf_i1)

**Title:** AosConfigSchemaV2

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** Aos deployable item config schema.

This schema describes the specification of the
 `application/vnd.aos.item.config.v1+json` layer in a deployable item.

| Property                                     | Pattern | Type             | Deprecated | Definition | Title/Description                           |
| -------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------------------------------- |
| + [created](#created )                       | No      | string           | No         | -          | Created                                     |
| - [author](#author )                         | No      | Combination      | No         | -          | Author                                      |
| - [skipResourceLimits](#skipResourceLimits ) | No      | Combination      | No         | -          | Skipresourcelimits                          |
| - [balancingPolicy](#balancingPolicy )       | No      | enum (of string) | No         | -          | Balancingpolicy                             |
| - [hostname](#hostname )                     | No      | Combination      | No         | -          | Hostname                                    |
| - [runtimes](#runtimes )                     | No      | Combination      | No         | -          | Runtimes                                    |
| - [runParameters](#runParameters )           | No      | Combination      | No         | -          | Run parameters for the Aos service.         |
| - [offlineTTL](#offlineTTL )                 | No      | Combination      | No         | -          | Offlinettl                                  |
| - [resources](#resources )                   | No      | Combination      | No         | -          | Resources                                   |
| - [allowedConnections](#allowedConnections ) | No      | Combination      | No         | -          | Allowedconnections                          |
| - [quotas](#quotas )                         | No      | Combination      | No         | -          | Quotas for the service.                     |
| - [requestedResources](#requestedResources ) | No      | Combination      | No         | -          | Requested Resources (CPU, RAM and Storage). |
| - [alertRules](#alertRules )                 | No      | Combination      | No         | -          | Alert rules for the service.                |
| - [permissions](#permissions )               | No      | Combination      | No         | -          | Permissions                                 |
| - [sysctl](#sysctl )                         | No      | Combination      | No         | -          | Sysctl                                      |

## <a name="created"></a>![Required](https://img.shields.io/badge/Required-blue) Property `AosConfigSchemaV2 > created`

**Title:** Created

|            |             |
| ---------- | ----------- |
| **Type**   | `string`    |
| **Format** | `date-time` |

**Description:** Timestamp when Aos service was created.

## <a name="author"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > author`

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

### <a name="author_anyOf_i0"></a>Property `AosConfigSchemaV2 > author > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="author_anyOf_i1"></a>Property `AosConfigSchemaV2 > author > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="skipResourceLimits"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > skipResourceLimits`

**Title:** Skipresourcelimits

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Use resource limits or not in Pre-release versions.

| Any of(Option)                         |
| -------------------------------------- |
| [item 0](#skipResourceLimits_anyOf_i0) |
| [item 1](#skipResourceLimits_anyOf_i1) |

### <a name="skipResourceLimits_anyOf_i0"></a>Property `AosConfigSchemaV2 > skipResourceLimits > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `boolean` |

### <a name="skipResourceLimits_anyOf_i1"></a>Property `AosConfigSchemaV2 > skipResourceLimits > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="balancingPolicy"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > balancingPolicy`

**Title:** Balancingpolicy

|             |                    |
| ----------- | ------------------ |
| **Type**    | `enum (of string)` |
| **Default** | `"enabled"`        |

**Description:** Balancing type. `disabled` means total prohibition from balancing to other nodes.

Must be one of:
* "enabled"
* "disabled"

## <a name="hostname"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > hostname`

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

### <a name="hostname_anyOf_i0"></a>Property `AosConfigSchemaV2 > hostname > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="hostname_anyOf_i1"></a>Property `AosConfigSchemaV2 > hostname > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="runtimes"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > runtimes`

**Title:** Runtimes

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos service allowed runtimes. Absense means all runtimes.

| Any of(Option)               |
| ---------------------------- |
| [item 0](#runtimes_anyOf_i0) |
| [item 1](#runtimes_anyOf_i1) |

### <a name="runtimes_anyOf_i0"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0`

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

| Each item of this array must be         | Description             |
| --------------------------------------- | ----------------------- |
| [AosIdentity](#runtimes_anyOf_i0_items) | Aos objects identifier. |

#### <a name="runtimes_anyOf_i0_items"></a>AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity

**Title:** AosIdentity

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosIdentity                                                         |

**Description:** Aos objects identifier.

| Property                                               | Pattern | Type        | Deprecated | Definition | Title/Description                                    |
| ------------------------------------------------------ | ------- | ----------- | ---------- | ---------- | ---------------------------------------------------- |
| - [id](#runtimes_anyOf_i0_items_id )                   | No      | Combination | No         | -          | Aos object UUID identifier. Unique per Aos instance. |
| - [type](#runtimes_anyOf_i0_items_type )               | No      | Combination | No         | -          | Aos object type.                                     |
| - [codename](#runtimes_anyOf_i0_items_codename )       | No      | Combination | No         | -          | Aos object codename.                                 |
| - [title](#runtimes_anyOf_i0_items_title )             | No      | Combination | No         | -          | Aos object title.                                    |
| - [description](#runtimes_anyOf_i0_items_description ) | No      | Combination | No         | -          | Aos object description.                              |
| - [urn](#runtimes_anyOf_i0_items_urn )                 | No      | Combination | No         | -          | Aos object URN.                                      |

##### <a name="runtimes_anyOf_i0_items_id"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > id`

**Title:** Aos object UUID identifier. Unique per Aos instance.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object unique per Aos instance UUID.

| Any of(Option)                                 |
| ---------------------------------------------- |
| [item 0](#runtimes_anyOf_i0_items_id_anyOf_i0) |
| [item 1](#runtimes_anyOf_i0_items_id_anyOf_i1) |

###### <a name="runtimes_anyOf_i0_items_id_anyOf_i0"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > id > anyOf > item 0`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `uuid`   |

###### <a name="runtimes_anyOf_i0_items_id_anyOf_i1"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > id > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="runtimes_anyOf_i0_items_type"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > type`

**Title:** Aos object type.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object type. E.g.: AosService, AosComponent

| Any of(Option)                                            |
| --------------------------------------------------------- |
| [AosIdentityType](#runtimes_anyOf_i0_items_type_anyOf_i0) |
| [item 1](#runtimes_anyOf_i0_items_type_anyOf_i1)          |

###### <a name="runtimes_anyOf_i0_items_type_anyOf_i0"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > type > anyOf > AosIdentityType`

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

###### <a name="runtimes_anyOf_i0_items_type_anyOf_i1"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > type > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="runtimes_anyOf_i0_items_codename"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > codename`

**Title:** Aos object codename.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object codename. Uniqueness depends on object type.

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [item 0](#runtimes_anyOf_i0_items_codename_anyOf_i0) |
| [item 1](#runtimes_anyOf_i0_items_codename_anyOf_i1) |

###### <a name="runtimes_anyOf_i0_items_codename_anyOf_i0"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > codename > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="runtimes_anyOf_i0_items_codename_anyOf_i1"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > codename > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="runtimes_anyOf_i0_items_title"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > title`

**Title:** Aos object title.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object title.

| Any of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#runtimes_anyOf_i0_items_title_anyOf_i0) |
| [item 1](#runtimes_anyOf_i0_items_title_anyOf_i1) |

###### <a name="runtimes_anyOf_i0_items_title_anyOf_i0"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > title > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="runtimes_anyOf_i0_items_title_anyOf_i1"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > title > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="runtimes_anyOf_i0_items_description"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > description`

**Title:** Aos object description.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object description.

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#runtimes_anyOf_i0_items_description_anyOf_i0) |
| [item 1](#runtimes_anyOf_i0_items_description_anyOf_i1) |

###### <a name="runtimes_anyOf_i0_items_description_anyOf_i0"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > description > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="runtimes_anyOf_i0_items_description_anyOf_i1"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > description > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="runtimes_anyOf_i0_items_urn"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > urn`

**Title:** Aos object URN.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object URN. Globally unique.

| Any of(Option)                                  |
| ----------------------------------------------- |
| [item 0](#runtimes_anyOf_i0_items_urn_anyOf_i0) |
| [item 1](#runtimes_anyOf_i0_items_urn_anyOf_i1) |

###### <a name="runtimes_anyOf_i0_items_urn_anyOf_i0"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > urn > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="runtimes_anyOf_i0_items_urn_anyOf_i1"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 0 > AosIdentity > urn > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="runtimes_anyOf_i1"></a>Property `AosConfigSchemaV2 > runtimes > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="runParameters"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > runParameters`

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

### <a name="runParameters_anyOf_i0"></a>Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters`

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

#### <a name="runParameters_anyOf_i0_startInterval"></a>Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > startInterval`

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

##### <a name="runParameters_anyOf_i0_startInterval_anyOf_i0"></a>Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > startInterval > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

##### <a name="runParameters_anyOf_i0_startInterval_anyOf_i1"></a>Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > startInterval > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="runParameters_anyOf_i0_startBurst"></a>Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > startBurst`

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

##### <a name="runParameters_anyOf_i0_startBurst_anyOf_i0"></a>Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > startBurst > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="runParameters_anyOf_i0_startBurst_anyOf_i1"></a>Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > startBurst > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="runParameters_anyOf_i0_restartInterval"></a>Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > restartInterval`

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

##### <a name="runParameters_anyOf_i0_restartInterval_anyOf_i0"></a>Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > restartInterval > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

##### <a name="runParameters_anyOf_i0_restartInterval_anyOf_i1"></a>Property `AosConfigSchemaV2 > runParameters > anyOf > RunParameters > restartInterval > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="runParameters_anyOf_i1"></a>Property `AosConfigSchemaV2 > runParameters > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="offlineTTL"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > offlineTTL`

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

### <a name="offlineTTL_anyOf_i0"></a>Property `AosConfigSchemaV2 > offlineTTL > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

### <a name="offlineTTL_anyOf_i1"></a>Property `AosConfigSchemaV2 > offlineTTL > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="resources"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > resources`

**Title:** Resources

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** List of needed resources.

**Examples:**

```json
{
    "mode": "rw",
    "name": "bluetooth"
}
```

```json
{
    "mode": "rw",
    "name": "system-dbus"
}
```

```json
{
    "mode": "r",
    "name": "camera0"
}
```

| Any of(Option)                |
| ----------------------------- |
| [item 0](#resources_anyOf_i0) |
| [item 1](#resources_anyOf_i1) |

### <a name="resources_anyOf_i0"></a>Property `AosConfigSchemaV2 > resources > anyOf > item 0`

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

| Each item of this array must be                | Description |
| ---------------------------------------------- | ----------- |
| [AosResourceAccess](#resources_anyOf_i0_items) | -           |

#### <a name="resources_anyOf_i0_items"></a>AosConfigSchemaV2 > resources > anyOf > item 0 > AosResourceAccess

**Title:** AosResourceAccess

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosResourceAccess                                                   |

| Property                                  | Pattern | Type             | Deprecated | Definition | Title/Description |
| ----------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [name](#resources_anyOf_i0_items_name ) | No      | string           | No         | -          | Name              |
| - [mode](#resources_anyOf_i0_items_mode ) | No      | enum (of string) | No         | -          | Mode              |

##### <a name="resources_anyOf_i0_items_name"></a>Property `AosConfigSchemaV2 > resources > anyOf > item 0 > AosResourceAccess > name`

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

##### <a name="resources_anyOf_i0_items_mode"></a>Property `AosConfigSchemaV2 > resources > anyOf > item 0 > AosResourceAccess > mode`

**Title:** Mode

|             |                    |
| ----------- | ------------------ |
| **Type**    | `enum (of string)` |
| **Default** | `"r"`              |

**Description:** The needed access permissions for the resource.

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

Must be one of:
* "w"
* "rw"
* "m"
* "rwm"

### <a name="resources_anyOf_i1"></a>Property `AosConfigSchemaV2 > resources > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="allowedConnections"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > allowedConnections`

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

### <a name="allowedConnections_anyOf_i0"></a>Property `AosConfigSchemaV2 > allowedConnections > anyOf > item 0`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

### <a name="allowedConnections_anyOf_i1"></a>Property `AosConfigSchemaV2 > allowedConnections > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="quotas"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > quotas`

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

### <a name="quotas_anyOf_i0"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas`

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

#### <a name="quotas_anyOf_i0_cpuLimit"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > cpuLimit`

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

##### <a name="quotas_anyOf_i0_cpuLimit_anyOf_i0"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > cpuLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_cpuLimit_anyOf_i1"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > cpuLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_cpuDmipsLimit"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > cpuDmipsLimit`

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

##### <a name="quotas_anyOf_i0_cpuDmipsLimit_anyOf_i0"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > cpuDmipsLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_cpuDmipsLimit_anyOf_i1"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > cpuDmipsLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_ramLimit"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > ramLimit`

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

##### <a name="quotas_anyOf_i0_ramLimit_anyOf_i0"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > ramLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_ramLimit_anyOf_i1"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > ramLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_storageLimit"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > storageLimit`

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

##### <a name="quotas_anyOf_i0_storageLimit_anyOf_i0"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > storageLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_storageLimit_anyOf_i1"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > storageLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_stateLimit"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > stateLimit`

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

##### <a name="quotas_anyOf_i0_stateLimit_anyOf_i0"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > stateLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_stateLimit_anyOf_i1"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > stateLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_tmpLimit"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > tmpLimit`

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

##### <a name="quotas_anyOf_i0_tmpLimit_anyOf_i0"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > tmpLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_tmpLimit_anyOf_i1"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > tmpLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_uploadSpeed"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > uploadSpeed`

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

##### <a name="quotas_anyOf_i0_uploadSpeed_anyOf_i0"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > uploadSpeed > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_uploadSpeed_anyOf_i1"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > uploadSpeed > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_downloadSpeed"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > downloadSpeed`

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

##### <a name="quotas_anyOf_i0_downloadSpeed_anyOf_i0"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > downloadSpeed > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_downloadSpeed_anyOf_i1"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > downloadSpeed > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_noFileLimit"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > noFileLimit`

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

##### <a name="quotas_anyOf_i0_noFileLimit_anyOf_i0"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > noFileLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_noFileLimit_anyOf_i1"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > noFileLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="quotas_anyOf_i0_pidsLimit"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > pidsLimit`

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

##### <a name="quotas_anyOf_i0_pidsLimit_anyOf_i0"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > pidsLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="quotas_anyOf_i0_pidsLimit_anyOf_i1"></a>Property `AosConfigSchemaV2 > quotas > anyOf > ServiceQuotas > pidsLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="quotas_anyOf_i1"></a>Property `AosConfigSchemaV2 > quotas > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="requestedResources"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > requestedResources`

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

### <a name="requestedResources_anyOf_i0"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources`

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

#### <a name="requestedResources_anyOf_i0_cpu"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > cpu`

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

##### <a name="requestedResources_anyOf_i0_cpu_anyOf_i0"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > cpu > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="requestedResources_anyOf_i0_cpu_anyOf_i1"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > cpu > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="requestedResources_anyOf_i0_ram"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > ram`

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

##### <a name="requestedResources_anyOf_i0_ram_anyOf_i0"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > ram > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="requestedResources_anyOf_i0_ram_anyOf_i1"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > ram > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="requestedResources_anyOf_i0_storage"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > storage`

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

##### <a name="requestedResources_anyOf_i0_storage_anyOf_i0"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > storage > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="requestedResources_anyOf_i0_storage_anyOf_i1"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > storage > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="requestedResources_anyOf_i0_state"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > state`

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

##### <a name="requestedResources_anyOf_i0_state_anyOf_i0"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > state > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

##### <a name="requestedResources_anyOf_i0_state_anyOf_i1"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > RequestedResources > state > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="requestedResources_anyOf_i1"></a>Property `AosConfigSchemaV2 > requestedResources > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="alertRules"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > alertRules`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Alert rules for the service.

| Any of(Option)                        |
| ------------------------------------- |
| [AosAlertRules](#alertRules_anyOf_i0) |
| [item 1](#alertRules_anyOf_i1)        |

### <a name="alertRules_anyOf_i0"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules`

**Title:** AosAlertRules

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertRules                                                       |

**Description:** Schema for all possible alert rules.

| Property                                     | Pattern | Type        | Deprecated | Definition | Title/Description        |
| -------------------------------------------- | ------- | ----------- | ---------- | ---------- | ------------------------ |
| - [ram](#alertRules_anyOf_i0_ram )           | No      | Combination | No         | -          | RAM alert settings.      |
| - [cpu](#alertRules_anyOf_i0_cpu )           | No      | Combination | No         | -          | CPU alert settings.      |
| - [storage](#alertRules_anyOf_i0_storage )   | No      | Combination | No         | -          | Storage alert settings.  |
| - [upload](#alertRules_anyOf_i0_upload )     | No      | Combination | No         | -          | Upload alert settings.   |
| - [download](#alertRules_anyOf_i0_download ) | No      | Combination | No         | -          | Download alert settings. |

#### <a name="alertRules_anyOf_i0_ram"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** RAM alert settings.

| Any of(Option)                                            |
| --------------------------------------------------------- |
| [AosAlertRulePercents](#alertRules_anyOf_i0_ram_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_ram_anyOf_i1)               |

##### <a name="alertRules_anyOf_i0_ram_anyOf_i0"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents`

**Title:** AosAlertRulePercents

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertRulePercents                                                |

**Description:** Schema alert triggering procedure in percents.

| Property                                                          | Pattern | Type        | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [minTimeout](#alertRules_anyOf_i0_ram_anyOf_i0_minTimeout )     | No      | Combination | No         | -          | Mintimeout        |
| + [minThreshold](#alertRules_anyOf_i0_ram_anyOf_i0_minThreshold ) | No      | Combination | No         | -          | Minthreshold      |
| + [maxThreshold](#alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold ) | No      | Combination | No         | -          | Maxthreshold      |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_minTimeout"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minTimeout`

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

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i0"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minTimeout > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i1"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minTimeout > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_minThreshold"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minThreshold`

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

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i0"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minThreshold > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `number` |

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i1"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minThreshold > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > maxThreshold`

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

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i0"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > maxThreshold > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `number` |

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i1"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > maxThreshold > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="alertRules_anyOf_i0_ram_anyOf_i1"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > ram > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="alertRules_anyOf_i0_cpu"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > cpu`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** CPU alert settings.

| Any of(Option)                                            |
| --------------------------------------------------------- |
| [AosAlertRulePercents](#alertRules_anyOf_i0_cpu_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_cpu_anyOf_i1)               |

##### <a name="alertRules_anyOf_i0_cpu_anyOf_i0"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > cpu > anyOf > AosAlertRulePercents`

**Title:** AosAlertRulePercents

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Same definition as**    | [AosAlertRulePercents](#alertRules_anyOf_i0_ram_anyOf_i0)                   |

**Description:** Schema alert triggering procedure in percents.

##### <a name="alertRules_anyOf_i0_cpu_anyOf_i1"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > cpu > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="alertRules_anyOf_i0_storage"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > storage`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Storage alert settings.

| Any of(Option)                                                |
| ------------------------------------------------------------- |
| [AosAlertRulePercents](#alertRules_anyOf_i0_storage_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_storage_anyOf_i1)               |

##### <a name="alertRules_anyOf_i0_storage_anyOf_i0"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > storage > anyOf > AosAlertRulePercents`

**Title:** AosAlertRulePercents

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Same definition as**    | [AosAlertRulePercents](#alertRules_anyOf_i0_ram_anyOf_i0)                   |

**Description:** Schema alert triggering procedure in percents.

##### <a name="alertRules_anyOf_i0_storage_anyOf_i1"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > storage > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="alertRules_anyOf_i0_upload"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Upload alert settings.

| Any of(Option)                                             |
| ---------------------------------------------------------- |
| [AosAlertRulePoints](#alertRules_anyOf_i0_upload_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_upload_anyOf_i1)             |

##### <a name="alertRules_anyOf_i0_upload_anyOf_i0"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints`

**Title:** AosAlertRulePoints

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertRulePoints                                                  |

**Description:** Schema alert triggering procedure.

| Property                                                             | Pattern | Type        | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [minTimeout](#alertRules_anyOf_i0_upload_anyOf_i0_minTimeout )     | No      | Combination | No         | -          | Mintimeout        |
| + [minThreshold](#alertRules_anyOf_i0_upload_anyOf_i0_minThreshold ) | No      | Combination | No         | -          | Minthreshold      |
| + [maxThreshold](#alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold ) | No      | Combination | No         | -          | Maxthreshold      |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_minTimeout"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minTimeout`

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

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i0"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minTimeout > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i1"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minTimeout > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_minThreshold"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minThreshold`

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

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i0"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minThreshold > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i1"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minThreshold > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > maxThreshold`

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

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i0"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > maxThreshold > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i1"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > maxThreshold > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="alertRules_anyOf_i0_upload_anyOf_i1"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > upload > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="alertRules_anyOf_i0_download"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > download`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Download alert settings.

| Any of(Option)                                               |
| ------------------------------------------------------------ |
| [AosAlertRulePoints](#alertRules_anyOf_i0_download_anyOf_i0) |
| [item 1](#alertRules_anyOf_i0_download_anyOf_i1)             |

##### <a name="alertRules_anyOf_i0_download_anyOf_i0"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > download > anyOf > AosAlertRulePoints`

**Title:** AosAlertRulePoints

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Same definition as**    | [AosAlertRulePoints](#alertRules_anyOf_i0_upload_anyOf_i0)                  |

**Description:** Schema alert triggering procedure.

##### <a name="alertRules_anyOf_i0_download_anyOf_i1"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > AosAlertRules > download > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="alertRules_anyOf_i1"></a>Property `AosConfigSchemaV2 > alertRules > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="permissions"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > permissions`

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

### <a name="permissions_anyOf_i0"></a>Property `AosConfigSchemaV2 > permissions > anyOf > item 0`

|                           |                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                          |
| **Additional properties** | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#permissions_anyOf_i0_additionalProperties) |

| Property                                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [](#permissions_anyOf_i0_additionalProperties ) | No      | object | No         | -          | -                 |

#### <a name="permissions_anyOf_i0_additionalProperties"></a>Property `AosConfigSchemaV2 > permissions > anyOf > item 0 > additionalProperties`

|                           |                                                                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                               |
| **Additional properties** | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#permissions_anyOf_i0_additionalProperties_additionalProperties) |

| Property                                                               | Pattern | Type             | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| - [](#permissions_anyOf_i0_additionalProperties_additionalProperties ) | No      | enum (of string) | No         | -          | -                 |

##### <a name="permissions_anyOf_i0_additionalProperties_additionalProperties"></a>Property `AosConfigSchemaV2 > permissions > anyOf > item 0 > additionalProperties > additionalProperties`

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

Must be one of:
* "r"
* "rw"
* "w"

### <a name="permissions_anyOf_i1"></a>Property `AosConfigSchemaV2 > permissions > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="sysctl"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosConfigSchemaV2 > sysctl`

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

### <a name="sysctl_anyOf_i0"></a>Property `AosConfigSchemaV2 > sysctl > anyOf > item 0`

|                           |                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                     |
| **Additional properties** | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#sysctl_anyOf_i0_additionalProperties) |

| Property                                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [](#sysctl_anyOf_i0_additionalProperties ) | No      | string | No         | -          | -                 |

#### <a name="sysctl_anyOf_i0_additionalProperties"></a>Property `AosConfigSchemaV2 > sysctl > anyOf > item 0 > additionalProperties`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="sysctl_anyOf_i1"></a>Property `AosConfigSchemaV2 > sysctl > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2026-06-05 at 13:49:29 +0300
