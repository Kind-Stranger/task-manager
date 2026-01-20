async function loadTasks() {
    const res = await fetch('/tasks');
    const tasks = await res.json();

    const list = document.getElementById('task-list');
    list.innerHTML = '';

    tasks.forEach(t => {
        const li = document.createElement('li');
        li.textContent = t.title;

        const del = document.createElement('button');
        del.textContent = 'Delete';
        del.onclick = () => deleteTask(t.id);

        li.appendChild(del);
        list.appendChild(li);
    });
}

async function createTask() {
    const title = document.getElementById('task-title').value;

    await fetch('/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title })
    });

    loadTasks();
}

async function deleteTask(id) {
    await fetch(`/tasks/${id}`, { method: 'DELETE' });
    loadTasks();
}

loadTasks();

