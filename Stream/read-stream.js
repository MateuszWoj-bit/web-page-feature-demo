const fs = require("fs");

const readableStream = fs.createReadStream("input.txt", "utf-8");

readableStream.on("data", (chunk) => {
  console.log(`Received chunk: ${chunk}`);
});

readableStream.on("end", () => {
  console.log("End of stream");
});

readableStream.on("error", (error) => {
  console.error(`Error: ${error.message}`);
});
