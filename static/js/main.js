let add_folder = document.getElementById('add_folder');
let form1 = document.getElementById('form1');
let add_folder_h2 = document.getElementById('add_folder_h2');

add_folder.addEventListener('click', function() {
    add_folder.classList.toggle('add_folder_active');
    if (add_folder.classList.contains('add_folder_active')) {
        add_folder_h2.innerHTML = "Yangi papka qo'shish <i class='fa-solid fa-chevron-up'></i>";
        form1.style.display = "flex";
    } else {
        add_folder_h2.innerHTML = "Yangi papka qo'shish <i class='fa-solid fa-chevron-down'></i>";
        form1.style.display = "none";
    }
    
});

let add_money = document.getElementById('add_money');
let add_money_h2 = document.getElementById('add_money_h2');

add_money.addEventListener('click', function() {
    add_money.classList.toggle('add_money_active');
    if (add_money.classList.contains('add_money_active')) {
        add_money_h2.innerHTML = "Yangi pul qo'shish <i class='fa-solid fa-chevron-up'></i>";
    } else {
        add_money_h2.innerHTML = "Yangi pul qo'shish <i class='fa-solid fa-chevron-down'></i>";
    }
    
});