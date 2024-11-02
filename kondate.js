document.getElementById('start-btn').addEventListener('click', function() {
    document.getElementById('title-screen').style.display = 'none';
    document.getElementById('menu-screen').style.display = 'block';
});

// ここに献立生成のロジックを追加
document.getElementById('generate-btn').addEventListener('click', function() {
    const budget = document.getElementById('budget').value;
    const menuList = document.getElementById('menu-list');
    menuList.innerHTML = ''; // 以前の献立をクリア

    // 例として、固定の献立を追加
    if (budget) {
        const exampleMenu = [
            { name: '鶏の照り焼き', cost: 500 },
            { name: '野菜炒め', cost: 300 },
            { name: '味噌汁', cost: 200 },
            { name: 'ご飯', cost: 100 }
        ];

        exampleMenu.forEach(item => {
            if (item.cost <= budget) {
                const li = document.createElement('li');
                li.textContent = `${item.name} - ¥${item.cost}`;
                menuList.appendChild(li);
            }
        });
    }
});
