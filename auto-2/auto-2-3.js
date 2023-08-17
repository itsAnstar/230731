// 输入链接
const url = 'https://www.douyin.com/video/7267922371716074767';

// 加载页面  
fetch(url)
  .then(response => {
    
    // 获取页面网络请求
    const networkRequests = performance.getEntriesByType('resource');

    // 找到最大的请求
    const maxRequest = networkRequests.reduce((a, b) => {
      return a.transferSize > b.transferSize ? a : b;
    });
    
    // 返回结果 
    return maxRequest.name;

  })
  .then(maxUrl => {
    // maxUrl就是最大请求的链接
    console.log(maxUrl); 
  });