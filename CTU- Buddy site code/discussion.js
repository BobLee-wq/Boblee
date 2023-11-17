document.addEventListener("DOMContentLoaded", function () {
    const expandBtns = document.querySelectorAll(".expand-btn");
    const modToolsDivs = document.querySelectorAll(".mod-tools");
    const form = document.querySelector("form");
    const discussionThreads = document.querySelector(".discussion-threads");
  
    expandBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        this.parentElement.classList.toggle("show-replies");
      });
    });
  
    modToolsDivs.forEach(function (div) {
      div.addEventListener("mouseenter", function () {
        this.parentElement.classList.add("show-mod-tools");
      });
  
      div.addEventListener("mouseleave", function () {
        this.parentElement.classList.remove("show-mod-tools");
      });
    });
  
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      const username = this.querySelector("#username").value;
      const question = this.querySelector("#question").value;
  
      if (username && question) {
        const newThread = createThread(username, question);
        discussionThreads.insertAdjacentHTML("afterbegin", newThread);
        this.reset();
        attachReplyFormEvents();
      }
    });
  
    function createThread(username, question) {
      return `
        <div class="thread">
          <div class="user-info">
            <img src="user-question.jpg" alt="User Question">
            <p>${username}</p>
          </div>
          <div class="thread-content">
            <h3>Question:</h3>
            <p>${question}</p>
            <a href="#" class="expand-btn">View Replies (0)</a>
            <div class="replies"></div>
            <div class="mod-tools">
              <a href="#" class="report-btn">Report</a>
              <a href="#" class="delete-btn">Delete</a>
            </div>
            <form class="reply-form">
              <label for="reply">Your Reply:</label>
              <textarea class="reply-textarea" rows="2"></textarea>
              <button type="submit">Submit Reply</button>
            </form>
          </div>
        </div>
      `;
    }
  
    function attachReplyFormEvents() {
      const replyForms = document.querySelectorAll(".reply-form");
      replyForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
          event.preventDefault();
          const replyTextarea = this.querySelector(".reply-textarea");
          const reply = replyTextarea.value;
          if (reply) {
            const newReply = `
              <div class="thread">
                <div class="user-info">
                  <img src="user-reply.jpg" alt="User Reply">
                  <p>Reply User</p>
                </div>
                <div class="thread-content">
                  <p>${reply}</p>
                  <div class="mod-tools">
                    <a href="#" class="report-btn">Report</a>
                    <a href="#" class="delete-btn">Delete</a>
                  </div>
                </div>
              </div>
            `;
            this.parentElement.querySelector(".replies").insertAdjacentHTML("beforeend", newReply);
            replyTextarea.value = "";
          }
        });
      });
    }
  
    // Attach events for reply forms initially
    attachReplyFormEvents();
  
    const newQuestionForm = document.getElementById("new-question-form");
    newQuestionForm.addEventListener("submit", function (event) {
      event.preventDefault();
      const newUsername = this.querySelector("#new-username").value;
      const newQuestion = this.querySelector("#new-question").value;
  
      if (newUsername && newQuestion) {
        const newThread = createThread(newUsername, newQuestion);
        discussionThreads.insertAdjacentHTML("afterbegin", newThread);
        this.reset();
        attachReplyFormEvents();
      }
    });
  });
  