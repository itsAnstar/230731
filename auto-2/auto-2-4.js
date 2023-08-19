import exceljs from 'exceljs/dist/exceljs.browser.js';

// 获取页面资源请求信息
const requests = performance.getEntriesByType('resource');

// 查找最大数据包
let maxPacket = null;
let maxPacketSize = 0;
for (let request of requests) {
  if (request.transferSize > maxPacketSize) {
    maxPacket = request;
    maxPacketSize = request.transferSize;
  }
}

// 创建Excel工作簿
let workbook = new ExcelJS.Workbook();
let worksheet = workbook.getWorksheet(1);

// 查找写入位置
let row = 1;
let col = 4;
while(worksheet.getCell(row, col).value) {
  row++;
}

// 写入最大数据包链接
worksheet.getCell(row, col).value = maxPacket.name;

// 生成Excel文件
workbook.xlsx.writeFile('packets.xlsx');