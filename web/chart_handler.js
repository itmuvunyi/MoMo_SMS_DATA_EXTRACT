document.addEventListener('DOMContentLoaded', function() {
    fetch('../data/processed/dashboard.json')
        .then(response => response.json())
        .then(data => {
            renderCharts(data);
            renderTables(data);
        })
        .catch(error => console.error('Error fetching data:', error));
});

function renderCharts(data) {

    const ctx = document.getElementById('myChart').getContext('2d');
    const chartData = {
        labels: data.labels,
        datasets: [{
            label: 'Transaction Amounts',
            data: data.amounts,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    };

    const myChart = new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function renderTables(data) {
    const tableBody = document.getElementById('data-table-body');
    data.transactions.forEach(transaction => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${transaction.date}</td>
            <td>${transaction.amount}</td>
            <td>${transaction.category}</td>
            <td>${transaction.phone}</td>
        `;
        tableBody.appendChild(row);
    });
}