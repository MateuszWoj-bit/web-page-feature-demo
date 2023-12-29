const fs = require("fs");

const writableStream = fs.createWriteStream("output.txt", "utf-8");

writableStream.write("Hello, ");
writableStream.write("world!");
writableStream.end();

writableStream.on("finish", () => {
  console.log("Write operation finished");
});

writableStream.on("error", (error) => {
  console.error(`Error: ${error.message}`);
});
