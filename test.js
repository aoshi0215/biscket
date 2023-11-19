fetch('localhost:8000', {
  method: 'GET', // or 'POST'
  headers: {
    'Content-Type': 'application/json',
    // 'Authorization': 'Bearer your-token' (if needed)
  },
  // body: JSON.stringify(data), (if you have data to send with request)
})
.then(response => response.json())
.then(data => console.log(data))
.catch((error) => {
  console.error('Error:', error);
});
