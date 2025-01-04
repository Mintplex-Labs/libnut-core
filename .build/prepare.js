const fs = require("fs");
const path = require("path");

const outputDir = path.join(__dirname, "../dist");
fs.mkdirSync(outputDir, { recursive: true });

const packageJson = require("../package.json");

if(process.platform === "win32" && process.arch === "arm64") {
  packageJson.name = `@mintplex-labs/libnut-winarm64`;
} else {
  packageJson.name = `@mintplex-labs/libnut-${process.platform}-${process.arch}`;
}

fs.writeFileSync(path.join(outputDir, "package.json"), JSON.stringify(packageJson, null, 2));
console.log(`Patched package name to '${packageJson.name}'`);

const rootFiles = [
  ".npmignore",
  "README.md",
  "LICENSE.md",
  "CHANGELOG.md",
  "index.d.ts",
  "index.js",
  "patch-packagename.js",
  "permissionCheck.js",
];

rootFiles.forEach(file => {
  console.log(`cp ${file} => ${path.join(outputDir, file)}`);
  fs.copyFileSync(path.join(__dirname, `../${file}`), path.join(outputDir, file));
});

console.log(`Copying Release NAPI files to ${outputDir}`);
const NAPI_FILES = [
"api-ms-win-crt-heap-l1-1-0.dll",
"api-ms-win-crt-runtime-l1-1-0.dll",
"api-ms-win-crt-string-l1-1-0.dll",
"libnut.exp",
"libnut.lib",
"libnut.node",
"msvcp140.dll",
"vcruntime140_1.dll",
"vcruntime140.dll",
]
fs.mkdirSync(path.join(outputDir, "build", "Release"), { recursive: true });
NAPI_FILES.forEach(file => {
  console.log(`cp ${file} => ${path.join(outputDir, "build", "Release", file)}`);
  fs.copyFileSync(path.join(__dirname, `../build/Release/${file}`), path.join(outputDir, "build", "Release", file));
});

console.log(`Done. cd dist; npm publish --access public`);

