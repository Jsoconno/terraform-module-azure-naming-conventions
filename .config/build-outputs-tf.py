# This script automatically creates the outputs.tf file

resource_list = [
    "azurerm_api_management",
    "azurerm_api_management_api",
    "azurerm_api_management_api_diagnostic",
    "azurerm_api_management_api_operation",
    "azurerm_api_management_api_operation_policy",
    "azurerm_api_management_api_operation_tag",
    "azurerm_api_management_api_policy",
    "azurerm_api_management_api_release",
    "azurerm_api_management_api_schema",
    "azurerm_api_management_api_version_set",
    "azurerm_api_management_authorization_server",
    "azurerm_api_management_backend",
    "azurerm_api_management_certificate",
    "azurerm_api_management_custom_domain",
    "azurerm_api_management_diagnostic",
    "azurerm_api_management_email_template",
    "azurerm_api_management_gateway",
    "azurerm_api_management_gateway_api",
    "azurerm_api_management_group",
    "azurerm_api_management_group_user",
    "azurerm_api_management_identity_provider_aad",
    "azurerm_api_management_identity_provider_aadb2c",
    "azurerm_api_management_identity_provider_facebook",
    "azurerm_api_management_identity_provider_google",
    "azurerm_api_management_identity_provider_microsoft",
    "azurerm_api_management_identity_provider_twitter",
    "azurerm_api_management_logger",
    "azurerm_api_management_named_value",
    "azurerm_api_management_notification_recipient_email",
    "azurerm_api_management_openid_connect_provider",
    "azurerm_api_management_policy",
    "azurerm_api_management_product",
    "azurerm_api_management_product_api",
    "azurerm_api_management_product_group",
    "azurerm_api_management_product_policy",
    "azurerm_api_management_property",
    "azurerm_api_management_redis_cache",
    "azurerm_api_management_subscription",
    "azurerm_api_management_tag",
    "azurerm_api_management_user",
    "azurerm_active_directory_domain_service",
    "azurerm_active_directory_domain_service_replica_set",
    "azurerm_advisor_recommendations",
    "azurerm_analysis_services_server",
    "azurerm_app_configuration",
    "azurerm_app_configuration_feature",
    "azurerm_app_configuration_key",
    "azurerm_app_service",
    "azurerm_app_service_active_slot",
    "azurerm_app_service_certificate",
    "azurerm_app_service_certificate_binding",
    "azurerm_app_service_certificate_order",
    "azurerm_app_service_custom_hostname_binding",
    "azurerm_app_service_environment",
    "azurerm_app_service_environment_v3",
    "azurerm_app_service_hybrid_connection",
    "azurerm_app_service_managed_certificate",
    "azurerm_app_service_plan",
    "azurerm_app_service_slot",
    "azurerm_app_service_slot_virtual_network_swift_connection",
    "azurerm_app_service_source_control",
    "azurerm_app_service_source_control_token",
    "azurerm_app_service_virtual_network_swift_connection",
    "azurerm_function_app",
    "azurerm_function_app_slot",
    "azurerm_linux_web_app",
    "azurerm_service_plan",
    "azurerm_source_control_token",
    "azurerm_static_site",
    "azurerm_windows_web_app",
    "azurerm_application_insights",
    "azurerm_application_insights_analytics_item",
    "azurerm_application_insights_api_key",
    "azurerm_application_insights_smart_detection_rule",
    "azurerm_application_insights_web_test",
    "azurerm_attestation",
    "azurerm_role_assignment",
    "azurerm_role_definition",
    "azurerm_user_assigned_identity",
    "azurerm_automation_account",
    "azurerm_automation_certificate",
    "azurerm_automation_connection",
    "azurerm_automation_connection_certificate",
    "azurerm_automation_connection_classic_certificate",
    "azurerm_automation_connection_service_principal",
    "azurerm_automation_credential",
    "azurerm_automation_dsc_configuration",
    "azurerm_automation_dsc_nodeconfiguration",
    "azurerm_automation_job_schedule",
    "azurerm_automation_module",
    "azurerm_automation_runbook",
    "azurerm_automation_schedule",
    "azurerm_automation_variable_bool",
    "azurerm_automation_variable_datetime",
    "azurerm_automation_variable_int",
    "azurerm_automation_variable_string",
    "azurerm_stack_hci_cluster",
    "azurerm_resource_group",
    "azurerm_resource_provider_registration",
    "azurerm_batch_account",
    "azurerm_batch_application",
    "azurerm_batch_certificate",
    "azurerm_batch_job",
    "azurerm_batch_pool",
    "azurerm_billing_enrollment_account_scope",
    "azurerm_billing_mca_account_scope",
    "azurerm_blueprint_assignment",
    "azurerm_bot_channel_alexa",
    "azurerm_bot_channel_direct_line_speech",
    "azurerm_bot_channel_directline",
    "azurerm_bot_channel_email",
    "azurerm_bot_channel_facebook",
    "azurerm_bot_channel_line",
    "azurerm_bot_channel_ms_teams",
    "azurerm_bot_channel_slack",
    "azurerm_bot_channel_sms",
    "azurerm_bot_channel_web_chat",
    "azurerm_bot_channels_registration",
    "azurerm_bot_connection",
    "azurerm_bot_healthbot",
    "azurerm_bot_web_app",
    "azurerm_cdn_endpoint",
    "azurerm_cdn_endpoint_custom_domain",
    "azurerm_cdn_profile",
    "azurerm_cognitive_account",
    "azurerm_cognitive_account_customer_managed_key",
    "azurerm_communication_service",
    "azurerm_availability_set",
    "azurerm_dedicated_host",
    "azurerm_dedicated_host_group",
    "azurerm_disk_access",
    "azurerm_disk_encryption_set",
    "azurerm_image",
    "azurerm_linux_virtual_machine",
    "azurerm_linux_virtual_machine_scale_set",
    "azurerm_managed_disk",
    "azurerm_marketplace_agreement",
    "azurerm_orchestrated_virtual_machine_scale_set",
    "azurerm_proximity_placement_group",
    "azurerm_shared_image",
    "azurerm_shared_image_gallery",
    "azurerm_shared_image_version",
    "azurerm_snapshot",
    "azurerm_ssh_public_key",
    "azurerm_virtual_machine",
    "azurerm_virtual_machine_data_disk_attachment",
    "azurerm_virtual_machine_extension",
    "azurerm_virtual_machine_scale_set",
    "azurerm_virtual_machine_scale_set_extension",
    "azurerm_windows_virtual_machine",
    "azurerm_windows_virtual_machine_scale_set",
    "azurerm_consumption_budget_resource_group",
    "azurerm_consumption_budget_subscription",
    "azurerm_container_group",
    "azurerm_container_registry",
    "azurerm_container_registry_scope_map",
    "azurerm_container_registry_token",
    "azurerm_container_registry_webhook",
    "azurerm_kubernetes_cluster",
    "azurerm_kubernetes_cluster_node_pool",
    "azurerm_cosmosdb_account",
    "azurerm_cosmosdb_cassandra_keyspace",
    "azurerm_cosmosdb_cassandra_table",
    "azurerm_cosmosdb_gremlin_database",
    "azurerm_cosmosdb_gremlin_graph",
    "azurerm_cosmosdb_mongo_collection",
    "azurerm_cosmosdb_mongo_database",
    "azurerm_cosmosdb_notebook_workspace",
    "azurerm_cosmosdb_sql_container",
    "azurerm_cosmosdb_sql_database",
    "azurerm_cosmosdb_sql_function",
    "azurerm_cosmosdb_sql_stored_procedure",
    "azurerm_cosmosdb_sql_trigger",
    "azurerm_cosmosdb_table",
    "azurerm_cost_management_export_resource_group",
    "azurerm_dns_a_record",
    "azurerm_dns_aaaa_record",
    "azurerm_dns_caa_record",
    "azurerm_dns_cname_record",
    "azurerm_dns_mx_record",
    "azurerm_dns_ns_record",
    "azurerm_dns_ptr_record",
    "azurerm_dns_srv_record",
    "azurerm_dns_txt_record",
    "azurerm_dns_zone",
    "azurerm_kusto_attached_database_configuration",
    "azurerm_kusto_cluster",
    "azurerm_kusto_cluster_customer_managed_key",
    "azurerm_kusto_cluster_principal_assignment",
    "azurerm_kusto_database",
    "azurerm_kusto_database_principal",
    "azurerm_kusto_database_principal_assignment",
    "azurerm_kusto_eventgrid_data_connection",
    "azurerm_kusto_eventhub_data_connection",
    "azurerm_kusto_iothub_data_connection",
    "azurerm_data_factory",
    "azurerm_data_factory_custom_dataset",
    "azurerm_data_factory_data_flow",
    "azurerm_data_factory_dataset_azure_blob",
    "azurerm_data_factory_dataset_binary",
    "azurerm_data_factory_dataset_cosmosdb_sqlapi",
    "azurerm_data_factory_dataset_delimited_text",
    "azurerm_data_factory_dataset_http",
    "azurerm_data_factory_dataset_json",
    "azurerm_data_factory_dataset_mysql",
    "azurerm_data_factory_dataset_parquet",
    "azurerm_data_factory_dataset_postgresql",
    "azurerm_data_factory_dataset_snowflake",
    "azurerm_data_factory_dataset_sql_server_table",
    "azurerm_data_factory_integration_runtime_azure",
    "azurerm_data_factory_integration_runtime_azure_ssis",
    "azurerm_data_factory_integration_runtime_managed",
    "azurerm_data_factory_integration_runtime_self_hosted",
    "azurerm_data_factory_linked_custom_service",
    "azurerm_data_factory_linked_service_azure_blob_storage",
    "azurerm_data_factory_linked_service_azure_databricks",
    "azurerm_data_factory_linked_service_azure_file_storage",
    "azurerm_data_factory_linked_service_azure_function",
    "azurerm_data_factory_linked_service_azure_search",
    "azurerm_data_factory_linked_service_azure_sql_database",
    "azurerm_data_factory_linked_service_azure_table_storage",
    "azurerm_data_factory_linked_service_cosmosdb",
    "azurerm_data_factory_linked_service_data_lake_storage_gen2",
    "azurerm_data_factory_linked_service_key_vault",
    "azurerm_data_factory_linked_service_kusto",
    "azurerm_data_factory_linked_service_mysql",
    "azurerm_data_factory_linked_service_odata",
    "azurerm_data_factory_linked_service_postgresql",
    "azurerm_data_factory_linked_service_sftp",
    "azurerm_data_factory_linked_service_snowflake",
    "azurerm_data_factory_linked_service_sql_server",
    "azurerm_data_factory_linked_service_synapse",
    "azurerm_data_factory_linked_service_web",
    "azurerm_data_factory_managed_private_endpoint",
    "azurerm_data_factory_pipeline",
    "azurerm_data_factory_trigger_blob_event",
    "azurerm_data_factory_trigger_custom_event",
    "azurerm_data_factory_trigger_schedule",
    "azurerm_data_factory_tumbling_window",
    "azurerm_data_lake_analytics_account",
    "azurerm_data_lake_analytics_firewall_rule",
    "azurerm_data_lake_store",
    "azurerm_data_lake_store_file",
    "azurerm_data_lake_store_firewall_rule",
    "azurerm_data_lake_store_virtual_network_rule",
    "azurerm_data_share",
    "azurerm_data_share_account",
    "azurerm_data_share_dataset_blob_storage",
    "azurerm_data_share_dataset_data_lake_gen1",
    "azurerm_data_share_dataset_data_lake_gen2",
    "azurerm_data_share_dataset_kusto_cluster",
    "azurerm_data_share_dataset_kusto_database",
    "azurerm_data_protection_backup_instance_blob_storage",
    "azurerm_data_protection_backup_instance_disk",
    "azurerm_data_protection_backup_instance_postgresql",
    "azurerm_data_protection_backup_policy_blob_storage",
    "azurerm_data_protection_backup_policy_disk",
    "azurerm_data_protection_backup_policy_postgresql",
    "azurerm_data_protection_backup_vault",
    "azurerm_mariadb_configuration",
    "azurerm_mariadb_database",
    "azurerm_mariadb_firewall_rule",
    "azurerm_mariadb_server",
    "azurerm_mariadb_virtual_network_rule",
    "azurerm_mssql_database",
    "azurerm_mssql_database_extended_auditing_policy",
    "azurerm_mssql_database_vulnerability_assessment_rule_baseline",
    "azurerm_mssql_elasticpool",
    "azurerm_mssql_failover_group",
    "azurerm_mssql_firewall_rule",
    "azurerm_mssql_job_agent",
    "azurerm_mssql_job_credential",
    "azurerm_mssql_server",
    "azurerm_mssql_server_extended_auditing_policy",
    "azurerm_mssql_server_security_alert_policy",
    "azurerm_mssql_server_transparent_data_encryption",
    "azurerm_mssql_server_vulnerability_assessment",
    "azurerm_mssql_virtual_machine",
    "azurerm_mssql_virtual_network_rule",
    "azurerm_mysql_active_directory_administrator",
    "azurerm_mysql_configuration",
    "azurerm_mysql_database",
    "azurerm_mysql_firewall_rule",
    "azurerm_mysql_server",
    "azurerm_mysql_server_key",
    "azurerm_mysql_virtual_network_rule",
    "azurerm_postgresql_active_directory_administrator",
    "azurerm_postgresql_configuration",
    "azurerm_postgresql_database",
    "azurerm_postgresql_firewall_rule",
    "azurerm_postgresql_flexible_server",
    "azurerm_postgresql_flexible_server_configuration",
    "azurerm_postgresql_flexible_server_database",
    "azurerm_postgresql_flexible_server_firewall_rule",
    "azurerm_postgresql_server",
    "azurerm_postgresql_server_key",
    "azurerm_postgresql_virtual_network_rule",
    "azurerm_sql_active_directory_administrator",
    "azurerm_sql_database",
    "azurerm_sql_elasticpool",
    "azurerm_sql_failover_group",
    "azurerm_sql_firewall_rule",
    "azurerm_sql_managed_database",
    "azurerm_sql_managed_instance",
    "azurerm_sql_server",
    "azurerm_sql_virtual_network_rule",
    "azurerm_database_migration_project",
    "azurerm_database_migration_service",
    "azurerm_databox_edge_device",
    "azurerm_databox_edge_order",
    "azurerm_databricks_workspace",
    "azurerm_databricks_workspace_customer_managed_key",
    "azurerm_virtual_desktop_application",
    "azurerm_virtual_desktop_application_group",
    "azurerm_virtual_desktop_host_pool",
    "azurerm_virtual_desktop_workspace",
    "azurerm_virtual_desktop_workspace_application_group_association",
    "azurerm_dev_test_global_vm_shutdown_schedule",
    "azurerm_dev_test_lab",
    "azurerm_dev_test_linux_virtual_machine",
    "azurerm_dev_test_policy",
    "azurerm_dev_test_schedule",
    "azurerm_dev_test_virtual_network",
    "azurerm_dev_test_windows_virtual_machine",
    "azurerm_devspace_controller",
    "azurerm_digital_twins_endpoint_eventgrid",
    "azurerm_digital_twins_endpoint_eventhub",
    "azurerm_digital_twins_endpoint_servicebus",
    "azurerm_digital_twins_instance",
    "azurerm_hdinsight_hadoop_cluster",
    "azurerm_hdinsight_hbase_cluster",
    "azurerm_hdinsight_interactive_query_cluster",
    "azurerm_hdinsight_kafka_cluster",
    "azurerm_hdinsight_ml_services_cluster",
    "azurerm_hdinsight_rserver_cluster",
    "azurerm_hdinsight_spark_cluster",
    "azurerm_hdinsight_storm_cluster",
    "azurerm_dedicated_hardware_security_module",
    "azurerm_healthcare_service",
    "azurerm_iotcentral_application",
    "azurerm_iothub",
    "azurerm_iothub_consumer_group",
    "azurerm_iothub_dps",
    "azurerm_iothub_dps_certificate",
    "azurerm_iothub_dps_shared_access_policy",
    "azurerm_iothub_shared_access_policy",
    "azurerm_key_vault",
    "azurerm_key_vault_access_policy",
    "azurerm_key_vault_certificate",
    "azurerm_key_vault_certificate_issuer",
    "azurerm_key_vault_key",
    "azurerm_key_vault_managed_hardware_security_module",
    "azurerm_key_vault_managed_storage_account",
    "azurerm_key_vault_managed_storage_account_sas_token_definition",
    "azurerm_key_vault_secret",
    "azurerm_lighthouse_assignment",
    "azurerm_lighthouse_definition",
    "azurerm_lb",
    "azurerm_lb_backend_address_pool",
    "azurerm_lb_backend_address_pool_address",
    "azurerm_lb_nat_pool",
    "azurerm_lb_nat_rule",
    "azurerm_lb_outbound_rule",
    "azurerm_lb_probe",
    "azurerm_lb_rule",
    "azurerm_log_analytics_cluster",
    "azurerm_log_analytics_cluster_customer_managed_key",
    "azurerm_log_analytics_data_export_rule",
    "azurerm_log_analytics_datasource_windows_event",
    "azurerm_log_analytics_datasource_windows_performance_counter",
    "azurerm_log_analytics_linked_service",
    "azurerm_log_analytics_linked_storage_account",
    "azurerm_log_analytics_saved_search",
    "azurerm_log_analytics_solution",
    "azurerm_log_analytics_storage_insights",
    "azurerm_log_analytics_workspace",
    "azurerm_integration_service_environment",
    "azurerm_logic_app_action_custom",
    "azurerm_logic_app_action_http",
    "azurerm_logic_app_integration_account",
    "azurerm_logic_app_integration_account_agreement",
    "azurerm_logic_app_integration_account_assembly",
    "azurerm_logic_app_integration_account_batch_configuration",
    "azurerm_logic_app_integration_account_certificate",
    "azurerm_logic_app_integration_account_map",
    "azurerm_logic_app_integration_account_partner",
    "azurerm_logic_app_integration_account_schema",
    "azurerm_logic_app_integration_account_session",
    "azurerm_logic_app_standard",
    "azurerm_logic_app_trigger_custom",
    "azurerm_logic_app_trigger_http_request",
    "azurerm_logic_app_trigger_recurrence",
    "azurerm_logic_app_workflow",
    "azurerm_machine_learning_compute_cluster",
    "azurerm_machine_learning_compute_instance",
    "azurerm_machine_learning_inference_cluster",
    "azurerm_machine_learning_synapse_spark",
    "azurerm_machine_learning_workspace",
    "azurerm_maintenance_assignment_dedicated_host",
    "azurerm_maintenance_assignment_virtual_machine",
    "azurerm_maintenance_assignment_virtual_machine_scale_set",
    "azurerm_maintenance_configuration",
    "azurerm_managed_application",
    "azurerm_managed_application_definition",
    "azurerm_management_group",
    "azurerm_management_group_subscription_association",
    "azurerm_management_lock",
    "azurerm_maps_account",
    "azurerm_media_asset",
    "azurerm_media_asset_filter",
    "azurerm_media_content_key_policy",
    "azurerm_media_job",
    "azurerm_media_live_event",
    "azurerm_media_live_output",
    "azurerm_media_services_account",
    "azurerm_media_streaming_endpoint",
    "azurerm_media_streaming_locator",
    "azurerm_media_streaming_policy",
    "azurerm_media_transform",
    "azurerm_eventgrid_domain",
    "azurerm_eventgrid_domain_topic",
    "azurerm_eventgrid_event_subscription",
    "azurerm_eventgrid_system_topic",
    "azurerm_eventgrid_system_topic_event_subscription",
    "azurerm_eventgrid_topic",
    "azurerm_eventhub",
    "azurerm_eventhub_authorization_rule",
    "azurerm_eventhub_cluster",
    "azurerm_eventhub_consumer_group",
    "azurerm_eventhub_namespace",
    "azurerm_eventhub_namespace_authorization_rule",
    "azurerm_eventhub_namespace_customer_managed_key",
    "azurerm_eventhub_namespace_disaster_recovery_config",
    "azurerm_iothub_endpoint_eventhub",
    "azurerm_iothub_endpoint_servicebus_queue",
    "azurerm_iothub_endpoint_servicebus_topic",
    "azurerm_iothub_endpoint_storage_container",
    "azurerm_iothub_enrichment",
    "azurerm_iothub_fallback_route",
    "azurerm_iothub_route",
    "azurerm_notification_hub",
    "azurerm_notification_hub_authorization_rule",
    "azurerm_notification_hub_namespace",
    "azurerm_relay_hybrid_connection",
    "azurerm_relay_hybrid_connection_authorization_rule",
    "azurerm_relay_namespace",
    "azurerm_relay_namespace_authorization_rule",
    "azurerm_servicebus_namespace",
    "azurerm_servicebus_namespace_authorization_rule",
    "azurerm_servicebus_namespace_disaster_recovery_config",
    "azurerm_servicebus_namespace_network_rule_set",
    "azurerm_servicebus_queue",
    "azurerm_servicebus_queue_authorization_rule",
    "azurerm_servicebus_subscription",
    "azurerm_servicebus_subscription_rule",
    "azurerm_servicebus_topic",
    "azurerm_servicebus_topic_authorization_rule",
    "azurerm_signalr_service",
    "azurerm_signalr_service_network_acl",
    "azurerm_spatial_anchors_account",
    "azurerm_monitor_aad_diagnostic_setting",
    "azurerm_monitor_action_group",
    "azurerm_monitor_action_rule_action_group",
    "azurerm_monitor_action_rule_suppression",
    "azurerm_monitor_activity_log_alert",
    "azurerm_monitor_autoscale_setting",
    "azurerm_monitor_diagnostic_setting",
    "azurerm_monitor_log_profile",
    "azurerm_monitor_metric_alert",
    "azurerm_monitor_scheduled_query_rules_alert",
    "azurerm_monitor_scheduled_query_rules_log",
    "azurerm_monitor_smart_detector_alert_rule",
    "azurerm_netapp_account",
    "azurerm_netapp_pool",
    "azurerm_netapp_snapshot",
    "azurerm_netapp_volume",
    "azurerm_application_gateway",
    "azurerm_application_security_group",
    "azurerm_bastion_host",
    "azurerm_express_route_circuit",
    "azurerm_express_route_circuit_authorization",
    "azurerm_express_route_circuit_connection",
    "azurerm_express_route_circuit_peering",
    "azurerm_express_route_connection",
    "azurerm_express_route_gateway",
    "azurerm_express_route_port",
    "azurerm_firewall",
    "azurerm_firewall_application_rule_collection",
    "azurerm_firewall_nat_rule_collection",
    "azurerm_firewall_network_rule_collection",
    "azurerm_firewall_policy",
    "azurerm_firewall_policy_rule_collection_group",
    "azurerm_frontdoor",
    "azurerm_frontdoor_custom_https_configuration",
    "azurerm_frontdoor_firewall_policy",
    "azurerm_frontdoor_rules_engine",
    "azurerm_ip_group",
    "azurerm_local_network_gateway",
    "azurerm_nat_gateway",
    "azurerm_nat_gateway_public_ip_association",
    "azurerm_nat_gateway_public_ip_prefix_association",
    "azurerm_network_connection_monitor",
    "azurerm_network_ddos_protection_plan",
    "azurerm_network_interface",
    "azurerm_network_interface_application_gateway_backend_address_pool_association",
    "azurerm_network_interface_application_security_group_association",
    "azurerm_network_interface_backend_address_pool_association",
    "azurerm_network_interface_nat_rule_association",
    "azurerm_network_interface_security_group_association",
    "azurerm_network_packet_capture",
    "azurerm_network_profile",
    "azurerm_network_security_group",
    "azurerm_network_security_rule",
    "azurerm_network_watcher",
    "azurerm_network_watcher_flow_log",
    "azurerm_packet_capture",
    "azurerm_point_to_site_vpn_gateway",
    "azurerm_private_endpoint",
    "azurerm_private_link_service",
    "azurerm_public_ip",
    "azurerm_public_ip_prefix",
    "azurerm_route",
    "azurerm_route_filter",
    "azurerm_route_table",
    "azurerm_subnet",
    "azurerm_subnet_nat_gateway_association",
    "azurerm_subnet_network_security_group_association",
    "azurerm_subnet_route_table_association",
    "azurerm_subnet_service_endpoint_storage_policy",
    "azurerm_traffic_manager_endpoint",
    "azurerm_traffic_manager_profile",
    "azurerm_virtual_hub",
    "azurerm_virtual_hub_bgp_connection",
    "azurerm_virtual_hub_connection",
    "azurerm_virtual_hub_ip",
    "azurerm_virtual_hub_route_table",
    "azurerm_virtual_hub_security_partner_provider",
    "azurerm_virtual_network",
    "azurerm_virtual_network_gateway",
    "azurerm_virtual_network_gateway_connection",
    "azurerm_virtual_network_peering",
    "azurerm_virtual_wan",
    "azurerm_vpn_gateway",
    "azurerm_vpn_gateway_connection",
    "azurerm_vpn_server_configuration",
    "azurerm_vpn_site",
    "azurerm_web_application_firewall_policy",
    "azurerm_management_group_policy_assignment",
    "azurerm_policy_assignment",
    "azurerm_policy_definition",
    "azurerm_policy_remediation",
    "azurerm_policy_set_definition",
    "azurerm_policy_virtual_machine_configuration_assignment",
    "azurerm_resource_group_policy_assignment",
    "azurerm_resource_policy_assignment",
    "azurerm_subscription_policy_assignment",
    "azurerm_virtual_machine_configuration_policy_assignment",
    "azurerm_dashboard",
    "azurerm_portal_tenant_configuration",
    "azurerm_powerbi_embedded",
    "azurerm_private_dns_a_record",
    "azurerm_private_dns_aaaa_record",
    "azurerm_private_dns_cname_record",
    "azurerm_private_dns_mx_record",
    "azurerm_private_dns_ptr_record",
    "azurerm_private_dns_srv_record",
    "azurerm_private_dns_txt_record",
    "azurerm_private_dns_zone",
    "azurerm_private_dns_zone_virtual_network_link",
    "azurerm_purview_account",
    "azurerm_backup_container_storage_account",
    "azurerm_backup_policy_file_share",
    "azurerm_backup_policy_vm",
    "azurerm_backup_protected_file_share",
    "azurerm_backup_protected_vm",
    "azurerm_recovery_services_vault",
    "azurerm_site_recovery_fabric",
    "azurerm_site_recovery_network_mapping",
    "azurerm_site_recovery_protection_container",
    "azurerm_site_recovery_protection_container_mapping",
    "azurerm_site_recovery_replicated_vm",
    "azurerm_site_recovery_replication_policy",
    "azurerm_redis_cache",
    "azurerm_redis_firewall_rule",
    "azurerm_redis_linked_server",
    "azurerm_redis_enterprise_cluster",
    "azurerm_redis_enterprise_database",
    "azurerm_search_service",
    "azurerm_advanced_threat_protection",
    "azurerm_security_center_server_vulnerability_assessment",
    "azurerm_iot_security_device_group",
    "azurerm_iot_security_solution",
    "azurerm_security_center_assessment",
    "azurerm_security_center_assessment_metadata",
    "azurerm_security_center_assessment_policy",
    "azurerm_security_center_auto_provisioning",
    "azurerm_security_center_automation",
    "azurerm_security_center_contact",
    "azurerm_security_center_setting",
    "azurerm_security_center_subscription_pricing",
    "azurerm_security_center_workspace",
    "azurerm_sentinel_alert_rule_machine_learning_behavior_analytics",
    "azurerm_sentinel_alert_rule_fusion",
    "azurerm_sentinel_alert_rule_ms_security_incident",
    "azurerm_sentinel_alert_rule_scheduled",
    "azurerm_sentinel_data_connector_aws_cloud_trail",
    "azurerm_sentinel_data_connector_azure_active_directory",
    "azurerm_sentinel_data_connector_azure_advanced_threat_protection",
    "azurerm_sentinel_data_connector_azure_security_center",
    "azurerm_sentinel_data_connector_microsoft_cloud_app_security",
    "azurerm_sentinel_data_connector_microsoft_defender_advanced_threat_protection",
    "azurerm_sentinel_data_connector_office_365",
    "azurerm_sentinel_data_connector_threat_intelligence",
    "azurerm_service_fabric_cluster",
    "azurerm_service_fabric_mesh_application",
    "azurerm_service_fabric_mesh_local_network",
    "azurerm_service_fabric_mesh_secret",
    "azurerm_service_fabric_mesh_secret_value",
    "azurerm_spring_cloud_active_deployment",
    "azurerm_spring_cloud_app",
    "azurerm_spring_cloud_app_cosmosdb_association",
    "azurerm_spring_cloud_app_mysql_association",
    "azurerm_spring_cloud_app_redis_association",
    "azurerm_spring_cloud_certificate",
    "azurerm_spring_cloud_custom_domain",
    "azurerm_spring_cloud_java_deployment",
    "azurerm_spring_cloud_service",
    "azurerm_hpc_cache",
    "azurerm_hpc_cache_access_policy",
    "azurerm_hpc_cache_blob_nfs_target",
    "azurerm_hpc_cache_blob_target",
    "azurerm_hpc_cache_nfs_target",
    "azurerm_storage_account",
    "azurerm_storage_account_customer_managed_key",
    "azurerm_storage_account_network_rules",
    "azurerm_storage_blob",
    "azurerm_storage_blob_inventory_policy",
    "azurerm_storage_container",
    "azurerm_storage_data_lake_gen2_filesystem",
    "azurerm_storage_data_lake_gen2_path",
    "azurerm_storage_encryption_scope",
    "azurerm_storage_management_policy",
    "azurerm_storage_object_replication",
    "azurerm_storage_queue",
    "azurerm_storage_share",
    "azurerm_storage_share_directory",
    "azurerm_storage_share_file",
    "azurerm_storage_sync",
    "azurerm_storage_sync_cloud_endpoint",
    "azurerm_storage_sync_group",
    "azurerm_storage_table",
    "azurerm_storage_table_entity",
    "azurerm_stream_analytics_function_javascript_udf",
    "azurerm_stream_analytics_job",
    "azurerm_stream_analytics_output_blob",
    "azurerm_stream_analytics_output_eventhub",
    "azurerm_stream_analytics_output_mssql",
    "azurerm_stream_analytics_output_servicebus_queue",
    "azurerm_stream_analytics_output_servicebus_topic",
    "azurerm_stream_analytics_reference_input_blob",
    "azurerm_stream_analytics_stream_input_blob",
    "azurerm_stream_analytics_stream_input_eventhub",
    "azurerm_stream_analytics_stream_input_iothub",
    "azurerm_synapse_firewall_rule",
    "azurerm_synapse_integration_runtime_azure",
    "azurerm_synapse_integration_runtime_self_hosted",
    "azurerm_synapse_linked_service",
    "azurerm_synapse_managed_private_endpoint",
    "azurerm_synapse_private_link_hub",
    "azurerm_synapse_role_assignment",
    "azurerm_synapse_spark_pool",
    "azurerm_synapse_sql_pool",
    "azurerm_synapse_sql_pool_extended_auditing_policy",
    "azurerm_synapse_sql_pool_security_alert_policy",
    "azurerm_synapse_sql_pool_vulnerability_assessment",
    "azurerm_synapse_workspace",
    "azurerm_synapse_workspace_extended_auditing_policy",
    "azurerm_synapse_workspace_keys",
    "azurerm_synapse_workspace_security_alert_policy",
    "azurerm_synapse_workspace_vulnerability_assessment",
    "azurerm_iot_time_series_insights_access_policy",
    "azurerm_iot_time_series_insights_event_source_iothub",
    "azurerm_iot_time_series_insights_gen2_environment",
    "azurerm_iot_time_series_insights_reference_data_set",
    "azurerm_iot_time_series_insights_standard_environment",
    "azurerm_vmware_cluster",
    "azurerm_vmware_express_route_authorization",
    "azurerm_vmware_private_cloud",
    "azurerm_video_analyzer",
    "azurerm_video_analyzer_edge_module",
]

