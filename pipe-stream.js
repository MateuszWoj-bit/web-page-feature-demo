const fs = require("fs");

const readableStream = fs.createReadStream("input.txt", "utf-8");
const writableStream = fs.createWriteStream("output.txt", "utf-8");

readableStream.pipe(writableStream);

readableStream.on("error", (error) => {
  console.error(`Read Error: ${error.message}`);
});

writableStream.on("finish", () => {
  console.log("Write operation finished");
});

writableStream.on("error", (error) => {
  console.error(`Write Error: ${error.message}`);
});
