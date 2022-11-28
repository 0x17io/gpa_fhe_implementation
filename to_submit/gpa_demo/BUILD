load("//transpiler:fhe.bzl", "fhe_cc_library")

fhe_cc_library(
    name = "gpa_demo",
        src = "gpa_demo.cc",
	    hdrs = ["calculator.h"],
	        encryption = "cleartext",
		    num_opt_passes = 2,
		        optimizer = "xls",
			)

cc_binary(
    name = "gpa_cleartext_test",
        srcs = ["gpa_cleartext_test.cc"],
	    deps = [
	          ":gpa_demo",
			 "//transpiler/data:cleartext_data",
				 "@com_google_absl//absl/container:fixed_array",
					 "@com_google_xls//xls/common/logging",
						 "@com_google_xls//xls/common/status:status_macros",
							 ],
							 )