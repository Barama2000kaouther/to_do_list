document.addEventListener("DOMContentLoaded", function () {

  const tasks = document.querySelectorAll('.task_container');
  tasks.forEach(item => {
    item.addEventListener('click', () => {
      const taskId = item.dataset.id;
      const url = item.dataset.url;
      const p = item.querySelector('p');
      const csrf = document.getElementById('csrf').value; // works here
      if (!p) return;
      const text = p.textContent;
      const html_content = `<form method='POST' action="${url}">
                                 <input type="hidden" name="csrfmiddlewaretoken" value="${csrf}">
                                 <input type='text' name='update_task' value="${text}">
                               </form>`;
      console.log(taskId);
      item.innerHTML = html_content;
    });
  });

});