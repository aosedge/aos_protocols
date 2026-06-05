# UnitConfig

- [![Required](https://img.shields.io/badge/Required-blue) Property `UnitConfig > version`](#version)
- [![Required](https://img.shields.io/badge/Required-blue) Property `UnitConfig > formatVersion`](#formatVersion)
- [![Required](https://img.shields.io/badge/Required-blue) Property `UnitConfig > nodes`](#nodes)
  - [UnitConfig > nodes > NodeConfig](#nodes_items)
    - [Property `UnitConfig > nodes > NodeConfig > nodeType`](#nodes_items_nodeType)
    - [Property `UnitConfig > nodes > NodeConfig > nodeId`](#nodes_items_nodeId)
    - [Property `UnitConfig > nodes > NodeConfig > alertRules`](#nodes_items_alertRules)
      - [Property `UnitConfig > nodes > NodeConfig > alertRules > cpu`](#nodes_items_alertRules_cpu)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > cpu > minThreshold`](#nodes_items_alertRules_cpu_minThreshold)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > cpu > maxThreshold`](#nodes_items_alertRules_cpu_maxThreshold)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > cpu > minTimeout`](#nodes_items_alertRules_cpu_minTimeout)
      - [Property `UnitConfig > nodes > NodeConfig > alertRules > ram`](#nodes_items_alertRules_ram)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > cpu > minThreshold`](#nodes_items_alertRules_cpu_minThreshold)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > cpu > maxThreshold`](#nodes_items_alertRules_cpu_maxThreshold)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > cpu > minTimeout`](#nodes_items_alertRules_cpu_minTimeout)
      - [Property `UnitConfig > nodes > NodeConfig > alertRules > partitions`](#nodes_items_alertRules_partitions)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0`](#nodes_items_alertRules_partitions_anyOf_i0)
          - [UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk](#nodes_items_alertRules_partitions_anyOf_i0_items)
            - [Property `UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > minThreshold`](#nodes_items_alertRules_partitions_anyOf_i0_items_minThreshold)
            - [Property `UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > maxThreshold`](#nodes_items_alertRules_partitions_anyOf_i0_items_maxThreshold)
            - [Property `UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > minTimeout`](#nodes_items_alertRules_partitions_anyOf_i0_items_minTimeout)
            - [Property `UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > name`](#nodes_items_alertRules_partitions_anyOf_i0_items_name)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 1`](#nodes_items_alertRules_partitions_anyOf_i1)
      - [Property `UnitConfig > nodes > NodeConfig > alertRules > download`](#nodes_items_alertRules_download)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > download > minThreshold`](#nodes_items_alertRules_download_minThreshold)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > download > maxThreshold`](#nodes_items_alertRules_download_maxThreshold)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > download > minTimeout`](#nodes_items_alertRules_download_minTimeout)
      - [Property `UnitConfig > nodes > NodeConfig > alertRules > upload`](#nodes_items_alertRules_upload)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > download > minThreshold`](#nodes_items_alertRules_download_minThreshold)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > download > maxThreshold`](#nodes_items_alertRules_download_maxThreshold)
        - [Property `UnitConfig > nodes > NodeConfig > alertRules > download > minTimeout`](#nodes_items_alertRules_download_minTimeout)
    - [Property `UnitConfig > nodes > NodeConfig > resourceRatios`](#nodes_items_resourceRatios)
      - [Property `UnitConfig > nodes > NodeConfig > resourceRatios > cpu`](#nodes_items_resourceRatios_cpu)
      - [Property `UnitConfig > nodes > NodeConfig > resourceRatios > ram`](#nodes_items_resourceRatios_ram)
      - [Property `UnitConfig > nodes > NodeConfig > resourceRatios > storage`](#nodes_items_resourceRatios_storage)
      - [Property `UnitConfig > nodes > NodeConfig > resourceRatios > state`](#nodes_items_resourceRatios_state)
    - [Property `UnitConfig > nodes > NodeConfig > devices`](#nodes_items_devices)
      - [UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo](#nodes_items_devices_items)
        - [Property `UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo > name`](#nodes_items_devices_items_name)
        - [Property `UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo > hostDevices`](#nodes_items_devices_items_hostDevices)
          - [UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo > hostDevices > hostDevices items](#nodes_items_devices_items_hostDevices_items)
        - [Property `UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo > sharedCount`](#nodes_items_devices_items_sharedCount)
        - [Property `UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo > groups`](#nodes_items_devices_items_groups)
          - [UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo > groups > groups items](#nodes_items_devices_items_groups_items)
    - [Property `UnitConfig > nodes > NodeConfig > resources`](#nodes_items_resources)
      - [UnitConfig > nodes > NodeConfig > resources > ResourceInfo](#nodes_items_resources_items)
        - [Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > name`](#nodes_items_resources_items_name)
        - [Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > groups`](#nodes_items_resources_items_groups)
          - [UnitConfig > nodes > NodeConfig > resources > ResourceInfo > groups > groups items](#nodes_items_resources_items_groups_items)
        - [Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts`](#nodes_items_resources_items_mounts)
          - [UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount](#nodes_items_resources_items_mounts_items)
            - [Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > destination`](#nodes_items_resources_items_mounts_items_destination)
            - [Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > source`](#nodes_items_resources_items_mounts_items_source)
            - [Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > type`](#nodes_items_resources_items_mounts_items_type)
            - [Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > options`](#nodes_items_resources_items_mounts_items_options)
              - [UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > options > options items](#nodes_items_resources_items_mounts_items_options_items)
        - [Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > envs`](#nodes_items_resources_items_envs)
          - [UnitConfig > nodes > NodeConfig > resources > ResourceInfo > envs > envs items](#nodes_items_resources_items_envs_items)
        - [Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts`](#nodes_items_resources_items_hosts)
          - [UnitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts > AosHostRecord](#nodes_items_resources_items_hosts_items)
            - [Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts > AosHostRecord > ip`](#nodes_items_resources_items_hosts_items_ip)
            - [Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts > AosHostRecord > hostname`](#nodes_items_resources_items_hosts_items_hostname)
    - [Property `UnitConfig > nodes > NodeConfig > labels`](#nodes_items_labels)
      - [UnitConfig > nodes > NodeConfig > labels > labels items](#nodes_items_labels_items)
    - [Property `UnitConfig > nodes > NodeConfig > priority`](#nodes_items_priority)

**Title:** UnitConfig

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

**Description:** Configuration parameters for a unit.

| Property                           | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [version](#version )             | No      | string | No         | -          | Version           |
| + [formatVersion](#formatVersion ) | No      | string | No         | -          | Format Version    |
| + [nodes](#nodes )                 | No      | array  | No         | -          | Nodes             |

## <a name="version"></a>![Required](https://img.shields.io/badge/Required-blue) Property `UnitConfig > version`

**Title:** Version

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Version identifies the configuration itself. It is automatically incremented with every configuration update.

## <a name="formatVersion"></a>![Required](https://img.shields.io/badge/Required-blue) Property `UnitConfig > formatVersion`

**Title:** Format Version

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** JSON format of the unit configuration may change over time. This field identifies current format of unit configuration. Cloud sets it automatically.

## <a name="nodes"></a>![Required](https://img.shields.io/badge/Required-blue) Property `UnitConfig > nodes`

**Title:** Nodes

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** The list of node configurations.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description                    |
| ------------------------------- | ------------------------------ |
| [NodeConfig](#nodes_items)      | Node configuration parameters. |

### <a name="nodes_items"></a>UnitConfig > nodes > NodeConfig

**Title:** NodeConfig

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/NodeConfig                                                          |

**Description:** Node configuration parameters.

| Property                                         | Pattern | Type            | Deprecated | Definition                    | Title/Description  |
| ------------------------------------------------ | ------- | --------------- | ---------- | ----------------------------- | ------------------ |
| + [nodeType](#nodes_items_nodeType )             | No      | string          | No         | -                             | Node type          |
| - [nodeId](#nodes_items_nodeId )                 | No      | string          | No         | -                             | Nodeid             |
| - [alertRules](#nodes_items_alertRules )         | No      | object          | No         | In #/$defs/AlertRules         | Alert Rules        |
| - [resourceRatios](#nodes_items_resourceRatios ) | No      | object          | No         | In #/$defs/ResourceRatiosInfo | ResourceRatiosInfo |
| - [devices](#nodes_items_devices )               | No      | array           | No         | -                             | Devices            |
| - [resources](#nodes_items_resources )           | No      | array           | No         | -                             | Resources          |
| - [labels](#nodes_items_labels )                 | No      | array of string | No         | -                             | Labels             |
| + [priority](#nodes_items_priority )             | No      | integer         | No         | -                             | Priority           |

#### <a name="nodes_items_nodeType"></a>Property `UnitConfig > nodes > NodeConfig > nodeType`

**Title:** Node type

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The type of the node.

**Examples:**

```json
"DomA"
```

```json
"DomD"
```

#### <a name="nodes_items_nodeId"></a>Property `UnitConfig > nodes > NodeConfig > nodeId`

**Title:** Nodeid

|             |          |
| ----------- | -------- |
| **Type**    | `string` |
| **Default** | `null`   |

**Description:** Unique ID of the node

#### <a name="nodes_items_alertRules"></a>Property `UnitConfig > nodes > NodeConfig > alertRules`

**Title:** Alert Rules

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/AlertRules                                                          |

**Description:** The default thresholds for services running on the node.

| Property                                            | Pattern | Type        | Deprecated | Definition                   | Title/Description |
| --------------------------------------------------- | ------- | ----------- | ---------- | ---------------------------- | ----------------- |
| - [cpu](#nodes_items_alertRules_cpu )               | No      | object      | No         | In #/$defs/AlertRulePercents | AlertRulePercents |
| - [ram](#nodes_items_alertRules_ram )               | No      | object      | No         | In #/$defs/AlertRulePercents | AlertRulePercents |
| - [partitions](#nodes_items_alertRules_partitions ) | No      | Combination | No         | -                            | Partitions        |
| - [download](#nodes_items_alertRules_download )     | No      | object      | No         | In #/$defs/AlertRulePoints   | AlertRulePoints   |
| - [upload](#nodes_items_alertRules_upload )         | No      | object      | No         | In #/$defs/AlertRulePoints   | AlertRulePoints   |

##### <a name="nodes_items_alertRules_cpu"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > cpu`

**Title:** AlertRulePercents

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/AlertRulePercents                                                   |

**Description:** The CPU thresholds.

| Property                                                    | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [minThreshold](#nodes_items_alertRules_cpu_minThreshold ) | No      | number | No         | -          | Minthreshold      |
| + [maxThreshold](#nodes_items_alertRules_cpu_maxThreshold ) | No      | number | No         | -          | Maxthreshold      |
| + [minTimeout](#nodes_items_alertRules_cpu_minTimeout )     | No      | number | No         | -          | Mintimeout        |

###### <a name="nodes_items_alertRules_cpu_minThreshold"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > cpu > minThreshold`

**Title:** Minthreshold

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The lowest percents of a value after which resource can be rebalanced back.

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="nodes_items_alertRules_cpu_maxThreshold"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > cpu > maxThreshold`

**Title:** Maxthreshold

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The highest percents of a value after which resource have be rebalanced.

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="nodes_items_alertRules_cpu_minTimeout"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > cpu > minTimeout`

**Title:** Mintimeout

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The timeout in seconds. Fraction of value specifies milliseconds

**Examples:**

```json
0.5
```

```json
100
```

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |

##### <a name="nodes_items_alertRules_ram"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > ram`

**Title:** AlertRulePercents

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/AlertRulePercents                                                   |

**Description:** The RAM thresholds.

| Property                                                    | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [minThreshold](#nodes_items_alertRules_cpu_minThreshold ) | No      | number | No         | -          | Minthreshold      |
| + [maxThreshold](#nodes_items_alertRules_cpu_maxThreshold ) | No      | number | No         | -          | Maxthreshold      |
| + [minTimeout](#nodes_items_alertRules_cpu_minTimeout )     | No      | number | No         | -          | Mintimeout        |

###### <a name="nodes_items_alertRules_cpu_minThreshold"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > cpu > minThreshold`

**Title:** Minthreshold

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The lowest percents of a value after which resource can be rebalanced back.

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="nodes_items_alertRules_cpu_maxThreshold"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > cpu > maxThreshold`

**Title:** Maxthreshold

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The highest percents of a value after which resource have be rebalanced.

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="nodes_items_alertRules_cpu_minTimeout"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > cpu > minTimeout`

**Title:** Mintimeout

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The timeout in seconds. Fraction of value specifies milliseconds

**Examples:**

```json
0.5
```

```json
100
```

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |

##### <a name="nodes_items_alertRules_partitions"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > partitions`

**Title:** Partitions

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |

**Description:** The list of thresholds partitions.

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [item 0](#nodes_items_alertRules_partitions_anyOf_i0) |
| [item 1](#nodes_items_alertRules_partitions_anyOf_i1) |

###### <a name="nodes_items_alertRules_partitions_anyOf_i0"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0`

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

| Each item of this array must be                                              | Description                                          |
| ---------------------------------------------------------------------------- | ---------------------------------------------------- |
| [AlertRulePercentsOfDisk](#nodes_items_alertRules_partitions_anyOf_i0_items) | Information about the threshold for disk with names. |

###### <a name="nodes_items_alertRules_partitions_anyOf_i0_items"></a>UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk

**Title:** AlertRulePercentsOfDisk

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AlertRulePercentsOfDisk                                             |

**Description:** Information about the threshold for disk with names.

| Property                                                                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [minThreshold](#nodes_items_alertRules_partitions_anyOf_i0_items_minThreshold ) | No      | number | No         | -          | Minthreshold      |
| + [maxThreshold](#nodes_items_alertRules_partitions_anyOf_i0_items_maxThreshold ) | No      | number | No         | -          | Maxthreshold      |
| + [minTimeout](#nodes_items_alertRules_partitions_anyOf_i0_items_minTimeout )     | No      | number | No         | -          | Mintimeout        |
| + [name](#nodes_items_alertRules_partitions_anyOf_i0_items_name )                 | No      | string | No         | -          | Name of partition |

###### <a name="nodes_items_alertRules_partitions_anyOf_i0_items_minThreshold"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > minThreshold`

**Title:** Minthreshold

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The lowest percents of a value after which resource can be rebalanced back.

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="nodes_items_alertRules_partitions_anyOf_i0_items_maxThreshold"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > maxThreshold`

**Title:** Maxthreshold

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The highest percents of a value after which resource have be rebalanced.

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |
| **Maximum**  | N/A |

###### <a name="nodes_items_alertRules_partitions_anyOf_i0_items_minTimeout"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > minTimeout`

**Title:** Mintimeout

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The timeout in seconds. Fraction of value specifies milliseconds

**Examples:**

```json
0.5
```

```json
100
```

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |

###### <a name="nodes_items_alertRules_partitions_anyOf_i0_items_name"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 0 > AlertRulePercentsOfDisk > name`

**Title:** Name of partition

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="nodes_items_alertRules_partitions_anyOf_i1"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > partitions > anyOf > item 1`

|          |        |
| -------- | ------ |
| **Type** | `null` |

##### <a name="nodes_items_alertRules_download"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > download`

**Title:** AlertRulePoints

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/AlertRulePoints                                                     |

**Description:** Alert rules for incoming network traffic(in bytes).

| Property                                                         | Pattern | Type    | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [minThreshold](#nodes_items_alertRules_download_minThreshold ) | No      | integer | No         | -          | Minthreshold      |
| + [maxThreshold](#nodes_items_alertRules_download_maxThreshold ) | No      | integer | No         | -          | Maxthreshold      |
| + [minTimeout](#nodes_items_alertRules_download_minTimeout )     | No      | number  | No         | -          | Mintimeout        |

###### <a name="nodes_items_alertRules_download_minThreshold"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > download > minThreshold`

**Title:** Minthreshold

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** The lowest points (DMIPs, Bytes, etc) of a value after which resource can be rebalanced back.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="nodes_items_alertRules_download_maxThreshold"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > download > maxThreshold`

**Title:** Maxthreshold

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** The highest points of a value after which resource have be rebalanced.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="nodes_items_alertRules_download_minTimeout"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > download > minTimeout`

**Title:** Mintimeout

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The timeout in seconds. Fraction of value specifies milliseconds

**Examples:**

```json
0.5
```

```json
100
```

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |

##### <a name="nodes_items_alertRules_upload"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > upload`

**Title:** AlertRulePoints

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/AlertRulePoints                                                     |

**Description:** Alert rules for outgoing network traffic(in bytes).

| Property                                                         | Pattern | Type    | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [minThreshold](#nodes_items_alertRules_download_minThreshold ) | No      | integer | No         | -          | Minthreshold      |
| + [maxThreshold](#nodes_items_alertRules_download_maxThreshold ) | No      | integer | No         | -          | Maxthreshold      |
| + [minTimeout](#nodes_items_alertRules_download_minTimeout )     | No      | number  | No         | -          | Mintimeout        |

###### <a name="nodes_items_alertRules_download_minThreshold"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > download > minThreshold`

**Title:** Minthreshold

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** The lowest points (DMIPs, Bytes, etc) of a value after which resource can be rebalanced back.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="nodes_items_alertRules_download_maxThreshold"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > download > maxThreshold`

**Title:** Maxthreshold

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** The highest points of a value after which resource have be rebalanced.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="nodes_items_alertRules_download_minTimeout"></a>Property `UnitConfig > nodes > NodeConfig > alertRules > download > minTimeout`

**Title:** Mintimeout

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The timeout in seconds. Fraction of value specifies milliseconds

**Examples:**

```json
0.5
```

```json
100
```

| Restrictions |     |
| ------------ | --- |
| **Minimum**  | N/A |

#### <a name="nodes_items_resourceRatios"></a>Property `UnitConfig > nodes > NodeConfig > resourceRatios`

**Title:** ResourceRatiosInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Default**               | `null`                                                                      |
| **Defined in**            | #/$defs/ResourceRatiosInfo                                                  |

**Description:** The default resource ratio allocated for a service.

| Property                                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [cpu](#nodes_items_resourceRatios_cpu )         | No      | number | No         | -          | Cpu               |
| - [ram](#nodes_items_resourceRatios_ram )         | No      | number | No         | -          | Ram               |
| - [storage](#nodes_items_resourceRatios_storage ) | No      | number | No         | -          | Storage           |
| - [state](#nodes_items_resourceRatios_state )     | No      | number | No         | -          | State             |

##### <a name="nodes_items_resourceRatios_cpu"></a>Property `UnitConfig > nodes > NodeConfig > resourceRatios > cpu`

**Title:** Cpu

|             |          |
| ----------- | -------- |
| **Type**    | `number` |
| **Default** | `null`   |

**Description:** The CPU ratio in percent.

##### <a name="nodes_items_resourceRatios_ram"></a>Property `UnitConfig > nodes > NodeConfig > resourceRatios > ram`

**Title:** Ram

|             |          |
| ----------- | -------- |
| **Type**    | `number` |
| **Default** | `null`   |

**Description:** The memory (RAM) ratio in percent.

##### <a name="nodes_items_resourceRatios_storage"></a>Property `UnitConfig > nodes > NodeConfig > resourceRatios > storage`

**Title:** Storage

|             |          |
| ----------- | -------- |
| **Type**    | `number` |
| **Default** | `null`   |

**Description:** The storage ratio in percent.

##### <a name="nodes_items_resourceRatios_state"></a>Property `UnitConfig > nodes > NodeConfig > resourceRatios > state`

**Title:** State

|             |          |
| ----------- | -------- |
| **Type**    | `number` |
| **Default** | `null`   |

**Description:** Requested size of the "state" partition (in percents of its capacity).

#### <a name="nodes_items_devices"></a>Property `UnitConfig > nodes > NodeConfig > devices`

**Title:** Devices

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** The device list available for running services.

**Examples:**

```json
"Name=\"camera\", host_devices=[\"/dev/camera\"]"
```

```json
"Name=\"pulseaudio\", host_devices=[\"/dev/pulseaudio\"]"
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [AosDeviceInfo](#nodes_items_devices_items) | -           |

##### <a name="nodes_items_devices_items"></a>UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo

**Title:** AosDeviceInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosDeviceInfo                                                       |

| Property                                                 | Pattern | Type            | Deprecated | Definition | Title/Description |
| -------------------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| + [name](#nodes_items_devices_items_name )               | No      | string          | No         | -          | Name              |
| + [hostDevices](#nodes_items_devices_items_hostDevices ) | No      | array of string | No         | -          | Hostdevices       |
| - [sharedCount](#nodes_items_devices_items_sharedCount ) | No      | integer         | No         | -          | Sharedcount       |
| - [groups](#nodes_items_devices_items_groups )           | No      | array of string | No         | -          | Groups            |

###### <a name="nodes_items_devices_items_name"></a>Property `UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo > name`

**Title:** Name

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Name of the device.

###### <a name="nodes_items_devices_items_hostDevices"></a>Property `UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo > hostDevices`

**Title:** Hostdevices

|          |                   |
| -------- | ----------------- |
| **Type** | `array of string` |

**Description:** List of host devices.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                   | Description |
| ----------------------------------------------------------------- | ----------- |
| [hostDevices items](#nodes_items_devices_items_hostDevices_items) | -           |

###### <a name="nodes_items_devices_items_hostDevices_items"></a>UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo > hostDevices > hostDevices items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="nodes_items_devices_items_sharedCount"></a>Property `UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo > sharedCount`

**Title:** Sharedcount

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `0`       |

**Description:** The count of shared devices that can be used in one time. 0 means no restrictions.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="nodes_items_devices_items_groups"></a>Property `UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo > groups`

**Title:** Groups

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `null`            |

**Description:** List of associated groups.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                         | Description |
| ------------------------------------------------------- | ----------- |
| [groups items](#nodes_items_devices_items_groups_items) | -           |

###### <a name="nodes_items_devices_items_groups_items"></a>UnitConfig > nodes > NodeConfig > devices > AosDeviceInfo > groups > groups items

|          |          |
| -------- | -------- |
| **Type** | `string` |

#### <a name="nodes_items_resources"></a>Property `UnitConfig > nodes > NodeConfig > resources`

**Title:** Resources

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** Available resources for services.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [ResourceInfo](#nodes_items_resources_items) | -           |

##### <a name="nodes_items_resources_items"></a>UnitConfig > nodes > NodeConfig > resources > ResourceInfo

**Title:** ResourceInfo

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/ResourceInfo                                                        |

| Property                                         | Pattern | Type            | Deprecated | Definition | Title/Description |
| ------------------------------------------------ | ------- | --------------- | ---------- | ---------- | ----------------- |
| + [name](#nodes_items_resources_items_name )     | No      | string          | No         | -          | Name              |
| - [groups](#nodes_items_resources_items_groups ) | No      | array of string | No         | -          | Groups            |
| - [mounts](#nodes_items_resources_items_mounts ) | No      | array           | No         | -          | Mounts            |
| - [envs](#nodes_items_resources_items_envs )     | No      | array of string | No         | -          | Envs              |
| - [hosts](#nodes_items_resources_items_hosts )   | No      | array           | No         | -          | Hosts             |

###### <a name="nodes_items_resources_items_name"></a>Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > name`

**Title:** Name

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The name of the resource.

###### <a name="nodes_items_resources_items_groups"></a>Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > groups`

**Title:** Groups

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `null`            |

**Description:** The group names for the resource.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [groups items](#nodes_items_resources_items_groups_items) | -           |

###### <a name="nodes_items_resources_items_groups_items"></a>UnitConfig > nodes > NodeConfig > resources > ResourceInfo > groups > groups items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="nodes_items_resources_items_mounts"></a>Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts`

**Title:** Mounts

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** The mounts list available for running services.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                 | Description |
| --------------------------------------------------------------- | ----------- |
| [AosFileSystemMount](#nodes_items_resources_items_mounts_items) | -           |

###### <a name="nodes_items_resources_items_mounts_items"></a>UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount

**Title:** AosFileSystemMount

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosFileSystemMount                                                  |

| Property                                                                | Pattern | Type            | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| + [destination](#nodes_items_resources_items_mounts_items_destination ) | No      | string          | No         | -          | Destination       |
| - [source](#nodes_items_resources_items_mounts_items_source )           | No      | string          | No         | -          | Source            |
| - [type](#nodes_items_resources_items_mounts_items_type )               | No      | string          | No         | -          | Type              |
| - [options](#nodes_items_resources_items_mounts_items_options )         | No      | array of string | No         | -          | Options           |

###### <a name="nodes_items_resources_items_mounts_items_destination"></a>Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > destination`

**Title:** Destination

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The mount's destination.

###### <a name="nodes_items_resources_items_mounts_items_source"></a>Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > source`

**Title:** Source

|             |          |
| ----------- | -------- |
| **Type**    | `string` |
| **Default** | `null`   |

**Description:** The mount's source.

###### <a name="nodes_items_resources_items_mounts_items_type"></a>Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > type`

**Title:** Type

|             |          |
| ----------- | -------- |
| **Type**    | `string` |
| **Default** | `null`   |

**Description:** The mount's type.

###### <a name="nodes_items_resources_items_mounts_items_options"></a>Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > options`

**Title:** Options

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `null`            |

**Description:** The mount's options.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                          | Description |
| ------------------------------------------------------------------------ | ----------- |
| [options items](#nodes_items_resources_items_mounts_items_options_items) | -           |

###### <a name="nodes_items_resources_items_mounts_items_options_items"></a>UnitConfig > nodes > NodeConfig > resources > ResourceInfo > mounts > AosFileSystemMount > options > options items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="nodes_items_resources_items_envs"></a>Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > envs`

**Title:** Envs

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `null`            |

**Description:** The list of environment variables.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                       | Description |
| ----------------------------------------------------- | ----------- |
| [envs items](#nodes_items_resources_items_envs_items) | -           |

###### <a name="nodes_items_resources_items_envs_items"></a>UnitConfig > nodes > NodeConfig > resources > ResourceInfo > envs > envs items

|          |          |
| -------- | -------- |
| **Type** | `string` |

###### <a name="nodes_items_resources_items_hosts"></a>Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts`

**Title:** Hosts

|             |         |
| ----------- | ------- |
| **Type**    | `array` |
| **Default** | `null`  |

**Description:** The list of hostnames.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                           | Description |
| --------------------------------------------------------- | ----------- |
| [AosHostRecord](#nodes_items_resources_items_hosts_items) | -           |

###### <a name="nodes_items_resources_items_hosts_items"></a>UnitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts > AosHostRecord

**Title:** AosHostRecord

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |
| **Defined in**            | #/$defs/AosHostRecord                                                       |

| Property                                                         | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [ip](#nodes_items_resources_items_hosts_items_ip )             | No      | string | No         | -          | IP address        |
| + [hostname](#nodes_items_resources_items_hosts_items_hostname ) | No      | string | No         | -          | Hostname          |

###### <a name="nodes_items_resources_items_hosts_items_ip"></a>Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts > AosHostRecord > ip`

**Title:** IP address

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** IP address.

###### <a name="nodes_items_resources_items_hosts_items_hostname"></a>Property `UnitConfig > nodes > NodeConfig > resources > ResourceInfo > hosts > AosHostRecord > hostname`

**Title:** Hostname

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The hostname for the IP address.

#### <a name="nodes_items_labels"></a>Property `UnitConfig > nodes > NodeConfig > labels`

**Title:** Labels

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `null`            |

**Description:** The list of labels for this node.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be           | Description |
| ----------------------------------------- | ----------- |
| [labels items](#nodes_items_labels_items) | -           |

##### <a name="nodes_items_labels_items"></a>UnitConfig > nodes > NodeConfig > labels > labels items

|          |          |
| -------- | -------- |
| **Type** | `string` |

#### <a name="nodes_items_priority"></a>Property `UnitConfig > nodes > NodeConfig > priority`

**Title:** Priority

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** The priority of the node for deploying services.

| Restrictions |                 |
| ------------ | --------------- |
| **Minimum**  | &ge; 0          |
| **Maximum**  | &lt; 4294967295 |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2026-06-05 at 11:50:37 +0300
