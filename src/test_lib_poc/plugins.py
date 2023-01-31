all_vars = set(dir())

# plugin references goes here

mocking_environment = "test_lib_poc.fixtures.mocking.environment_vars"
factories_altinn = "test_lib_poc.fixtures.factories.altinn_factory"
factories_gcp = "test_lib_poc.fixtures.factories.gcp_factories"
factories_file = "test_lib_poc.fixtures.factories.file_factory"

# create list of plugin reference names
temp_list = set(dir()) - all_vars
all_plugins = [eval(p) for p in temp_list if p != "all_vars"]

factory_plugins = [p for p in all_plugins if str(p).find(".fixtures.factories.") != -1]
mocking_plugins = [p for p in all_plugins if str(p).find(".fixtures.mocking.") != -1]
