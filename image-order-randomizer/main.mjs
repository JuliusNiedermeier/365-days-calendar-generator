import { readdir, mkdir, copyFile } from "fs/promises";
import { prompt } from "./prompt.mjs";
import { shuffleArray } from "./shuffle.mjs";

const sourceDir = await prompt("Select source directory: ");
const sourceFileNames = await readdir(sourceDir);
console.log(`${sourceFileNames.length} files found in source directory.`);
const targetDir = await prompt("Name target directory: ");

await mkdir(targetDir);

const targetFileNames = shuffleArray(sourceFileNames).map(
  (fileName, index, array) => {
    const fileExtension = fileName.split(".").at(-1);
    const fileNameLength = array.length.toString().length;
    const newFileName = index.toString().padStart(fileNameLength, "0");
    return { source: fileName, target: [newFileName, fileExtension].join(".") };
  }
);

await Promise.all(
  targetFileNames.map(async (file) => {
    await copyFile(
      `${sourceDir}/${file.source}`,
      `${targetDir}/${file.target}`
    );
    console.log(`${sourceDir}/${file.source} -> ${targetDir}/${file.target}`);
  })
);
