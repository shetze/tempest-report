# Copyright (C) 2013 eNovance SAS <licensing@enovance.com>

# mapping of tests to openstack versions
name_mapping = {
    5: 'Essex',
    6: 'Folsom',
    7: 'Grizzly',
    8: 'Havana',
    9: 'Icehouse',
}

description_list = {
    # Levels:
    # 0: only basic discovery and readonly operations
    # 1: DEFAULT, feature discovery 
    # 2: more general tests
    # 3: scenario tests, long running
    # 5: ok, but not yet decided
    # 10: tests that failed devstack and need further investigation

    # Level 0: minimal tests that don't require an admin account, only for discovering
    'tempest.cli.simple_read_only.test_keystone:SimpleReadOnlyKeystoneClientTest.test_admin_discover': {'service': 'Identity Service (Keystone)', 'level': 0},
    'tempest.cli.simple_read_only.test_glance:SimpleReadOnlyGlanceClientTest.test_glance_image_list': {'service': 'Image Service (Glance)', 'level': 0},
    'tempest.cli.simple_read_only.test_nova_manage': {'service': 'Compute (Nova)', 'level': 0},
    'tempest.cli.simple_read_only.test_cinder:SimpleReadOnlyCinderClientTest.test_cinder_volumes_list': {'service': 'Volume Service (Cinder)', 'level': 0},
    'tempest.api.object_storage.test_container_services:ContainerTest.test_create_container': {'service': 'Object Storage (Swift)', 'level': 0},

    # Level 1 (default): service/extension discovery, used to make an educated guess about OpenStack release
    # Object Storage (Swift)
    'tempest.api.object_storage.test_container_quotas': {'service': 'Object Storage (Swift)', 'feature': 'Container Quota', 'release': 7, },
    'tempest.api.object_storage.test_object_version': {'service': 'Object Storage (Swift)', 'feature': 'Object versioning', 'release': 6, }, 
    'tempest.api.object_storage.test_object_temp_url:ObjectTempUrlTest.test_get_object_using_temp_url': {
        'service': 'Object Storage (Swift)', 'feature': 'Temporary object URL', 'release': 5},
    'tempest.api.object_storage.test_container_staticweb': {'service': 'Object Storage (Swift)', 'feature': 'Static Web', }, 
    'tempest.api.object_storage.test_container_services': {'service': 'Object Storage (Swift)'},
    'tempest.api.object_storage.test_container_sync': {'service': 'Object Storage (Swift)'},
    'tempest.api.object_storage.test_object_expiry': {'service': 'Object Storage (Swift)'},
    'tempest.thirdparty.boto.test_s3_buckets': {'service': 'Object Storage (Swift)', 'feature': 'S3 API' },

    'tempest_report.tempest_addons:GlanceV1Test': {'service': 'Image Service (Glance)', 'feature': 'V1 Api', }, 
    'tempest_report.tempest_addons:GlanceV2Test': {'service': 'Image Service (Glance)', 'feature': 'V2 Api', 'release': 6 },
 
    'tempest_report.tempest_addons:NovaExtensionTest.test_NMN': {'service': 'Compute (Nova)', 'feature': 'Multi-NIC Support', 'release': 5, },
    'tempest_report.tempest_addons:NovaExtensionTest.test_OS_EXT_STS': {'service': 'Compute (Nova)', 'feature': 'Extended Status support', 'release': 5, },
    'tempest_report.tempest_addons:NovaExtensionTest.test_user_data': {'service': 'Compute (Nova)', 'feature': 'User Data support', 'release': 6, },
    'tempest_report.tempest_addons:NovaExtensionTest.test_OS_DCF': {'service': 'Compute (Nova)', 'feature': 'Disk Management Extension', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_OS_EXT_AZ': {'service': 'Compute (Nova)', 'feature': 'Extended Server Attributes', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_OS_EXT_SRV_ATTR': {'service': 'Compute (Nova)', 'feature': 'Extended Server Attributes', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_assisted_volume_snapshots': {'service': 'Compute (Nova)', 'feature': 'Assisted volume snapshots', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_create_server_ext': {'service': 'Compute (Nova)', 'feature': 'Extended support to the Create Server v1.1 API', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_deferred_delete': {'service': 'Compute (Nova)', 'feature': 'Instance deferred delete', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_extended_volumes': {'service': 'Compute (Nova)', 'feature': 'Extended Volumes support', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_fixed_ips': {'service': 'Compute (Nova)', 'feature': 'Fixed IPs support', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_flavor_access': {'service': 'Compute (Nova)', 'feature': 'Flavor access support', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_floating_ip_dns': {'service': 'Compute (Nova)', 'feature': 'Floating IP DNS support', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_floating_ip_pools': {'service': 'Compute (Nova)', 'feature': 'Floating IPs support', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_floating_ips': {'service': 'Compute (Nova)', 'feature': 'Floating IPs support', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_rescue': {'service': 'Compute (Nova)', 'feature': 'Instance rescue mode', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_security_groups': {'service': 'Compute (Nova)', 'feature': 'Security group support', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_server_password': {'service': 'Compute (Nova)', 'feature': 'Server password support', 'release': 7},
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_shelve': {'service': 'Compute (Nova)', 'feature': 'Instance shelve mode', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_user_quotas': {'service': 'Compute (Nova)', 'feature': 'Project user quota support', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_virtual_interfaces': {'service': 'Compute (Nova)', 'feature': 'Virtual interface support', },
    'tempest_report.tempest_addons:NovaExtensionTest.test_os_volumes': {'service': 'Compute (Nova)', 'feature': 'Volumes support', },

    'tempest_report.tempest_addons:CinderExtensionTest.test_os_admin_actions': {'service': 'Volume Service (Cinder)', 'feature': 'Enable admin actions', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_os_availability_zone': {'service': 'Volume Service (Cinder)', 'feature': 'Describe Availability Zones', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_backups': {'service': 'Volume Service (Cinder)', 'feature': 'Backups support', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_os_image_create': {'service': 'Volume Service (Cinder)', 'feature': 'Allow creating a volume from an image in the Create Volume v1 API', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_os_extended_snapshot_attributes': {'service': 'Volume Service (Cinder)', 'feature': 'Extended SnapshotAttributes support', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_os_hosts': {'service': 'Volume Service (Cinder)', 'feature': 'Admin-only host administration', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_qos_specs': {'service': 'Volume Service (Cinder)', 'feature': 'QoS specs support', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_os_quota_class_sets': {'service': 'Volume Service (Cinder)', 'feature': 'Quota classes management support', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_os_quota_sets': {'service': 'Volume Service (Cinder)', 'feature': 'Quotas management support', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_OS_SCH_HNT': {'service': 'Volume Service (Cinder)', 'feature': 'Pass arbitrary key/value pairs to the scheduler', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_os_services': {'service': 'Volume Service (Cinder)', 'feature': 'Services support', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_os_snapshot_actions': {'service': 'Volume Service (Cinder)', 'feature': 'Enable snapshot manager actions', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_os_types_extra_specs': {'service': 'Volume Service (Cinder)', 'feature': 'Types extra specs support', }, 
    'tempest_report.tempest_addons:CinderExtensionTest.test_os_types_manage': {'service': 'Volume Service (Cinder)', 'feature': 'Types manage support', }, 

    # Level 2: longer running tempests tests

    'tempest.api.compute.flavors.test_flavors': {'service': 'Compute (Nova)', 'level': 2},
    'tempest.api.compute.floating_ips.test_list_floating_ips': {'service': 'Compute (Nova)', 'level': 2},
    'tempest.api.compute.images.test_list_images': {'service': 'Compute (Nova)', 'level': 2},
    'tempest.api.compute.keypairs.test_keypairs': {'service': 'Compute (Nova)', 'level': 2},
    'tempest.api.compute.limits.test_absolute_limits': {'service': 'Compute (Nova)', 'level': 2},
    'tempest.api.compute.test_authorization': {'service': 'Compute (Nova)', 'level': 2},
    'tempest.api.compute.test_auth_token': {'service': 'Compute (Nova)', 'level': 2},
    'tempest.api.compute.test_extensions': {'service': 'Compute (Nova)', 'level': 2},
    'tempest.api.compute.volumes.test_attach_volume': {'service': 'Compute (Nova)', 'level': 2},
    'tempest.api.compute.volumes.test_volumes_get': {'service': 'Compute (Nova)', 'level': 2},
    'tempest.api.compute.volumes.test_volumes_list': {'service': 'Compute (Nova)', 'level': 2},
    'tempest.api.compute.volumes.test_volumes_negative': {'service': 'Compute (Nova)', 'level': 2},
    'tempest.thirdparty.boto.test_ec2_instance_run': {'service': 'Compute (Nova)', 'feature': 'EC2 API', }, 

    'tempest.api.image.v1.test_images': {'service': 'Image Service (Glance)', 'level': 2},
    'tempest.api.image.v2.test_images': {'service': 'Image Service (Glance)', 'level': 2},
    'tempest.cli.simple_read_only.test_glance': {'service': 'Image Service (Glance)', 'level': 2},
    'tempest.thirdparty.boto.test_s3_ec2_images': {'service': 'Image Service (Glance)', 'level': 2},

    # Level 3: long-running scenario tests
    'tempest.scenario.test_dashboard_basic_ops': {'service': 'Scenario', 'level': 3, 'feature': 'Dashboard (Horizon)', }, 
    'tempest.scenario.test_large_ops': {'service': 'Scenario', 'level': 3, 'feature': 'Large Operation Scenario (Nova & Glance)', }, 
    'tempest.scenario.test_server_advanced_ops': {'service': 'Scenario', 'level': 3, 'feature': 'Resize & Suspend (Nova)'},
    'tempest.scenario.test_minimum_basic': {'service': 'Scenario', 'level': 3, 'feature': 'Minimum Scenario (Nova, Glance, Conder)', },
    'tempest.scenario.test_network_basic_ops': {'service': 'Scenario', 'level': 3, 'feature': 'Network (Nova & Neutron)' },

    # Level 5: not yet decided 
    'tempest.scenario.orchestration.test_autoscaling': {'service': 'Scenario', 'level': 5},
    'tempest.scenario.test_network_quotas': {'service': 'Scenario', 'level': 5},
    'tempest.scenario.test_stamp_pattern': {'service': 'Scenario', 'level': 5},
    
    'tempest.api.network.test_extensions': {'level': 5},
    'tempest.thirdparty.boto.test_ec2_keys': {'level': 5},
    'tempest.thirdparty.boto.test_ec2_network': {'level': 5},

    'tempest.api.orchestration.stacks.test_limits': {'level': 5},
    'tempest.api.orchestration.stacks.test_neutron_resources': {'level': 5},
    'tempest.api.orchestration.stacks.test_non_empty_stack': {'level': 5},
    'tempest.api.orchestration.stacks.test_server_cfn_init': {'level': 5},
    'tempest.api.orchestration.stacks.test_stacks': {'level': 5},
    'tempest.api.orchestration.stacks.test_templates': {'level': 5},
    
    # Level 10: tests that failed devstack and need further investigation
    # A subset of these tests may still work
    'tempest.api.compute.admin.test_aggregates': {'level': 10},
    'tempest.api.compute.admin.test_availability_zone': {'level': 10},
    'tempest.api.compute.admin.test_fixed_ips': {'level': 10},
    'tempest.api.compute.admin.test_flavors': {'level': 10},
    'tempest.api.compute.admin.test_flavors_access': {'level': 10},
    'tempest.api.compute.admin.test_flavors_extra_specs': {'level': 10},
    'tempest.api.compute.admin.test_hosts': {'level': 10},
    'tempest.api.compute.admin.test_hypervisor': {'level': 10},
    'tempest.api.compute.admin.test_quotas': {'level': 10},
    'tempest.api.compute.admin.test_servers': {'level': 10},
    'tempest.api.compute.admin.test_services': {'level': 10},
    'tempest.api.compute.admin.test_simple_tenant_usage': {'level': 10},
    'tempest.api.compute.floating_ips.test_floating_ips_actions': {'level': 10},
    'tempest.api.compute.images.test_image_metadata': {'level': 10},
    'tempest.api.compute.images.test_images': {'level': 10},
    'tempest.api.compute.images.test_images_oneserver': {'level': 10},
    'tempest.api.compute.images.test_list_image_filters': {'level': 10},
    'tempest.api.compute.security_groups.test_security_group_rules': {'level': 10},
    'tempest.api.compute.security_groups.test_security_groups': {'level': 10},
    'tempest.api.compute.servers.test_attach_interfaces': {'level': 10},
    'tempest.api.compute.servers.test_create_server': {'level': 10},
    'tempest.api.compute.servers.test_disk_config': {'level': 10},
    'tempest.api.compute.servers.test_instance_actions': {'level': 10},
    'tempest.api.compute.servers.test_list_server_filters': {'level': 10},
    'tempest.api.compute.servers.test_list_servers_negative': {'level': 10},
    'tempest.api.compute.servers.test_multiple_create': {'level': 10},
    'tempest.api.compute.servers.test_server_actions': {'level': 10},
    'tempest.api.compute.servers.test_server_addresses': {'level': 10},
    'tempest.api.compute.servers.test_server_metadata': {'level': 10},
    'tempest.api.compute.servers.test_server_personality': {'level': 10},
    'tempest.api.compute.servers.test_server_rescue': {'level': 10},
    'tempest.api.compute.servers.test_servers': {'level': 10},
    'tempest.api.compute.servers.test_servers_negative': {'level': 10},
    'tempest.api.compute.servers.test_virtual_interfaces': {'level': 10},
    'tempest.api.compute.test_live_block_migration': {'level': 10},
    'tempest.api.compute.test_quotas': {'level': 10},
    'tempest.api.identity.admin.test_roles': {'level': 10},
    'tempest.api.identity.admin.test_services': {'level': 10},
    'tempest.api.identity.admin.test_tenant_negative': {'level': 10},
    'tempest.api.identity.admin.test_tenants': {'level': 10},
    'tempest.api.identity.admin.test_users': {'level': 10},
    'tempest.api.identity.admin.test_users_negative': {'level': 10},
    'tempest.api.identity.admin.v3.test_credentials': {'level': 10},
    'tempest.api.identity.admin.v3.test_domains': {'level': 10},
    'tempest.api.identity.admin.v3.test_endpoints': {'level': 10},
    'tempest.api.identity.admin.v3.test_policies': {'level': 10},
    'tempest.api.identity.admin.v3.test_projects': {'level': 10},
    'tempest.api.identity.admin.v3.test_roles': {'level': 10},
    'tempest.api.identity.admin.v3.test_services': {'level': 10},
    'tempest.api.identity.admin.v3.test_tokens': {'level': 10},
    'tempest.api.identity.admin.v3.test_users': {'level': 10},
    'tempest.api.image.v1.test_image_members': {'level': 10},
    'tempest.api.network.test_floating_ips': {'level': 10},
    'tempest.api.network.test_load_balancer': {'level': 10},
    'tempest.api.network.test_networks': {'level': 10},
    'tempest.api.network.test_quotas': {'level': 10},
    'tempest.api.network.test_routers': {'level': 10},
    'tempest.api.network.test_security_groups': {'level': 10},
    'tempest.api.network.test_security_groups_negative': {'level': 10},
    'tempest.api.network.test_vpnaas_extensions': {'level': 10},
    'tempest.api.object_storage.test_account_quotas': {'level': 10},
    'tempest.api.object_storage.test_account_services': {'level': 10},
    'tempest.api.object_storage.test_container_acl': {'level': 10},
    'tempest.api.object_storage.test_object_services': {'level': 10},
    'tempest.api.volume.admin.test_multi_backend': {'level': 10},
    'tempest.api.volume.admin.test_volume_types': {'level': 10},
    'tempest.api.volume.admin.test_volume_types_extra_specs': {'level': 10},
    'tempest.api.volume.admin.test_volume_types_extra_specs_negative': {'level': 10},
    'tempest.api.volume.admin.test_volume_types_negative': {'level': 10},
    'tempest.api.volume.test_volumes_actions': {'level': 10},
    'tempest.api.volume.test_volumes_get': {'level': 10},
    'tempest.api.volume.test_volumes_list': {'level': 10},
    'tempest.api.volume.test_volumes_negative': {'level': 10},
    'tempest.api.volume.test_volumes_snapshots': {'level': 10},
    'tempest.cli.simple_read_only.test_cinder': {'level': 10},
    'tempest.cli.simple_read_only.test_keystone': {'level': 10},
    'tempest.cli.simple_read_only.test_neutron': {'level': 10},
    'tempest.cli.simple_read_only.test_nova': {'level': 10},
    'tempest.scenario.test_minimum_basic': {'level': 10},
    'tempest.scenario.test_network_basic_ops': {'level': 10},
    'tempest.scenario.test_server_basic_ops': {'level': 10},
    'tempest.scenario.test_snapshot_pattern': {'level': 10},
    'tempest.scenario.test_volume_boot_pattern': {'level': 10},
    'tempest.thirdparty.boto.test_ec2_security_groups': {'level': 10},
    'tempest.thirdparty.boto.test_s3_objects': {'level': 10},
    'tempest.thirdparty.boto.test_ec2_volumes': {'level': 10},
}