alphanumeric_lowercase_only = [
    "azurerm_analysis_services_server",
    "azurerm_batch_account",
    "azurerm_data_factory_linked_service_data_lake_storage_gen2",
    "azurerm_data_lake_analytics_account",
    "azurerm_data_lake_store",
    "azurerm_data_share_dataset_kusto_cluster",
    "azurerm_media_services_account",
    "azurerm_storage_account",
]

alphanumeric_only = [
    "azurerm_app_service_certificate_order",
    "azurerm_container_registry",
    "azurerm_container_registry_webhook",
    "azurerm_logic_app_integration_account",
    "azurerm_frontdoor_firewall_policy",
    "azurerm_storage_table",
]

lowercase_only = [
    "azurerm_container_group",
    "azurerm_sql_failover_group",
    "azurerm_sql_managed_instance",
    "azurerm_sql_server",
    "azurerm_service_fabric_cluster",
    "azurerm_storage_container",
    "azurerm_storage_queue",
    "azurerm_storage_share",
]

alphanumeric_underscore_only = [
    "azurerm_disk_encryption_set",
]

length_restricted = [
    "azurerm_windows_virtual_machine",
    "azurerm_windows_virtual_machine_scale_set",
]

def format_standard(resource, acronym):
    return f'output "{resource}" {{\n  value = "{acronym}${{local.convention}}"\n  description = "Naming convention for the resource {resource}."\n}}\n\n'

