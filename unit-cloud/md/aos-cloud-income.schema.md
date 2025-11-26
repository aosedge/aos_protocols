# AosUploadMetaConfig

- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosUploadMetaConfig > schemaVersion`](#schemaVersion)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosUploadMetaConfig > publisher`](#publisher)
  - [Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher`](#publisher_anyOf_i0)
    - [Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher > author`](#publisher_anyOf_i0_author)
      - [Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher > author > anyOf > item 0`](#publisher_anyOf_i0_author_anyOf_i0)
      - [Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher > author > anyOf > item 1`](#publisher_anyOf_i0_author_anyOf_i1)
    - [Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher > company`](#publisher_anyOf_i0_company)
      - [Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher > company > anyOf > item 0`](#publisher_anyOf_i0_company_anyOf_i0)
      - [Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher > company > anyOf > item 1`](#publisher_anyOf_i0_company_anyOf_i1)
  - [Property `AosUploadMetaConfig > publisher > anyOf > item 1`](#publisher_anyOf_i1)
- [![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosUploadMetaConfig > publish`](#publish)
  - [Property `AosUploadMetaConfig > publish > anyOf > AosPublish`](#publish_anyOf_i0)
    - [Property `AosUploadMetaConfig > publish > anyOf > AosPublish > tlsKey`](#publish_anyOf_i0_tlsKey)
    - [Property `AosUploadMetaConfig > publish > anyOf > AosPublish > signKey`](#publish_anyOf_i0_signKey)
      - [Property `AosUploadMetaConfig > publish > anyOf > AosPublish > signKey > anyOf > item 0`](#publish_anyOf_i0_signKey_anyOf_i0)
      - [Property `AosUploadMetaConfig > publish > anyOf > AosPublish > signKey > anyOf > item 1`](#publish_anyOf_i0_signKey_anyOf_i1)
    - [Property `AosUploadMetaConfig > publish > anyOf > AosPublish > domain`](#publish_anyOf_i0_domain)
      - [Property `AosUploadMetaConfig > publish > anyOf > AosPublish > domain > anyOf > item 0`](#publish_anyOf_i0_domain_anyOf_i0)
      - [Property `AosUploadMetaConfig > publish > anyOf > AosPublish > domain > anyOf > item 1`](#publish_anyOf_i0_domain_anyOf_i1)
  - [Property `AosUploadMetaConfig > publish > anyOf > item 1`](#publish_anyOf_i1)
- [![Required](https://img.shields.io/badge/Required-blue) Property `AosUploadMetaConfig > items`](#items)
  - [AosUploadMetaConfig > items > AosUpdateItem](#items_items)
    - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity`](#items_items_identity)
      - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > id`](#items_items_identity_id)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > id > anyOf > item 0`](#items_items_identity_id_anyOf_i0)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > id > anyOf > item 1`](#items_items_identity_id_anyOf_i1)
      - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > type`](#items_items_identity_type)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > type > anyOf > item 0`](#items_items_identity_type_anyOf_i0)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > type > anyOf > item 1`](#items_items_identity_type_anyOf_i1)
      - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > codename`](#items_items_identity_codename)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > codename > anyOf > item 0`](#items_items_identity_codename_anyOf_i0)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > codename > anyOf > item 1`](#items_items_identity_codename_anyOf_i1)
      - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > title`](#items_items_identity_title)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > title > anyOf > item 0`](#items_items_identity_title_anyOf_i0)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > title > anyOf > item 1`](#items_items_identity_title_anyOf_i1)
      - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > description`](#items_items_identity_description)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > description > anyOf > item 0`](#items_items_identity_description_anyOf_i0)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > description > anyOf > item 1`](#items_items_identity_description_anyOf_i1)
      - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > urn`](#items_items_identity_urn)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > urn > anyOf > item 0`](#items_items_identity_urn_anyOf_i0)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > identity > urn > anyOf > item 1`](#items_items_identity_urn_anyOf_i1)
    - [Property `AosUploadMetaConfig > items > AosUpdateItem > sourceFolder`](#items_items_sourceFolder)
      - [Property `AosUploadMetaConfig > items > AosUpdateItem > sourceFolder > anyOf > item 0`](#items_items_sourceFolder_anyOf_i0)
      - [Property `AosUploadMetaConfig > items > AosUpdateItem > sourceFolder > anyOf > item 1`](#items_items_sourceFolder_anyOf_i1)
    - [Property `AosUploadMetaConfig > items > AosUpdateItem > images`](#items_items_images)
      - [AosUploadMetaConfig > items > AosUpdateItem > images > AosImage](#items_items_images_items)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > sourceFolder`](#items_items_images_items_sourceFolder)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo`](#items_items_images_items_osInfo)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > os`](#items_items_images_items_osInfo_os)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > version`](#items_items_images_items_osInfo_version)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > version > anyOf > item 0`](#items_items_images_items_osInfo_version_anyOf_i0)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > version > anyOf > item 1`](#items_items_images_items_osInfo_version_anyOf_i1)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > features`](#items_items_images_items_osInfo_features)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > features > anyOf > item 0`](#items_items_images_items_osInfo_features_anyOf_i0)
              - [AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > features > anyOf > item 0 > item 0 items](#items_items_images_items_osInfo_features_anyOf_i0_items)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > features > anyOf > item 1`](#items_items_images_items_osInfo_features_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > archInfo`](#items_items_images_items_archInfo)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > archInfo > architecture`](#items_items_images_items_archInfo_architecture)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > archInfo > variant`](#items_items_images_items_archInfo_variant)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > archInfo > variant > anyOf > item 0`](#items_items_images_items_archInfo_variant_anyOf_i0)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > archInfo > variant > anyOf > item 1`](#items_items_images_items_archInfo_variant_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > env`](#items_items_images_items_env)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > env > anyOf > item 0`](#items_items_images_items_env_anyOf_i0)
            - [AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > env > anyOf > item 0 > item 0 items](#items_items_images_items_env_anyOf_i0_items)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > env > anyOf > item 1`](#items_items_images_items_env_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > workingDir`](#items_items_images_items_workingDir)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > workingDir > anyOf > item 0`](#items_items_images_items_workingDir_anyOf_i0)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > workingDir > anyOf > item 1`](#items_items_images_items_workingDir_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > cmd`](#items_items_images_items_cmd)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > cmd > anyOf > item 0`](#items_items_images_items_cmd_anyOf_i0)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > cmd > anyOf > item 1`](#items_items_images_items_cmd_anyOf_i1)
    - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration`](#items_items_configuration)
      - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration`](#items_items_configuration_anyOf_i0)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > env`](#items_items_configuration_anyOf_i0_env)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > env > anyOf > item 0`](#items_items_configuration_anyOf_i0_env_anyOf_i0)
            - [AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > env > anyOf > item 0 > item 0 items](#items_items_configuration_anyOf_i0_env_anyOf_i0_items)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > env > anyOf > item 1`](#items_items_configuration_anyOf_i0_env_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > workingDir`](#items_items_configuration_anyOf_i0_workingDir)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > workingDir > anyOf > item 0`](#items_items_configuration_anyOf_i0_workingDir_anyOf_i0)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > workingDir > anyOf > item 1`](#items_items_configuration_anyOf_i0_workingDir_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances`](#items_items_configuration_anyOf_i0_instances)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo`](#items_items_configuration_anyOf_i0_instances_anyOf_i0)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo > minInstances`](#items_items_configuration_anyOf_i0_instances_anyOf_i0_minInstances)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo > priority`](#items_items_configuration_anyOf_i0_instances_anyOf_i0_priority)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo > labels`](#items_items_configuration_anyOf_i0_instances_anyOf_i0_labels)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo > labels > anyOf > item 0`](#items_items_configuration_anyOf_i0_instances_anyOf_i0_labels_anyOf_i0)
                - [AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo > labels > anyOf > item 0 > item 0 items](#items_items_configuration_anyOf_i0_instances_anyOf_i0_labels_anyOf_i0_items)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo > labels > anyOf > item 1`](#items_items_configuration_anyOf_i0_instances_anyOf_i0_labels_anyOf_i1)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > item 1`](#items_items_configuration_anyOf_i0_instances_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > cmd`](#items_items_configuration_anyOf_i0_cmd)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > cmd > anyOf > item 0`](#items_items_configuration_anyOf_i0_cmd_anyOf_i0)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > cmd > anyOf > item 1`](#items_items_configuration_anyOf_i0_cmd_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > skipResourceLimits`](#items_items_configuration_anyOf_i0_skipResourceLimits)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > balancingPolicy`](#items_items_configuration_anyOf_i0_balancingPolicy)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > baseLayerIsNodeRootfs`](#items_items_configuration_anyOf_i0_baseLayerIsNodeRootfs)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > baseLayerIsNodeRootfs > anyOf > item 0`](#items_items_configuration_anyOf_i0_baseLayerIsNodeRootfs_anyOf_i0)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > baseLayerIsNodeRootfs > anyOf > item 1`](#items_items_configuration_anyOf_i0_baseLayerIsNodeRootfs_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > hostname`](#items_items_configuration_anyOf_i0_hostname)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > hostname > anyOf > item 0`](#items_items_configuration_anyOf_i0_hostname_anyOf_i0)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > hostname > anyOf > item 1`](#items_items_configuration_anyOf_i0_hostname_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > exposedPorts`](#items_items_configuration_anyOf_i0_exposedPorts)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > exposedPorts > anyOf > item 0`](#items_items_configuration_anyOf_i0_exposedPorts_anyOf_i0)
            - [AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > exposedPorts > anyOf > item 0 > item 0 items](#items_items_configuration_anyOf_i0_exposedPorts_anyOf_i0_items)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > exposedPorts > anyOf > item 1`](#items_items_configuration_anyOf_i0_exposedPorts_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runtimes`](#items_items_configuration_anyOf_i0_runtimes)
          - [AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runtimes > AosIdentity](#items_items_configuration_anyOf_i0_runtimes_items)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters`](#items_items_configuration_anyOf_i0_runParameters)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters`](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > startInterval`](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startInterval)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > startInterval > anyOf > item 0`](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startInterval_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > startInterval > anyOf > item 1`](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startInterval_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > startBurst`](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startBurst)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > startBurst > anyOf > item 0`](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startBurst_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > startBurst > anyOf > item 1`](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startBurst_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > restartInterval`](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_restartInterval)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > restartInterval > anyOf > item 0`](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_restartInterval_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > restartInterval > anyOf > item 1`](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_restartInterval_anyOf_i1)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > item 1`](#items_items_configuration_anyOf_i0_runParameters_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > offlineTTL`](#items_items_configuration_anyOf_i0_offlineTTL)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > offlineTTL > anyOf > item 0`](#items_items_configuration_anyOf_i0_offlineTTL_anyOf_i0)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > offlineTTL > anyOf > item 1`](#items_items_configuration_anyOf_i0_offlineTTL_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > resources`](#items_items_configuration_anyOf_i0_resources)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > resources > anyOf > item 0`](#items_items_configuration_anyOf_i0_resources_anyOf_i0)
            - [AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > resources > anyOf > item 0 > AosResourceAccess](#items_items_configuration_anyOf_i0_resources_anyOf_i0_items)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > resources > anyOf > item 0 > AosResourceAccess > name`](#items_items_configuration_anyOf_i0_resources_anyOf_i0_items_name)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > resources > anyOf > item 0 > AosResourceAccess > mode`](#items_items_configuration_anyOf_i0_resources_anyOf_i0_items_mode)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > resources > anyOf > item 1`](#items_items_configuration_anyOf_i0_resources_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > allowedConnections`](#items_items_configuration_anyOf_i0_allowedConnections)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > allowedConnections > anyOf > item 0`](#items_items_configuration_anyOf_i0_allowedConnections_anyOf_i0)
            - [AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > allowedConnections > anyOf > item 0 > item 0 items](#items_items_configuration_anyOf_i0_allowedConnections_anyOf_i0_items)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > allowedConnections > anyOf > item 1`](#items_items_configuration_anyOf_i0_allowedConnections_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas`](#items_items_configuration_anyOf_i0_quotas)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > cpuLimit`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_cpuLimit)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > cpuLimit > anyOf > item 0`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_cpuLimit_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > cpuLimit > anyOf > item 1`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_cpuLimit_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > ramLimit`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_ramLimit)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > ramLimit > anyOf > item 0`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_ramLimit_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > ramLimit > anyOf > item 1`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_ramLimit_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > storageLimit`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_storageLimit)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > storageLimit > anyOf > item 0`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_storageLimit_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > storageLimit > anyOf > item 1`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_storageLimit_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > stateLimit`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_stateLimit)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > stateLimit > anyOf > item 0`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_stateLimit_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > stateLimit > anyOf > item 1`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_stateLimit_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > tmpLimit`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_tmpLimit)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > tmpLimit > anyOf > item 0`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_tmpLimit_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > tmpLimit > anyOf > item 1`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_tmpLimit_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > uploadSpeed`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_uploadSpeed)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > uploadSpeed > anyOf > item 0`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_uploadSpeed_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > uploadSpeed > anyOf > item 1`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_uploadSpeed_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > downloadSpeed`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_downloadSpeed)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > downloadSpeed > anyOf > item 0`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_downloadSpeed_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > downloadSpeed > anyOf > item 1`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_downloadSpeed_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > noFileLimit`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_noFileLimit)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > noFileLimit > anyOf > item 0`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_noFileLimit_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > noFileLimit > anyOf > item 1`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_noFileLimit_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > pidsLimit`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_pidsLimit)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > pidsLimit > anyOf > item 0`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_pidsLimit_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > pidsLimit > anyOf > item 1`](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_pidsLimit_anyOf_i1)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > item 1`](#items_items_configuration_anyOf_i0_quotas_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules`](#items_items_configuration_anyOf_i0_alertRules)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0)
                - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minTimeout`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minTimeout)
                  - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minTimeout > anyOf > item 0`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i0)
                  - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minTimeout > anyOf > item 1`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i1)
                - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minThreshold`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minThreshold)
                  - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minThreshold > anyOf > item 0`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i0)
                  - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minThreshold > anyOf > item 1`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i1)
                - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > maxThreshold`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold)
                  - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > maxThreshold > anyOf > item 0`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i0)
                  - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > maxThreshold > anyOf > item 1`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i1)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > item 1`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > cpu`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_cpu)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > cpu > anyOf > AosAlertRulePercents`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_cpu_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > cpu > anyOf > item 1`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_cpu_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > storage`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_storage)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > storage > anyOf > AosAlertRulePercents`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_storage_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > storage > anyOf > item 1`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_storage_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0)
                - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minTimeout`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minTimeout)
                  - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minTimeout > anyOf > item 0`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i0)
                  - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minTimeout > anyOf > item 1`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i1)
                - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minThreshold`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minThreshold)
                  - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minThreshold > anyOf > item 0`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i0)
                  - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minThreshold > anyOf > item 1`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i1)
                - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > maxThreshold`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold)
                  - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > maxThreshold > anyOf > item 0`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i0)
                  - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > maxThreshold > anyOf > item 1`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i1)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > item 1`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i1)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > download`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_download)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > download > anyOf > AosAlertRulePoints`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_download_anyOf_i0)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > download > anyOf > item 1`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_download_anyOf_i1)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > item 1`](#items_items_configuration_anyOf_i0_alertRules_anyOf_i1)
        - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > permissions`](#items_items_configuration_anyOf_i0_permissions)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > permissions > anyOf > item 0`](#items_items_configuration_anyOf_i0_permissions_anyOf_i0)
            - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > permissions > anyOf > item 0 > additionalProperties`](#items_items_configuration_anyOf_i0_permissions_anyOf_i0_additionalProperties)
              - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > permissions > anyOf > item 0 > additionalProperties > additionalProperties`](#items_items_configuration_anyOf_i0_permissions_anyOf_i0_additionalProperties_additionalProperties)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > permissions > anyOf > item 1`](#items_items_configuration_anyOf_i0_permissions_anyOf_i1)
      - [Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > item 1`](#items_items_configuration_anyOf_i1)
    - [Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies`](#items_items_dependencies)
      - [Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 0`](#items_items_dependencies_anyOf_i0)
        - [AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 0 > AosDependency](#items_items_dependencies_anyOf_i0_items)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 0 > AosDependency > identity`](#items_items_dependencies_anyOf_i0_items_identity)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 0 > AosDependency > versions`](#items_items_dependencies_anyOf_i0_items_versions)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 0 > AosDependency > includePreRelease`](#items_items_dependencies_anyOf_i0_items_includePreRelease)
          - [Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 0 > AosDependency > condition`](#items_items_dependencies_anyOf_i0_items_condition)
      - [Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 1`](#items_items_dependencies_anyOf_i1)

**Title:** AosUploadMetaConfig

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

| Property                           | Pattern | Type        | Deprecated | Definition | Title/Description                        |
| ---------------------------------- | ------- | ----------- | ---------- | ---------- | ---------------------------------------- |
| - [schemaVersion](#schemaVersion ) | No      | const       | No         | -          | Schemaversion                            |
| - [publisher](#publisher )         | No      | Combination | No         | -          | Publisher information about the package. |
| - [publish](#publish )             | No      | Combination | No         | -          | Publish information about the package.   |
| + [items](#items )                 | No      | array       | No         | -          | Items                                    |

## <a name="schemaVersion"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosUploadMetaConfig > schemaVersion`

**Title:** Schemaversion

|             |         |
| ----------- | ------- |
| **Type**    | `const` |
| **Default** | `2`     |

**Description:** Schema version of the metadata configuration.

Specific value: `2`

## <a name="publisher"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosUploadMetaConfig > publisher`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Publisher information about the package.

| Any of(Option)                      |
| ----------------------------------- |
| [AosPublisher](#publisher_anyOf_i0) |
| [item 1](#publisher_anyOf_i1)       |

### <a name="publisher_anyOf_i0"></a>Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher`

**Title:** AosPublisher

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosPublisher                                                        |

| Property                                  | Pattern | Type        | Deprecated | Definition | Title/Description |
| ----------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [author](#publisher_anyOf_i0_author )   | No      | Combination | No         | -          | Author            |
| - [company](#publisher_anyOf_i0_company ) | No      | Combination | No         | -          | Company           |

#### <a name="publisher_anyOf_i0_author"></a>Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher > author`

**Title:** Author

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Author of the package.

| Any of(Option)                                |
| --------------------------------------------- |
| [item 0](#publisher_anyOf_i0_author_anyOf_i0) |
| [item 1](#publisher_anyOf_i0_author_anyOf_i1) |

##### <a name="publisher_anyOf_i0_author_anyOf_i0"></a>Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher > author > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

##### <a name="publisher_anyOf_i0_author_anyOf_i1"></a>Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher > author > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="publisher_anyOf_i0_company"></a>Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher > company`

**Title:** Company

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Company that created the package.

| Any of(Option)                                 |
| ---------------------------------------------- |
| [item 0](#publisher_anyOf_i0_company_anyOf_i0) |
| [item 1](#publisher_anyOf_i0_company_anyOf_i1) |

##### <a name="publisher_anyOf_i0_company_anyOf_i0"></a>Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher > company > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

##### <a name="publisher_anyOf_i0_company_anyOf_i1"></a>Property `AosUploadMetaConfig > publisher > anyOf > AosPublisher > company > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="publisher_anyOf_i1"></a>Property `AosUploadMetaConfig > publisher > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="publish"></a>![Optional](https://img.shields.io/badge/Optional-yellow) Property `AosUploadMetaConfig > publish`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Publish information about the package.

| Any of(Option)                  |
| ------------------------------- |
| [AosPublish](#publish_anyOf_i0) |
| [item 1](#publish_anyOf_i1)     |

### <a name="publish_anyOf_i0"></a>Property `AosUploadMetaConfig > publish > anyOf > AosPublish`

**Title:** AosPublish

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosPublish                                                          |

| Property                                | Pattern | Type        | Deprecated | Definition | Title/Description |
| --------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [tlsKey](#publish_anyOf_i0_tlsKey )   | No      | string      | No         | -          | Tlskey            |
| - [signKey](#publish_anyOf_i0_signKey ) | No      | Combination | No         | -          | Signkey           |
| - [domain](#publish_anyOf_i0_domain )   | No      | Combination | No         | -          | Domain            |

#### <a name="publish_anyOf_i0_tlsKey"></a>Property `AosUploadMetaConfig > publish > anyOf > AosPublish > tlsKey`

**Title:** Tlskey

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Certificate and private key for the TLS connection.

#### <a name="publish_anyOf_i0_signKey"></a>Property `AosUploadMetaConfig > publish > anyOf > AosPublish > signKey`

**Title:** Signkey

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Signing key for the package. If not provided, the package will be signed with the TLS key.

| Any of(Option)                               |
| -------------------------------------------- |
| [item 0](#publish_anyOf_i0_signKey_anyOf_i0) |
| [item 1](#publish_anyOf_i0_signKey_anyOf_i1) |

##### <a name="publish_anyOf_i0_signKey_anyOf_i0"></a>Property `AosUploadMetaConfig > publish > anyOf > AosPublish > signKey > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

##### <a name="publish_anyOf_i0_signKey_anyOf_i1"></a>Property `AosUploadMetaConfig > publish > anyOf > AosPublish > signKey > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="publish_anyOf_i0_domain"></a>Property `AosUploadMetaConfig > publish > anyOf > AosPublish > domain`

**Title:** Domain

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Domain to upload the package. If not provided, domain will be extracted from the certificate.

| Any of(Option)                              |
| ------------------------------------------- |
| [item 0](#publish_anyOf_i0_domain_anyOf_i0) |
| [item 1](#publish_anyOf_i0_domain_anyOf_i1) |

##### <a name="publish_anyOf_i0_domain_anyOf_i0"></a>Property `AosUploadMetaConfig > publish > anyOf > AosPublish > domain > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

##### <a name="publish_anyOf_i0_domain_anyOf_i1"></a>Property `AosUploadMetaConfig > publish > anyOf > AosPublish > domain > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="publish_anyOf_i1"></a>Property `AosUploadMetaConfig > publish > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="items"></a>![Required](https://img.shields.io/badge/Required-blue) Property `AosUploadMetaConfig > items`

**Title:** Items

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** List of the update items to upload.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [AosUpdateItem](#items_items)   | -           |

### <a name="items_items"></a>AosUploadMetaConfig > items > AosUpdateItem

**Title:** AosUpdateItem

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosUpdateItem                                                       |

| Property                                       | Pattern | Type        | Deprecated | Definition             | Title/Description                 |
| ---------------------------------------------- | ------- | ----------- | ---------- | ---------------------- | --------------------------------- |
| + [identity](#items_items_identity )           | No      | object      | No         | In #/$defs/AosIdentity | AosIdentity                       |
| - [sourceFolder](#items_items_sourceFolder )   | No      | Combination | No         | -                      | Sourcefolder                      |
| + [images](#items_items_images )               | No      | array       | No         | -                      | Images                            |
| - [configuration](#items_items_configuration ) | No      | Combination | No         | -                      | Configuration of the update item. |
| - [dependencies](#items_items_dependencies )   | No      | Combination | No         | -                      | Dependencies                      |

#### <a name="items_items_identity"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity`

**Title:** AosIdentity

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosIdentity                                                         |

**Description:** Identity of the update item.

| Property                                            | Pattern | Type        | Deprecated | Definition | Title/Description                                    |
| --------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ---------------------------------------------------- |
| - [id](#items_items_identity_id )                   | No      | Combination | No         | -          | Aos object UUID identifier. Unique per Aos instance. |
| - [type](#items_items_identity_type )               | No      | Combination | No         | -          | Aos object type.                                     |
| - [codename](#items_items_identity_codename )       | No      | Combination | No         | -          | Aos object codename.                                 |
| - [title](#items_items_identity_title )             | No      | Combination | No         | -          | Aos object title.                                    |
| - [description](#items_items_identity_description ) | No      | Combination | No         | -          | Aos object description.                              |
| - [urn](#items_items_identity_urn )                 | No      | Combination | No         | -          | Aos object URN.                                      |

##### <a name="items_items_identity_id"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > id`

**Title:** Aos object UUID identifier. Unique per Aos instance.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object unique per Aos instance UUID.

| Any of(Option)                              |
| ------------------------------------------- |
| [item 0](#items_items_identity_id_anyOf_i0) |
| [item 1](#items_items_identity_id_anyOf_i1) |

###### <a name="items_items_identity_id_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > id > anyOf > item 0`

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `uuid4`  |

###### <a name="items_items_identity_id_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > id > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="items_items_identity_type"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > type`

**Title:** Aos object type.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object type. E.g.: AosService, AosComponent

| Any of(Option)                                |
| --------------------------------------------- |
| [item 0](#items_items_identity_type_anyOf_i0) |
| [item 1](#items_items_identity_type_anyOf_i1) |

###### <a name="items_items_identity_type_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > type > anyOf > item 0`

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

Must be one of:
* "component"
* "service"
* "layer"
* "subject"
* "oem"
* "sp"
* "node"
* "runtime"

###### <a name="items_items_identity_type_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > type > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="items_items_identity_codename"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > codename`

**Title:** Aos object codename.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object codename. Uniqueness depends on object type.

| Any of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#items_items_identity_codename_anyOf_i0) |
| [item 1](#items_items_identity_codename_anyOf_i1) |

###### <a name="items_items_identity_codename_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > codename > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_identity_codename_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > codename > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="items_items_identity_title"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > title`

**Title:** Aos object title.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object title.

| Any of(Option)                                 |
| ---------------------------------------------- |
| [item 0](#items_items_identity_title_anyOf_i0) |
| [item 1](#items_items_identity_title_anyOf_i1) |

###### <a name="items_items_identity_title_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > title > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_identity_title_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > title > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="items_items_identity_description"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > description`

**Title:** Aos object description.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object description.

| Any of(Option)                                       |
| ---------------------------------------------------- |
| [item 0](#items_items_identity_description_anyOf_i0) |
| [item 1](#items_items_identity_description_anyOf_i1) |

###### <a name="items_items_identity_description_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > description > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_identity_description_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > description > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="items_items_identity_urn"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > urn`

**Title:** Aos object URN.

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Aos object URN. Globally unique.

| Any of(Option)                               |
| -------------------------------------------- |
| [item 0](#items_items_identity_urn_anyOf_i0) |
| [item 1](#items_items_identity_urn_anyOf_i1) |

###### <a name="items_items_identity_urn_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > urn > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_identity_urn_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > identity > urn > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="items_items_sourceFolder"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > sourceFolder`

**Title:** Sourcefolder

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Source folder for the item. If absent, codename from identity will be used.

| Any of(Option)                               |
| -------------------------------------------- |
| [item 0](#items_items_sourceFolder_anyOf_i0) |
| [item 1](#items_items_sourceFolder_anyOf_i1) |

##### <a name="items_items_sourceFolder_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > sourceFolder > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

##### <a name="items_items_sourceFolder_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > sourceFolder > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="items_items_images"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images`

**Title:** Images

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** List of images for different architectures.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be       | Description |
| ------------------------------------- | ----------- |
| [AosImage](#items_items_images_items) | -           |

##### <a name="items_items_images_items"></a>AosUploadMetaConfig > items > AosUpdateItem > images > AosImage

**Title:** AosImage

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosImage                                                            |

| Property                                                  | Pattern | Type        | Deprecated | Definition             | Title/Description |
| --------------------------------------------------------- | ------- | ----------- | ---------- | ---------------------- | ----------------- |
| + [sourceFolder](#items_items_images_items_sourceFolder ) | No      | string      | No         | -                      | Sourcefolder      |
| - [osInfo](#items_items_images_items_osInfo )             | No      | object      | No         | In #/$defs/AosOsInfo   | AosOsInfo         |
| + [archInfo](#items_items_images_items_archInfo )         | No      | object      | No         | In #/$defs/AosArchInfo | AosArchInfo       |
| - [env](#items_items_images_items_env )                   | No      | Combination | No         | -                      | Env               |
| - [workingDir](#items_items_images_items_workingDir )     | No      | Combination | No         | -                      | Workingdir        |
| - [cmd](#items_items_images_items_cmd )                   | No      | Combination | No         | -                      | Cmd               |

###### <a name="items_items_images_items_sourceFolder"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > sourceFolder`

**Title:** Sourcefolder

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Source folder for the image.

###### <a name="items_items_images_items_osInfo"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo`

**Title:** AosOsInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `{"os": "Linux", "version": null, "features": null}`                        |
| **Defined in**            | #/$defs/AosOsInfo                                                           |

**Description:** OS information of the image.

| Property                                                 | Pattern | Type        | Deprecated | Definition | Title/Description |
| -------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [os](#items_items_images_items_osInfo_os )             | No      | string      | No         | -          | Os                |
| - [version](#items_items_images_items_osInfo_version )   | No      | Combination | No         | -          | Version           |
| - [features](#items_items_images_items_osInfo_features ) | No      | Combination | No         | -          | Features          |

###### <a name="items_items_images_items_osInfo_os"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > os`

**Title:** Os

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Example:**

```json
"linux"
```

###### <a name="items_items_images_items_osInfo_version"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > version`

**Title:** Version

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** The version of the OS.

**Example:**

```json
"6.8.0"
```

| Any of(Option)                                              |
| ----------------------------------------------------------- |
| [item 0](#items_items_images_items_osInfo_version_anyOf_i0) |
| [item 1](#items_items_images_items_osInfo_version_anyOf_i1) |

###### <a name="items_items_images_items_osInfo_version_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > version > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_images_items_osInfo_version_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > version > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_images_items_osInfo_features"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > features`

**Title:** Features

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** This OPTIONAL property specifies an array of strings, each specifying a mandatory OS feature.

| Any of(Option)                                               |
| ------------------------------------------------------------ |
| [item 0](#items_items_images_items_osInfo_features_anyOf_i0) |
| [item 1](#items_items_images_items_osInfo_features_anyOf_i1) |

###### <a name="items_items_images_items_osInfo_features_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > features > anyOf > item 0`

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

| Each item of this array must be                                          | Description |
| ------------------------------------------------------------------------ | ----------- |
| [item 0 items](#items_items_images_items_osInfo_features_anyOf_i0_items) | -           |

###### <a name="items_items_images_items_osInfo_features_anyOf_i0_items"></a>AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > features > anyOf > item 0 > item 0 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_images_items_osInfo_features_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > osInfo > features > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_images_items_archInfo"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > archInfo`

**Title:** AosArchInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosArchInfo                                                         |

**Description:** Architecture information of the image.

| Property                                                           | Pattern | Type        | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------ | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [architecture](#items_items_images_items_archInfo_architecture ) | No      | string      | No         | -          | Architecture      |
| - [variant](#items_items_images_items_archInfo_variant )           | No      | Combination | No         | -          | Variant           |

###### <a name="items_items_images_items_archInfo_architecture"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > archInfo > architecture`

**Title:** Architecture

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The architecture of the CPU. Refer to the "https://github.com/opencontainers/image-spec/blob/main/config.md#properties"

**Examples:**

```json
"amd64"
```

```json
"arm64"
```

```json
"arm"
```

###### <a name="items_items_images_items_archInfo_variant"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > archInfo > variant`

**Title:** Variant

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** The variant of the specified CPU architecture. Refer to the "https://github.com/opencontainers/image-spec/blob/main/config.md#properties"

| Any of(Option)                                                |
| ------------------------------------------------------------- |
| [item 0](#items_items_images_items_archInfo_variant_anyOf_i0) |
| [item 1](#items_items_images_items_archInfo_variant_anyOf_i1) |

###### <a name="items_items_images_items_archInfo_variant_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > archInfo > variant > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_images_items_archInfo_variant_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > archInfo > variant > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_images_items_env"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > env`

**Title:** Env

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Environment variables for the image.

| Any of(Option)                                   |
| ------------------------------------------------ |
| [item 0](#items_items_images_items_env_anyOf_i0) |
| [item 1](#items_items_images_items_env_anyOf_i1) |

###### <a name="items_items_images_items_env_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > env > anyOf > item 0`

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

| Each item of this array must be                              | Description |
| ------------------------------------------------------------ | ----------- |
| [item 0 items](#items_items_images_items_env_anyOf_i0_items) | -           |

###### <a name="items_items_images_items_env_anyOf_i0_items"></a>AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > env > anyOf > item 0 > item 0 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_images_items_env_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > env > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_images_items_workingDir"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > workingDir`

**Title:** Workingdir

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Working directory for the image.

| Any of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#items_items_images_items_workingDir_anyOf_i0) |
| [item 1](#items_items_images_items_workingDir_anyOf_i1) |

###### <a name="items_items_images_items_workingDir_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > workingDir > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_images_items_workingDir_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > workingDir > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_images_items_cmd"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > cmd`

**Title:** Cmd

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Command line for the image.

| Any of(Option)                                   |
| ------------------------------------------------ |
| [item 0](#items_items_images_items_cmd_anyOf_i0) |
| [item 1](#items_items_images_items_cmd_anyOf_i1) |

###### <a name="items_items_images_items_cmd_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > cmd > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_images_items_cmd_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > images > AosImage > cmd > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="items_items_configuration"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Configuration of the update item.

| Any of(Option)                                                    |
| ----------------------------------------------------------------- |
| [AosUpdateItemConfiguration](#items_items_configuration_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i1)                     |

##### <a name="items_items_configuration_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration`

**Title:** AosUpdateItemConfiguration

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosUpdateItemConfiguration                                          |

| Property                                                                              | Pattern | Type             | Deprecated | Definition | Title/Description                |
| ------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | -------------------------------- |
| - [env](#items_items_configuration_anyOf_i0_env )                                     | No      | Combination      | No         | -          | Env                              |
| - [workingDir](#items_items_configuration_anyOf_i0_workingDir )                       | No      | Combination      | No         | -          | Workingdir                       |
| - [instances](#items_items_configuration_anyOf_i0_instances )                         | No      | Combination      | No         | -          | Instances info.                  |
| - [cmd](#items_items_configuration_anyOf_i0_cmd )                                     | No      | Combination      | No         | -          | Cmd                              |
| - [skipResourceLimits](#items_items_configuration_anyOf_i0_skipResourceLimits )       | No      | boolean          | No         | -          | Skipresourcelimits               |
| - [balancingPolicy](#items_items_configuration_anyOf_i0_balancingPolicy )             | No      | enum (of string) | No         | -          | Balancingpolicy                  |
| - [baseLayerIsNodeRootfs](#items_items_configuration_anyOf_i0_baseLayerIsNodeRootfs ) | No      | Combination      | No         | -          | Baselayerisnoderootfs            |
| - [hostname](#items_items_configuration_anyOf_i0_hostname )                           | No      | Combination      | No         | -          | Hostname                         |
| - [exposedPorts](#items_items_configuration_anyOf_i0_exposedPorts )                   | No      | Combination      | No         | -          | Exposedports                     |
| - [runtimes](#items_items_configuration_anyOf_i0_runtimes )                           | No      | array            | No         | -          | Runtimes                         |
| - [runParameters](#items_items_configuration_anyOf_i0_runParameters )                 | No      | Combination      | No         | -          | Run parameters for the Aos item. |
| - [offlineTTL](#items_items_configuration_anyOf_i0_offlineTTL )                       | No      | Combination      | No         | -          | Offlinettl                       |
| - [resources](#items_items_configuration_anyOf_i0_resources )                         | No      | Combination      | No         | -          | Resources                        |
| - [allowedConnections](#items_items_configuration_anyOf_i0_allowedConnections )       | No      | Combination      | No         | -          | Allowedconnections               |
| - [quotas](#items_items_configuration_anyOf_i0_quotas )                               | No      | Combination      | No         | -          | Quotas for the service.          |
| - [alertRules](#items_items_configuration_anyOf_i0_alertRules )                       | No      | Combination      | No         | -          | Alert rules for the service.     |
| - [permissions](#items_items_configuration_anyOf_i0_permissions )                     | No      | Combination      | No         | -          | Permissions                      |

###### <a name="items_items_configuration_anyOf_i0_env"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > env`

**Title:** Env

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Environment variables for the image.

| Any of(Option)                                             |
| ---------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_env_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_env_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_env_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > env > anyOf > item 0`

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

| Each item of this array must be                                        | Description |
| ---------------------------------------------------------------------- | ----------- |
| [item 0 items](#items_items_configuration_anyOf_i0_env_anyOf_i0_items) | -           |

###### <a name="items_items_configuration_anyOf_i0_env_anyOf_i0_items"></a>AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > env > anyOf > item 0 > item 0 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_configuration_anyOf_i0_env_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > env > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_workingDir"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > workingDir`

**Title:** Workingdir

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Working directory for the image.

| Any of(Option)                                                    |
| ----------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_workingDir_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_workingDir_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_workingDir_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > workingDir > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_configuration_anyOf_i0_workingDir_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > workingDir > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_instances"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Instances info.

| Any of(Option)                                                             |
| -------------------------------------------------------------------------- |
| [AosInstancesInfo](#items_items_configuration_anyOf_i0_instances_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_instances_anyOf_i1)           |

###### <a name="items_items_configuration_anyOf_i0_instances_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo`

**Title:** AosInstancesInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosInstancesInfo                                                    |

**Description:** Schema for instances info.

| Property                                                                               | Pattern | Type        | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [minInstances](#items_items_configuration_anyOf_i0_instances_anyOf_i0_minInstances ) | No      | integer     | No         | -          | Mininstances      |
| - [priority](#items_items_configuration_anyOf_i0_instances_anyOf_i0_priority )         | No      | integer     | No         | -          | Priority          |
| - [labels](#items_items_configuration_anyOf_i0_instances_anyOf_i0_labels )             | No      | Combination | No         | -          | Labels            |

###### <a name="items_items_configuration_anyOf_i0_instances_anyOf_i0_minInstances"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo > minInstances`

**Title:** Mininstances

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `1`       |

**Description:** Minimum number of instances.

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &gt; 1   |
| **Maximum**  | &le; 100 |

###### <a name="items_items_configuration_anyOf_i0_instances_anyOf_i0_priority"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo > priority`

**Title:** Priority

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `0`       |

**Description:** Priority of the instances.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="items_items_configuration_anyOf_i0_instances_anyOf_i0_labels"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo > labels`

**Title:** Labels

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Labels of the instances.

| Any of(Option)                                                                   |
| -------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_instances_anyOf_i0_labels_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_instances_anyOf_i0_labels_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_instances_anyOf_i0_labels_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo > labels > anyOf > item 0`

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

| Each item of this array must be                                                              | Description |
| -------------------------------------------------------------------------------------------- | ----------- |
| [item 0 items](#items_items_configuration_anyOf_i0_instances_anyOf_i0_labels_anyOf_i0_items) | -           |

###### <a name="items_items_configuration_anyOf_i0_instances_anyOf_i0_labels_anyOf_i0_items"></a>AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo > labels > anyOf > item 0 > item 0 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_configuration_anyOf_i0_instances_anyOf_i0_labels_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > AosInstancesInfo > labels > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_instances_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > instances > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_cmd"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > cmd`

**Title:** Cmd

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Command line for the image.

| Any of(Option)                                             |
| ---------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_cmd_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_cmd_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_cmd_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > cmd > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_configuration_anyOf_i0_cmd_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > cmd > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_skipResourceLimits"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > skipResourceLimits`

**Title:** Skipresourcelimits

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `false`   |

**Description:** Use resource limits or not in pre-release versions.

###### <a name="items_items_configuration_anyOf_i0_balancingPolicy"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > balancingPolicy`

**Title:** Balancingpolicy

|             |                    |
| ----------- | ------------------ |
| **Type**    | `enum (of string)` |
| **Default** | `"enabled"`        |

**Description:** Balancing type. `disabled` means total prohibition from balancing to other nodes.`

Must be one of:
* "enabled"
* "disabled"

###### <a name="items_items_configuration_anyOf_i0_baseLayerIsNodeRootfs"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > baseLayerIsNodeRootfs`

**Title:** Baselayerisnoderootfs

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `true`                                                                      |

**Description:** Whether the base layer is the node rootfs or not.

| Any of(Option)                                                               |
| ---------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_baseLayerIsNodeRootfs_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_baseLayerIsNodeRootfs_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_baseLayerIsNodeRootfs_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > baseLayerIsNodeRootfs > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `boolean` |

###### <a name="items_items_configuration_anyOf_i0_baseLayerIsNodeRootfs_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > baseLayerIsNodeRootfs > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_hostname"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > hostname`

**Title:** Hostname

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** The hostname of the Aos service. The FQDN is {hostname].{service_provider}.

| Any of(Option)                                                  |
| --------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_hostname_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_hostname_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_hostname_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > hostname > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_configuration_anyOf_i0_hostname_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > hostname > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_exposedPorts"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > exposedPorts`

**Title:** Exposedports

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** List of exposed ports.

**Examples:**

```json
8080
```

```json
8081
```

| Any of(Option)                                                      |
| ------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_exposedPorts_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_exposedPorts_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_exposedPorts_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > exposedPorts > anyOf > item 0`

|          |                    |
| -------- | ------------------ |
| **Type** | `array of integer` |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                 | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [item 0 items](#items_items_configuration_anyOf_i0_exposedPorts_anyOf_i0_items) | -           |

###### <a name="items_items_configuration_anyOf_i0_exposedPorts_anyOf_i0_items"></a>AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > exposedPorts > anyOf > item 0 > item 0 items

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_exposedPorts_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > exposedPorts > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_runtimes"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runtimes`

**Title:** Runtimes

|             |                                                                                                                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**    | `array`                                                                                                                                                                                                        |
| **Default** | `[{"id": null, "type": "runtime", "codename": "runc", "title": null, "description": null, "urn": null}, {"id": null, "type": "runtime", "codename": "crun", "title": null, "description": null, "urn": null}]` |

**Description:** Aos service allowed runner types. Absense means ["runc", "crun"].

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                   | Description             |
| ----------------------------------------------------------------- | ----------------------- |
| [AosIdentity](#items_items_configuration_anyOf_i0_runtimes_items) | Aos objects identifier. |

###### <a name="items_items_configuration_anyOf_i0_runtimes_items"></a>AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runtimes > AosIdentity

**Title:** AosIdentity

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Same definition as**    | [identity](#items_items_identity)                                           |

**Description:** Aos objects identifier.

###### <a name="items_items_configuration_anyOf_i0_runParameters"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Run parameters for the Aos item.

| Any of(Option)                                                                 |
| ------------------------------------------------------------------------------ |
| [AosRunParameters](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_runParameters_anyOf_i1)           |

###### <a name="items_items_configuration_anyOf_i0_runParameters_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters`

**Title:** AosRunParameters

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosRunParameters                                                    |

| Property                                                                                         | Pattern | Type        | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------------------ | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [startInterval](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startInterval )     | No      | Combination | No         | -          | Startinterval     |
| - [startBurst](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startBurst )           | No      | Combination | No         | -          | Startburst        |
| - [restartInterval](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_restartInterval ) | No      | Combination | No         | -          | Restartinterval   |

###### <a name="items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startInterval"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > startInterval`

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

| Any of(Option)                                                                              |
| ------------------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startInterval_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startInterval_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startInterval_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > startInterval > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

###### <a name="items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startInterval_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > startInterval > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startBurst"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > startBurst`

**Title:** Startburst

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:**     Service which are started more than burst times within an interval time span are not permitted to start any more.
    Use `startInterval` to configure the checking interval and `startBurst`
    to configure how many starts per interval are allowed.

**Examples:**

```json
3
```

```json
10
```

| Any of(Option)                                                                           |
| ---------------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startBurst_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startBurst_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startBurst_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > startBurst > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_runParameters_anyOf_i0_startBurst_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > startBurst > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_runParameters_anyOf_i0_restartInterval"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > restartInterval`

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

| Any of(Option)                                                                                |
| --------------------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_restartInterval_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_runParameters_anyOf_i0_restartInterval_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_runParameters_anyOf_i0_restartInterval_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > restartInterval > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

###### <a name="items_items_configuration_anyOf_i0_runParameters_anyOf_i0_restartInterval_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > AosRunParameters > restartInterval > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_runParameters_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > runParameters > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_offlineTTL"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > offlineTTL`

**Title:** Offlinettl

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:**     TTL (allowed time) to run service when unit in offline mode.
    If value is absent service will live on an unit forever.
    Format: ISO8601 duration.

**Examples:**

```json
"PT1M"
```

```json
"PT7D"
```

| Any of(Option)                                                    |
| ----------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_offlineTTL_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_offlineTTL_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_offlineTTL_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > offlineTTL > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

###### <a name="items_items_configuration_anyOf_i0_offlineTTL_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > offlineTTL > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_resources"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > resources`

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

| Any of(Option)                                                   |
| ---------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_resources_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_resources_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_resources_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > resources > anyOf > item 0`

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

| Each item of this array must be                                                   | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [AosResourceAccess](#items_items_configuration_anyOf_i0_resources_anyOf_i0_items) | -           |

###### <a name="items_items_configuration_anyOf_i0_resources_anyOf_i0_items"></a>AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > resources > anyOf > item 0 > AosResourceAccess

**Title:** AosResourceAccess

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosResourceAccess                                                   |

| Property                                                                     | Pattern | Type             | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [name](#items_items_configuration_anyOf_i0_resources_anyOf_i0_items_name ) | No      | string           | No         | -          | Name              |
| - [mode](#items_items_configuration_anyOf_i0_resources_anyOf_i0_items_mode ) | No      | enum (of string) | No         | -          | Mode              |

###### <a name="items_items_configuration_anyOf_i0_resources_anyOf_i0_items_name"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > resources > anyOf > item 0 > AosResourceAccess > name`

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

###### <a name="items_items_configuration_anyOf_i0_resources_anyOf_i0_items_mode"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > resources > anyOf > item 0 > AosResourceAccess > mode`

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

###### <a name="items_items_configuration_anyOf_i0_resources_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > resources > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_allowedConnections"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > allowedConnections`

**Title:** Allowedconnections

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:**     List of allowed network connections.
    Format of connection string: {fqdn}/[port|port_range]/[tcp|udp]

**Examples:**

```json
"hello-world/8087:8088/tcp"
```

```json
"hello-world/1515/udp"
```

| Any of(Option)                                                            |
| ------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_allowedConnections_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_allowedConnections_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_allowedConnections_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > allowedConnections > anyOf > item 0`

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

| Each item of this array must be                                                       | Description |
| ------------------------------------------------------------------------------------- | ----------- |
| [item 0 items](#items_items_configuration_anyOf_i0_allowedConnections_anyOf_i0_items) | -           |

###### <a name="items_items_configuration_anyOf_i0_allowedConnections_anyOf_i0_items"></a>AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > allowedConnections > anyOf > item 0 > item 0 items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="items_items_configuration_anyOf_i0_allowedConnections_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > allowedConnections > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_quotas"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Quotas for the service.

| Any of(Option)                                                   |
| ---------------------------------------------------------------- |
| [AosQuotas](#items_items_configuration_anyOf_i0_quotas_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_quotas_anyOf_i1)    |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas`

**Title:** AosQuotas

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosQuotas                                                           |

**Description:** Schema for possible quotas for an Aos item.

| Property                                                                              | Pattern | Type        | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [cpuLimit](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_cpuLimit )           | No      | Combination | No         | -          | Cpulimit          |
| - [ramLimit](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_ramLimit )           | No      | Combination | No         | -          | Ramlimit          |
| - [storageLimit](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_storageLimit )   | No      | Combination | No         | -          | Storagelimit      |
| - [stateLimit](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_stateLimit )       | No      | Combination | No         | -          | Statelimit        |
| - [tmpLimit](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_tmpLimit )           | No      | Combination | No         | -          | Tmplimit          |
| - [uploadSpeed](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_uploadSpeed )     | No      | Combination | No         | -          | Uploadspeed       |
| - [downloadSpeed](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_downloadSpeed ) | No      | Combination | No         | -          | Downloadspeed     |
| - [noFileLimit](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_noFileLimit )     | No      | Combination | No         | -          | Nofilelimit       |
| - [pidsLimit](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_pidsLimit )         | No      | Combination | No         | -          | Pidslimit         |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_cpuLimit"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > cpuLimit`

**Title:** Cpulimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** CPU limit in DMIPs

| Any of(Option)                                                                  |
| ------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_cpuLimit_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_cpuLimit_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_cpuLimit_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > cpuLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_cpuLimit_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > cpuLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_ramLimit"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > ramLimit`

**Title:** Ramlimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** RAM limit in bytes

| Any of(Option)                                                                  |
| ------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_ramLimit_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_ramLimit_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_ramLimit_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > ramLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_ramLimit_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > ramLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_storageLimit"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > storageLimit`

**Title:** Storagelimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Storage limit in bytes

| Any of(Option)                                                                      |
| ----------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_storageLimit_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_storageLimit_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_storageLimit_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > storageLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_storageLimit_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > storageLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_stateLimit"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > stateLimit`

**Title:** Statelimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** State limit in bytes

| Any of(Option)                                                                    |
| --------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_stateLimit_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_stateLimit_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_stateLimit_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > stateLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_stateLimit_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > stateLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_tmpLimit"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > tmpLimit`

**Title:** Tmplimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Temporary storage limit in bytes

| Any of(Option)                                                                  |
| ------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_tmpLimit_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_tmpLimit_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_tmpLimit_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > tmpLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_tmpLimit_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > tmpLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_uploadSpeed"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > uploadSpeed`

**Title:** Uploadspeed

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Upload limit in bits per second

| Any of(Option)                                                                     |
| ---------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_uploadSpeed_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_uploadSpeed_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_uploadSpeed_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > uploadSpeed > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_uploadSpeed_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > uploadSpeed > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_downloadSpeed"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > downloadSpeed`

**Title:** Downloadspeed

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Upload limit in bits per second

| Any of(Option)                                                                       |
| ------------------------------------------------------------------------------------ |
| [item 0](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_downloadSpeed_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_downloadSpeed_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_downloadSpeed_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > downloadSpeed > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_downloadSpeed_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > downloadSpeed > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_noFileLimit"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > noFileLimit`

**Title:** Nofilelimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Limit of opened files

| Any of(Option)                                                                     |
| ---------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_noFileLimit_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_noFileLimit_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_noFileLimit_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > noFileLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_noFileLimit_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > noFileLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_pidsLimit"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > pidsLimit`

**Title:** Pidslimit

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Limit of PIDs

| Any of(Option)                                                                   |
| -------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_pidsLimit_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_quotas_anyOf_i0_pidsLimit_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_pidsLimit_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > pidsLimit > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i0_pidsLimit_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > AosQuotas > pidsLimit > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_quotas_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > quotas > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_alertRules"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Alert rules for the service.

| Any of(Option)                                                           |
| ------------------------------------------------------------------------ |
| [AosAlertRules](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_alertRules_anyOf_i1)        |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules`

**Title:** AosAlertRules

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertRules                                                       |

**Description:** Schema for all possible alert rules.

| Property                                                                        | Pattern | Type        | Deprecated | Definition | Title/Description        |
| ------------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ------------------------ |
| - [ram](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram )           | No      | Combination | No         | -          | RAM alert settings.      |
| - [cpu](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_cpu )           | No      | Combination | No         | -          | CPU alert settings.      |
| - [storage](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_storage )   | No      | Combination | No         | -          | Storage alert settings.  |
| - [upload](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload )     | No      | Combination | No         | -          | Upload alert settings.   |
| - [download](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_download ) | No      | Combination | No         | -          | Download alert settings. |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** RAM alert settings.

| Any of(Option)                                                                               |
| -------------------------------------------------------------------------------------------- |
| [AosAlertRulePercents](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i1)               |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents`

**Title:** AosAlertRulePercents

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertRulePercents                                                |

**Description:** Schema alert triggering procedure in percents.

| Property                                                                                             | Pattern | Type        | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [minTimeout](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minTimeout )     | No      | Combination | No         | -          | Mintimeout        |
| + [minThreshold](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minThreshold ) | No      | Combination | No         | -          | Minthreshold      |
| + [maxThreshold](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold ) | No      | Combination | No         | -          | Maxthreshold      |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minTimeout"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minTimeout`

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

| Any of(Option)                                                                                     |
| -------------------------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minTimeout > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minTimeout_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minTimeout > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minThreshold"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minThreshold`

**Title:** Minthreshold

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** The minimum threshold to stop alert.

| Any of(Option)                                                                                       |
| ---------------------------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minThreshold > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `number` |

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 100 |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_minThreshold_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > minThreshold > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > maxThreshold`

**Title:** Maxthreshold

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** The maximum threshold value to start alert.

| Any of(Option)                                                                                       |
| ---------------------------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > maxThreshold > anyOf > item 0`

|          |          |
| -------- | -------- |
| **Type** | `number` |

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 100 |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0_maxThreshold_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > AosAlertRulePercents > maxThreshold > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > ram > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_cpu"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > cpu`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** CPU alert settings.

| Any of(Option)                                                                               |
| -------------------------------------------------------------------------------------------- |
| [AosAlertRulePercents](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_cpu_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_cpu_anyOf_i1)               |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_cpu_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > cpu > anyOf > AosAlertRulePercents`

**Title:** AosAlertRulePercents

|                           |                                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                     |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)                  |
| **Same definition as**    | [AosAlertRulePercents](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0) |

**Description:** Schema alert triggering procedure in percents.

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_cpu_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > cpu > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_storage"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > storage`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Storage alert settings.

| Any of(Option)                                                                                   |
| ------------------------------------------------------------------------------------------------ |
| [AosAlertRulePercents](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_storage_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_storage_anyOf_i1)               |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_storage_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > storage > anyOf > AosAlertRulePercents`

**Title:** AosAlertRulePercents

|                           |                                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                     |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)                  |
| **Same definition as**    | [AosAlertRulePercents](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_ram_anyOf_i0) |

**Description:** Schema alert triggering procedure in percents.

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_storage_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > storage > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Upload alert settings.

| Any of(Option)                                                                                |
| --------------------------------------------------------------------------------------------- |
| [AosAlertRulePoints](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i1)             |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints`

**Title:** AosAlertRulePoints

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosAlertRulePoints                                                  |

**Description:** Schema alert triggering procedure.

| Property                                                                                                | Pattern | Type        | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [minTimeout](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minTimeout )     | No      | Combination | No         | -          | Mintimeout        |
| + [minThreshold](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minThreshold ) | No      | Combination | No         | -          | Minthreshold      |
| + [maxThreshold](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold ) | No      | Combination | No         | -          | Maxthreshold      |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minTimeout"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minTimeout`

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

| Any of(Option)                                                                                        |
| ----------------------------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minTimeout > anyOf > item 0`

|            |            |
| ---------- | ---------- |
| **Type**   | `string`   |
| **Format** | `duration` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minTimeout_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minTimeout > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minThreshold"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minThreshold`

**Title:** Minthreshold

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** The minimum threshold to stop alert.

| Any of(Option)                                                                                          |
| ------------------------------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minThreshold > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_minThreshold_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > minThreshold > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > maxThreshold`

**Title:** Maxthreshold

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** The maximum threshold value to start alert.

| Any of(Option)                                                                                          |
| ------------------------------------------------------------------------------------------------------- |
| [item 0](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > maxThreshold > anyOf > item 0`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0_maxThreshold_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > AosAlertRulePoints > maxThreshold > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > upload > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_download"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > download`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Download alert settings.

| Any of(Option)                                                                                  |
| ----------------------------------------------------------------------------------------------- |
| [AosAlertRulePoints](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_download_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_download_anyOf_i1)             |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_download_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > download > anyOf > AosAlertRulePoints`

**Title:** AosAlertRulePoints

|                           |                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                      |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)                   |
| **Same definition as**    | [AosAlertRulePoints](#items_items_configuration_anyOf_i0_alertRules_anyOf_i0_upload_anyOf_i0) |

**Description:** Schema alert triggering procedure.

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i0_download_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > AosAlertRules > download > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_alertRules_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > alertRules > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

###### <a name="items_items_configuration_anyOf_i0_permissions"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > permissions`

**Title:** Permissions

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** Permissions to access resources.

**Example:**

```json
{
    "vis": {
        "Attributes.Vehicle.Vin": "r",
        "Signal.Doors.*": "rw"
    }
}
```

| Any of(Option)                                                     |
| ------------------------------------------------------------------ |
| [item 0](#items_items_configuration_anyOf_i0_permissions_anyOf_i0) |
| [item 1](#items_items_configuration_anyOf_i0_permissions_anyOf_i1) |

###### <a name="items_items_configuration_anyOf_i0_permissions_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > permissions > anyOf > item 0`

|                           |                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                             |
| **Additional properties** | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#items_items_configuration_anyOf_i0_permissions_anyOf_i0_additionalProperties) |

| Property                                                                             | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| - [](#items_items_configuration_anyOf_i0_permissions_anyOf_i0_additionalProperties ) | No      | object | No         | -          | -                 |

###### <a name="items_items_configuration_anyOf_i0_permissions_anyOf_i0_additionalProperties"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > permissions > anyOf > item 0 > additionalProperties`

|                           |                                                                                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                                  |
| **Additional properties** | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#items_items_configuration_anyOf_i0_permissions_anyOf_i0_additionalProperties_additionalProperties) |

| Property                                                                                                  | Pattern | Type             | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| - [](#items_items_configuration_anyOf_i0_permissions_anyOf_i0_additionalProperties_additionalProperties ) | No      | enum (of string) | No         | -          | -                 |

###### <a name="items_items_configuration_anyOf_i0_permissions_anyOf_i0_additionalProperties_additionalProperties"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > permissions > anyOf > item 0 > additionalProperties > additionalProperties`

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

Must be one of:
* "r"
* "rw"
* "w"

###### <a name="items_items_configuration_anyOf_i0_permissions_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > AosUpdateItemConfiguration > permissions > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="items_items_configuration_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > configuration > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

#### <a name="items_items_dependencies"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies`

**Title:** Dependencies

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** List of the update item dependencies.

| Any of(Option)                               |
| -------------------------------------------- |
| [item 0](#items_items_dependencies_anyOf_i0) |
| [item 1](#items_items_dependencies_anyOf_i1) |

##### <a name="items_items_dependencies_anyOf_i0"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 0`

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

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [AosDependency](#items_items_dependencies_anyOf_i0_items) | -           |

###### <a name="items_items_dependencies_anyOf_i0_items"></a>AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 0 > AosDependency

**Title:** AosDependency

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosDependency                                                       |

| Property                                                                           | Pattern | Type             | Deprecated | Definition                                 | Title/Description |
| ---------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------------------ | ----------------- |
| + [identity](#items_items_dependencies_anyOf_i0_items_identity )                   | No      | object           | No         | Same as [identity](#items_items_identity ) | AosIdentity       |
| + [versions](#items_items_dependencies_anyOf_i0_items_versions )                   | No      | string           | No         | -                                          | Versions          |
| - [includePreRelease](#items_items_dependencies_anyOf_i0_items_includePreRelease ) | No      | boolean          | No         | -                                          | Includeprerelease |
| - [condition](#items_items_dependencies_anyOf_i0_items_condition )                 | No      | enum (of string) | No         | -                                          | Condition         |

###### <a name="items_items_dependencies_anyOf_i0_items_identity"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 0 > AosDependency > identity`

**Title:** AosIdentity

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Same definition as**    | [identity](#items_items_identity)                                           |

**Description:** Identity of the AOS object.

###### <a name="items_items_dependencies_anyOf_i0_items_versions"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 0 > AosDependency > versions`

**Title:** Versions

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Versions of the AOS object.

**Examples:**

```json
">=1.0.0,<2.0.0"
```

```json
"1.2.3"
```

###### <a name="items_items_dependencies_anyOf_i0_items_includePreRelease"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 0 > AosDependency > includePreRelease`

**Title:** Includeprerelease

|             |           |
| ----------- | --------- |
| **Type**    | `boolean` |
| **Default** | `false`   |

**Description:** Include pre-release versions.

###### <a name="items_items_dependencies_anyOf_i0_items_condition"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 0 > AosDependency > condition`

**Title:** Condition

|             |                    |
| ----------- | ------------------ |
| **Type**    | `enum (of string)` |
| **Default** | `"completed"`      |

**Description:** Condition for dependency of the AOS object.

Must be one of:
* "started"
* "healthy"
* "completed"
* "before"
* "after"

##### <a name="items_items_dependencies_anyOf_i1"></a>Property `AosUploadMetaConfig > items > AosUpdateItem > dependencies > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-11-26 at 15:47:18 +0200
