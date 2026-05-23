async function updateVisitorCount() {
    try {
        const response = await fetch(
            'https://YOUR-API-ID.execute-api.us-east-1.amazonaws.com/prod/count'
        );
        const data = await response.json();
        document.getElementById('visitor-count').textContent = data.count;
    } catch (error) {
        console.error('Counter error:', error);
        document.getElementById('visitor-count').textContent = '-';
    }
}

updateVisitorCount();