def format_alphanumeric_lowercase_only(resource, acronym):
    return f'output "{resource}" {{\n  value = "{acronym}${{lower(replace(local.convention, "-", ""))}}"\n  description = "Naming convention for the resource {resource}.  This resource requires alphanumeric and lowercase values only."\n}}\n\n'

def format_alphanumeric_only(resource, acronym):
    return f'output "{resource}" {{\n  value = "{acronym}${{replace(local.convention, "-", "")}}"\n  description = "Naming convention for the resource {resource}.  This resource requires alphanumeric values only."\n}}\n\n'

def format_lowercase_only(resource, acronym):
    return f'output "{resource}" {{\n  value = "{acronym}${{lower(local.convention, "-", "")}}"\n  description = "Naming convention for the resource {resource}.  This resource requires lowercase values only."\n}}\n\n'

def format_alphanumeric_underscore_only(resource, acronym):
    return f'output "{resource}" {{\n  value = "{acronym}${{lower(replace(local.convention, "_", ""))}}"\n  description = "Naming convention for the resource {resource}.  This resource requires alphanumeric and underscore values only."\n}}\n\n'

def build_resource_acronyms(resource_list=[]):
    """
    Automatically generate unique naming conventions for resources.
    """
    resource_acronyms = {}

    for resource in resource_list:
        resource_name_components = resource.lower().replace("azurerm_", "").split("_")
        resource_name_last = resource_name_components[-1]
        if len(resource_name_components) == 1:
            resource_base_acronym = resource_name_components[0][:3]
        else:
            resource_base_acronym = [word[0] for word in resource_name_components]
            resource_base_acronym = ''.join(resource_base_acronym)

        counter = 2
        acronym = resource_base_acronym

        print(f'Generating acronym for {resource}.')
        while acronym in resource_acronyms:
            print(f'{acronym} cannot be used for {resource} because it already is used by {resource_acronyms[acronym]}.')
            acronym = resource_base_acronym[:-1] + resource_name_last[:counter]
            print(f'Trying to use the acronym {acronym}.')
            counter += 1

        print(f'The acronym {acronym} was generated for {resource}.')
        resource_acronyms[acronym] = resource

    return resource_acronyms

def build_terraform_output_file(acronym_dictionary={}):
    """
    Creates a Terraform outputs.tf file that contains the naming conventions.
    """
    with open("outputs.tf", 'a') as terraform_outputs:
        terraform_outputs.truncate(0)
        for acronym, resource in acronym_dictionary.items():
            if resource in alphanumeric_lowercase_only:
                terraform_outputs.write(format_alphanumeric_lowercase_only(resource=resource, acronym=acronym))
            elif resource in alphanumeric_only or resource in length_restricted:
                terraform_outputs.write(format_alphanumeric_only(resource=resource, acronym=acronym))
            elif resource in lowercase_only:
                terraform_outputs.write(format_lowercase_only(resource=resource, acronym=acronym))
            elif resource in alphanumeric_underscore_only:
                terraform_outputs.write(format_alphanumeric_underscore_only(resource=resource, acronym=acronym))
            else:
                terraform_outputs.write(format_standard(resource=resource, acronym=acronym))

    return terraform_outputs

output = build_resource_acronyms(resource_list=resource_list)
build_terraform_output_file(output)