package org.openapitools.codegen.python;

import static org.openapitools.codegen.languages.AbstractPythonConnexionServerCodegen.PYTHON_SRC_ROOT;
import static org.openapitools.codegen.languages.AbstractPythonConnexionServerCodegen.USE_PYTHON_SRC_ROOT_IN_IMPORTS;

import java.util.Collections;
import java.util.Map;

import com.google.common.collect.ImmutableMap;
import org.openapitools.codegen.CodegenConstants;
import org.openapitools.codegen.languages.AbstractPythonConnexionServerCodegen;
import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class AbstractPythonConnexionServerCodegenTest {

    /**
     * Passing "description" as first param to succinctly identify the significance of test parameters.
     */
    @Test(dataProvider = "data")
    public void test(String description, Map<String, Object> additionalProperties, String modelName,
                     ExpectedValues expectedValues) {
        AbstractPythonConnexionServerCodegen codegen = new MockAbstractPythonConnexionServerCodegen("", false);
        codegen.additionalProperties().putAll(additionalProperties);
        codegen.processOpts();
        Assert.assertEquals(codegen.apiPackage(), expectedValues.expectedApiPackage);
        Assert.assertEquals(codegen.modelFileFolder(), expectedValues.expectedModelFileFolder);
        Assert.assertEquals(codegen.apiFileFolder(), expectedValues.expectedApiFileFolder);
        Assert.assertEquals(codegen.toModelImport(modelName), expectedValues.expectedImport);
    }

    @DataProvider
    public Object[][] data() {
        return new Object[][]{
            new Object[]{
                "Default setup",
                Collections.emptyMap(),
                "TestModel",
                new ExpectedValues("from openapi_server.models.test_model import TestModel",
                    "openapi_server.controllers",
                    "generated-code/connexion/openapi_server/models",
                    "generated-code/connexion/openapi_server/controllers")
            },
            new Object[]{
                "Default setup with Python src root",
                ImmutableMap.of(PYTHON_SRC_ROOT, "test_root"),
                "TestModel",
                new ExpectedValues("from openapi_server.models.test_model import TestModel",
                    "openapi_server.controllers",
                    "generated-code/connexion/test_root/openapi_server/models",
                    "generated-code/connexion/test_root/openapi_server/controllers")
            },
            new Object[]{
                "Python src in import",
                ImmutableMap.of(PYTHON_SRC_ROOT, "test_root", USE_PYTHON_SRC_ROOT_IN_IMPORTS, "true"),
                "TestModel",
                new ExpectedValues("from test_root.openapi_server.models.test_model import TestModel",
                    "test_root.openapi_server.controllers",
                    "generated-code/connexion/test_root/openapi_server/models",
                    "generated-code/connexion/test_root/openapi_server/controllers")
            },
            new Object[]{
                "Python src in import with specified package",
                ImmutableMap.of(PYTHON_SRC_ROOT, "test_root",
                    USE_PYTHON_SRC_ROOT_IN_IMPORTS, "true",
                    CodegenConstants.PACKAGE_NAME, "test_package"),
                "TestModel",
                new ExpectedValues("from test_root.test_package.models.test_model import TestModel",
                    "test_root.test_package.controllers",
                    "generated-code/connexion/test_root/test_package/models",
                    "generated-code/connexion/test_root/test_package/controllers")
            }
        };
    }

    private static class MockAbstractPythonConnexionServerCodegen extends AbstractPythonConnexionServerCodegen {
        public MockAbstractPythonConnexionServerCodegen(String templateDirectory, boolean fixBodyNameValue) {
            super(templateDirectory, fixBodyNameValue);
        }
    }

    private static class ExpectedValues {
        public final String expectedImport;
        public final String expectedApiPackage;
        public final String expectedModelFileFolder;
        public final String expectedApiFileFolder;

        public ExpectedValues(String expectedImport, String expectedApiPackage, String expectedModelFileFolder,
                              String expectedApiFileFolder) {
            this.expectedImport = expectedImport;
            this.expectedApiPackage = expectedApiPackage;
            this.expectedModelFileFolder = expectedModelFileFolder;
            this.expectedApiFileFolder = expectedApiFileFolder;
        }
    }

}
