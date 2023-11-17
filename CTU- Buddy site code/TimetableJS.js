document.addEventListener("DOMContentLoaded", function() {
    const subjects = document.querySelectorAll(".subject");
    
    subjects.forEach(subject => {
        subject.addEventListener("click", () => {
            alert(`You clicked on ${subject.textContent}`);
        });
    });
});

function addClass() {
    const time = prompt("Enter the time (e.g., 15:30):");
    if (time) {
        const day = prompt("Enter the day (e.g., Monday):");
        if (day) {
            let subjects = [];
            let subject;
            do {
                subject = prompt("Enter a subject for this time slot (or leave empty to finish):");
                if (subject) {
                    subjects.push(subject);
                }
            } while (subject !== null && subject !== "");

            if (subjects.length > 0) {
                const table = document.querySelector("table");
                const row = table.insertRow(table.rows.length - 1);
                row.innerHTML = `<td>${time}</td>`;
                subjects.forEach(subj => {
                    row.innerHTML += `<td class="subject">${subj}</td>`;
                });
            }
        }
    }
}

function getTimeColumnIndex(time) {
    const table = document.querySelector("table");
    const timeHeaders = Array.from(table.rows[0].cells).map(cell => cell.textContent);
    return timeHeaders.indexOf(time);
}

function getDayRowIndex(day) {
    const table = document.querySelector("table");
    const dayColumn = Array.from(table.rows).find(row => row.cells[0].textContent === day);
    return dayColumn ? dayColumn.rowIndex : -1;
}

function updateClock() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    const timeString = `${hours}:${minutes}:${seconds}`;
    document.getElementById('digital-clock').textContent = timeString;

    if (minutes === '00' && seconds === '00') {
        ringBell();
    }
}

setInterval(updateClock, 1000);

updateClock();

function ringBell() {
    const bellIcon = document.getElementById('bell-icon');
    bellIcon.classList.add('ring');
        
    setTimeout(() => {
        bellIcon.classList.remove('ring');
    }, 2000); 
}

setInterval(updateClock, 1000);

updateClock();

function addClass() {
    const time = prompt("Enter the time (e.g., 17:00):");
    if (time) {
        const day = prompt("Enter the day (e.g., Monday):");
        if (day) {
            const subject = prompt("Enter the subject:");
            if (subject) {
                const table = document.querySelector("table");
                const row = table.insertRow(table.rows.length);
                row.innerHTML = `<td>${time}</td><td class="subject">${subject}</td><td class="subject"></td><td class="subject"></td><td class="subject"></td><td class="subject"></td>`;
            }
        }
    }
}

const bellContainer = document.getElementById('bell-container');
const bellIcon = document.getElementById('bell-icon');

let timer;

bellContainer.addEventListener('click', () => {

    clearTimeout(timer);

    bellIcon.classList.add('ring');

    timer = setTimeout(() => {
        bellIcon.classList.remove('ring');
    }, 5000);
});

document.addEventListener("DOMContentLoaded", function() {
    const subjects = document.querySelectorAll(".subject");

    subjects.forEach(subject => {
        subject.addEventListener("click", () => {
            alert(`You clicked on ${subject.textContent}`);
        });
    });
});


    document.addEventListener("DOMContentLoaded", function () {
        const subjects = document.querySelectorAll(".subject");
    
        subjects.forEach(subject => {
            subject.addEventListener("dblclick", () => {
                const subjectText = subject.textContent.trim();
                switch (subjectText) {
                    case "Cloud Fundamentals":
                        subject.style.backgroundImage = 'url("Icons/CF.png")';
                        break;
                    case "Robotics":
                        subject.style.backgroundImage = 'url("Icons/RD.png")';
                        break;
                    case "Web Development":
                        subject.style.backgroundImage = 'url("Icons/CWD.png")';
                        break;
                    case "Ethics":
                        subject.style.backgroundImage = 'url("Icons/ENA.png")';
                        break;
                    default:
                        subject.style.backgroundImage = 'none';
                }
            });
        });
    });
    

document.getElementById('print-button').addEventListener('click', function() {
    Swal.fire({
        title: 'Print Timetable',
        text: 'Are you sure you want to print the timetable?',
        icon: 'info',
        showCancelButton: true,
        confirmButtonText: 'Print',
        cancelButtonText: 'Cancel',
    }).then((result) => {
        if (result.isConfirmed) {

            Swal.fire({
                title: 'Timetable Printed',
                text: 'Timetable has been printed and exported for offline use.',
                icon: 'success'
            });
            window.print();
        }
    });
});
document.getElementById('print-button').addEventListener('click', function() {

    var isConfirmed = window.confirm('Are you sure you want to print the timetable?');

    if (isConfirmed) {
        alert('Timetable has been printed and exported for offline use.');
        window.print();
    }
});




