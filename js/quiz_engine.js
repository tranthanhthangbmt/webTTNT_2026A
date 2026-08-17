(function () {
  // Styles for the quiz
  const style = document.createElement('style');
  style.innerHTML = `
    .quiz-app {
      font-family: 'Inter', sans-serif;
      background: #fff;
      border: 1px solid #e1e4e8;
      border-radius: 12px;
      padding: 24px;
      margin-top: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .quiz-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      border-bottom: 1px solid #eee;
      padding-bottom: 15px;
    }
    .quiz-title {
      font-size: 18px;
      font-weight: 600;
      color: #333;
      margin: 0;
    }
    .quiz-progress {
      font-size: 14px;
      color: #666;
      font-weight: 500;
    }
    .quiz-badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      margin-bottom: 15px;
    }
    .badge-de { background: #e6f4ea; color: #1e8e3e; }
    .badge-tb { background: #fef7e0; color: #f29900; }
    .badge-kho { background: #fce8e6; color: #d93025; }
    
    .quiz-question-text {
      font-size: 16px;
      line-height: 1.6;
      color: #222;
      margin-bottom: 20px;
    }
    
    .quiz-options {
      display: grid;
      grid-template-columns: 1fr;
      grid-auto-rows: 1fr; /* Mọi lựa chọn sẽ có cùng chiều cao với lựa chọn cao nhất */
      gap: 12px;
      margin-bottom: 25px;
    }
    
    .quiz-option {
      display: flex;
      align-items: center;
      padding: 12px 16px;
      border: 2px solid #eaedf0;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .quiz-option:hover { background: #f8f9fa; }
    .quiz-option input { margin-right: 12px; transform: scale(1.2); }
    
    .quiz-option.correct {
      border-color: #34a853;
      background: #e6f4ea;
    }
    .quiz-option.incorrect {
      border-color: #ea4335;
      background: #fce8e6;
    }
    .quiz-option.disabled {
      pointer-events: none;
      opacity: 0.8;
    }
    
    .quiz-dropdown {
      padding: 10px;
      font-size: 15px;
      border: 2px solid #eaedf0;
      border-radius: 6px;
      outline: none;
      min-width: 200px;
    }
    .quiz-dropdown:focus { border-color: #1a73e8; }
    .quiz-dropdown.correct { border-color: #34a853; background: #e6f4ea; }
    .quiz-dropdown.incorrect { border-color: #ea4335; background: #fce8e6; }
    
    .quiz-feedback {
      padding: 15px;
      border-radius: 8px;
      background: #e8f0fe;
      border-left: 4px solid #1a73e8;
      color: #1a73e8;
      font-size: 15px;
      line-height: 1.5;
      margin-bottom: 20px;
      display: none;
    }
    .quiz-feedback.show { display: block; animation: fadeIn 0.3s; }
    
    .quiz-controls {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid #eee;
      padding-top: 20px;
    }
    
    .quiz-btn {
      padding: 10px 20px;
      border: none;
      border-radius: 6px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.2s;
    }
    .quiz-btn-nav { background: #f1f3f4; color: #3c4043; }
    .quiz-btn-nav:hover:not(:disabled) { background: #e8eaed; }
    .quiz-btn-nav:disabled { opacity: 0.5; cursor: not-allowed; }
    
    .quiz-btn-check { background: #1a73e8; color: #fff; }
    .quiz-btn-check:hover:not(:disabled) { background: #1557b0; }
    
    .quiz-result { text-align: center; padding: 30px 10px; }
    .quiz-score { font-size: 36px; font-weight: 700; color: #1a73e8; margin-bottom: 10px; }
    .quiz-score-text { font-size: 18px; color: #555; margin-bottom: 30px; }
    
    @keyframes fadeIn { from { opacity: 0; transform: translateY(-5px); } to { opacity: 1; transform: translateY(0); } }
  `;
  document.head.appendChild(style);

  window.initQuiz = function (container) {
    const chapterId = container.getAttribute('data-chapter');
    if (!chapterId) return;

    let questions = [];
    let currentIndex = 0;
    let score = 0;
    // Track states of each question: { firstTry: true, answeredCorrectly: false, userSelection: null, currentOrder: null }
    let qStates = [];

    // Loading State
    container.innerHTML = '<div style="padding: 30px; text-align: center; color: #666;">Đang tải dữ liệu trắc nghiệm...</div>';

    fetch(`quizzes/chapter_${chapterId}.json`)
      .then(res => {
        if (!res.ok) throw new Error("File not found");
        return res.json();
      })
      .then(data => {
        // Map difficulty to sort order
        const diffMap = { "Dễ": 1, "Trung bình": 2, "Khó": 3 };
        questions = data.sort((a, b) => diffMap[a.difficulty] - diffMap[b.difficulty]);
        
        qStates = questions.map(() => ({ firstTry: true, answeredCorrectly: false, userSelection: null, currentOrder: null }));
        
        renderQuizApp();
      })
      .catch(err => {
        container.innerHTML = `<div style="padding: 20px; color: #ea4335; border: 1px solid #ea4335; border-radius: 8px;">Không thể tải bài tập trắc nghiệm cho chương này (quizzes/chapter_${chapterId}.json).</div>`;
      });

    function renderQuizApp() {
      container.innerHTML = `
        <div class="quiz-app">
          <div class="quiz-header">
            <h3 class="quiz-title">Bài tập Trắc nghiệm</h3>
            <div class="quiz-progress">Câu <span id="quiz-curr">1</span> / ${questions.length}</div>
          </div>
          <div id="quiz-body"></div>
          <div class="quiz-controls">
            <button id="quiz-btn-prev" class="quiz-btn quiz-btn-nav">< Câu trước</button>
            <button id="quiz-btn-check" class="quiz-btn quiz-btn-check" style="display: none;">Kiểm tra</button>
            <button id="quiz-btn-next" class="quiz-btn quiz-btn-nav">Câu sau ></button>
          </div>
        </div>
      `;
      
      document.getElementById('quiz-btn-prev').addEventListener('click', () => {
        if (currentIndex > 0) { currentIndex--; updateView(); }
      });
      
      document.getElementById('quiz-btn-next').addEventListener('click', () => {
        if (currentIndex < questions.length - 1) { 
          currentIndex++; updateView(); 
        } else {
          showResults();
        }
      });
      
      updateView();
    }

    function updateView() {
      const q = questions[currentIndex];
      const state = qStates[currentIndex];
      
      document.getElementById('quiz-curr').textContent = currentIndex + 1;
      const prevBtn = document.getElementById('quiz-btn-prev');
      const nextBtn = document.getElementById('quiz-btn-next');
      const checkBtn = document.getElementById('quiz-btn-check');
      
      prevBtn.disabled = (currentIndex === 0);
      nextBtn.textContent = (currentIndex === questions.length - 1) ? "Hoàn thành" : "Câu sau >";
      
      let badgeClass = "badge-de";
      if (q.difficulty === "Trung bình") badgeClass = "badge-tb";
      if (q.difficulty === "Khó") badgeClass = "badge-kho";

      let bodyHTML = `
        <div class="quiz-badge ${badgeClass}">${q.difficulty}</div>
        <div class="quiz-question-text">${q.question}</div>
      `;
      
      // Render options based on type
      if (q.type === 'single_choice' || q.type === 'true_false') {
        checkBtn.style.display = 'none';
        bodyHTML += `<div class="quiz-options">`;
        q.options.forEach((opt, idx) => {
          bodyHTML += `
            <label class="quiz-option" id="opt-lbl-${idx}">
              <input type="radio" name="quiz-radio" value="${idx}">
              <span>${opt}</span>
            </label>
          `;
        });
        bodyHTML += `</div>`;
      } else if (q.type === 'multiple_select') {
        checkBtn.style.display = 'block';
        bodyHTML += `<div class="quiz-options">`;
        q.options.forEach((opt, idx) => {
          bodyHTML += `
            <label class="quiz-option" id="opt-lbl-${idx}">
              <input type="checkbox" value="${idx}">
              <span>${opt}</span>
            </label>
          `;
        });
        bodyHTML += `</div>`;
      } else if (q.type === 'fill_blank') {
        checkBtn.style.display = 'block';
        bodyHTML += `<div style="margin-bottom: 25px;">`;
        bodyHTML += `<select id="quiz-select" class="quiz-dropdown">
          <option value="" disabled selected> ▼ Chọn từ... </option>`;
        q.options.forEach((opt, idx) => {
          bodyHTML += `<option value="${idx}">${opt}</option>`;
        });
        bodyHTML += `</select></div>`;
      } else if (q.type === 'matching') {
        checkBtn.style.display = 'block';
        if (!state.matchingRightOptions) {
           state.matchingRightOptions = q.pairs.map(p => p.right).sort(() => Math.random() - 0.5);
        }
        bodyHTML += `<div class="quiz-options">`;
        q.pairs.forEach((pair, idx) => {
          bodyHTML += `
            <div class="quiz-option" style="cursor: default; display: flex; justify-content: space-between; gap: 10px; align-items: center;">
              <div style="flex: 1; font-weight: 500;">${pair.left}</div>
              <select class="quiz-dropdown quiz-matching-sel" data-idx="${idx}" style="flex: 1; max-width: 50%;">
                <option value="" disabled selected> ▼ Chọn... </option>
                ${state.matchingRightOptions.map(r => `<option value="${r.replace(/"/g, '&quot;')}">${r}</option>`).join('')}
              </select>
            </div>
          `;
        });
        bodyHTML += `</div>`;
      } else if (q.type === 'ordering') {
        checkBtn.style.display = 'block';
        if (!state.currentOrder) {
           state.currentOrder = q.items.map((it, idx) => ({text: it, origIdx: idx})).sort(() => Math.random() - 0.5);
        }
        bodyHTML += `<div class="quiz-options" id="quiz-ordering-list"></div>`;
      }

      bodyHTML += `<div id="quiz-feedback" class="quiz-feedback">${q.feedback || 'Chính xác!'}</div>`;
      document.getElementById('quiz-body').innerHTML = bodyHTML;
      
      attachEvents(q, state);
    }
    
    function attachEvents(q, state) {
      const checkBtn = document.getElementById('quiz-btn-check');
      const feedbackDiv = document.getElementById('quiz-feedback');
      
      // Restore state if already answered correctly
      if (state.answeredCorrectly) {
        feedbackDiv.classList.add('show');
        if (q.type === 'single_choice' || q.type === 'true_false') {
          const lbl = document.getElementById(`opt-lbl-${state.userSelection}`);
          if(lbl) lbl.classList.add('correct');
          document.querySelectorAll('input[name="quiz-radio"]').forEach(r => r.disabled = true);
        } else if (q.type === 'fill_blank') {
          const sel = document.getElementById('quiz-select');
          sel.value = state.userSelection;
          sel.disabled = true;
          sel.classList.add('correct');
          checkBtn.style.display = 'none';
        } else if (q.type === 'multiple_select') {
          q.options.forEach((_, idx) => {
            if(q.answer.includes(idx)) {
               document.getElementById(`opt-lbl-${idx}`).classList.add('correct');
               document.querySelector(`input[type="checkbox"][value="${idx}"]`).checked = true;
            }
            document.querySelector(`input[type="checkbox"][value="${idx}"]`).disabled = true;
          });
          checkBtn.style.display = 'none';
        } else if (q.type === 'matching') {
          const selects = document.querySelectorAll('.quiz-matching-sel');
          selects.forEach((sel, i) => {
            sel.value = state.userSelection[i];
            sel.disabled = true;
            sel.classList.add('correct');
          });
          checkBtn.style.display = 'none';
        } else if (q.type === 'ordering') {
          const renderCorrectOrder = () => {
             const list = document.getElementById('quiz-ordering-list');
             if(!list) return;
             list.innerHTML = '';
             state.currentOrder.forEach((item, idx) => {
               list.innerHTML += `
                 <div class="quiz-option correct" style="cursor: default; display: flex; justify-content: space-between; gap: 10px;">
                   <span style="flex: 1;">${item.text}</span>
                 </div>
               `;
             });
          };
          renderCorrectOrder();
          checkBtn.style.display = 'none';
        }
        return;
      }

      // Render ordering bindings if ordering type
      if (q.type === 'ordering') {
        const renderOrder = () => {
           const list = document.getElementById('quiz-ordering-list');
           if (!list) return;
           list.innerHTML = '';
           state.currentOrder.forEach((item, idx) => {
             list.innerHTML += `
               <div class="quiz-option quiz-ordering-item" id="ord-item-${idx}" style="cursor: default; display: flex; justify-content: space-between; gap: 10px; align-items: center;">
                 <span style="flex: 1;">${item.text}</span>
                 <div style="display: flex; gap: 5px;" class="ord-controls">
                   <button class="quiz-btn quiz-btn-nav order-up" style="padding: 5px 10px; min-width: 40px;" data-idx="${idx}" ${idx===0 ? 'disabled' : ''}>⬆️</button>
                   <button class="quiz-btn quiz-btn-nav order-down" style="padding: 5px 10px; min-width: 40px;" data-idx="${idx}" ${idx===state.currentOrder.length-1 ? 'disabled' : ''}>⬇️</button>
                 </div>
               </div>
             `;
           });
           
           document.querySelectorAll('.order-up').forEach(btn => btn.onclick = function() {
              const i = parseInt(this.getAttribute('data-idx'));
              if(i > 0) {
                const temp = state.currentOrder[i-1];
                state.currentOrder[i-1] = state.currentOrder[i];
                state.currentOrder[i] = temp;
                renderOrder();
              }
           });
           document.querySelectorAll('.order-down').forEach(btn => btn.onclick = function() {
              const i = parseInt(this.getAttribute('data-idx'));
              if(i < state.currentOrder.length - 1) {
                const temp = state.currentOrder[i+1];
                state.currentOrder[i+1] = state.currentOrder[i];
                state.currentOrder[i] = temp;
                renderOrder();
              }
           });
        };
        renderOrder();
      }

      if (q.type === 'single_choice' || q.type === 'true_false') {
        const radios = document.querySelectorAll('input[name="quiz-radio"]');
        radios.forEach(radio => {
          radio.addEventListener('change', function() {
            const val = parseInt(this.value);
            const lbl = document.getElementById(`opt-lbl-${val}`);
            
            if (val === q.answer) {
              lbl.classList.add('correct');
              lbl.classList.remove('incorrect');
              feedbackDiv.classList.add('show');
              state.answeredCorrectly = true;
              state.userSelection = val;
              if (state.firstTry) score++;
              radios.forEach(r => r.disabled = true); // Lock after correct
            } else {
              lbl.classList.add('incorrect');
              state.firstTry = false;
            }
          });
        });
      } else if (q.type === 'multiple_select') {
        checkBtn.onclick = () => {
          const checkboxes = document.querySelectorAll('input[type="checkbox"]');
          let selected = [];
          checkboxes.forEach(c => {
             if(c.checked) selected.push(parseInt(c.value));
             // reset colors
             document.getElementById(`opt-lbl-${c.value}`).classList.remove('incorrect', 'correct');
          });
          
          // Check if identical arrays
          const correctAns = [...q.answer].sort();
          const userAns = [...selected].sort();
          const isCorrect = JSON.stringify(correctAns) === JSON.stringify(userAns);
          
          if (isCorrect) {
             selected.forEach(v => document.getElementById(`opt-lbl-${v}`).classList.add('correct'));
             feedbackDiv.classList.add('show');
             state.answeredCorrectly = true;
             if (state.firstTry) score++;
             checkboxes.forEach(c => c.disabled = true);
             checkBtn.style.display = 'none';
          } else {
             selected.forEach(v => {
                if(!correctAns.includes(v)) document.getElementById(`opt-lbl-${v}`).classList.add('incorrect');
             });
             state.firstTry = false;
          }
        };
      } else if (q.type === 'fill_blank') {
        checkBtn.onclick = () => {
          const sel = document.getElementById('quiz-select');
          const val = parseInt(sel.value);
          sel.classList.remove('incorrect', 'correct');
          
          if (isNaN(val)) return;
          
          if (val === q.answer) {
             sel.classList.add('correct');
             feedbackDiv.classList.add('show');
             state.answeredCorrectly = true;
             state.userSelection = val;
             if (state.firstTry) score++;
             sel.disabled = true;
             checkBtn.style.display = 'none';
          } else {
             sel.classList.add('incorrect');
             state.firstTry = false;
          }
        };
      } else if (q.type === 'matching') {
        checkBtn.onclick = () => {
          const selects = document.querySelectorAll('.quiz-matching-sel');
          let allCorrect = true;
          let allSelected = true;
          selects.forEach(sel => {
            if(!sel.value) allSelected = false;
          });
          if(!allSelected) return; // Wait until all are selected
          
          selects.forEach(sel => {
            const idx = parseInt(sel.getAttribute('data-idx'));
            const correctVal = q.pairs[idx].right;
            sel.classList.remove('incorrect', 'correct');
            if (sel.value === correctVal) {
              sel.classList.add('correct');
            } else {
              sel.classList.add('incorrect');
              allCorrect = false;
            }
          });
          
          if (allCorrect) {
             feedbackDiv.classList.add('show');
             state.answeredCorrectly = true;
             state.userSelection = Array.from(selects).map(s => s.value);
             if (state.firstTry) score++;
             selects.forEach(sel => sel.disabled = true);
             checkBtn.style.display = 'none';
          } else {
             state.firstTry = false;
          }
        };
      } else if (q.type === 'ordering') {
        checkBtn.onclick = () => {
           let allCorrect = true;
           state.currentOrder.forEach((item, idx) => {
              const el = document.getElementById(`ord-item-${idx}`);
              el.classList.remove('incorrect', 'correct');
              if (item.origIdx === idx) {
                 el.classList.add('correct');
              } else {
                 el.classList.add('incorrect');
                 allCorrect = false;
              }
           });
           if (allCorrect) {
              feedbackDiv.classList.add('show');
              state.answeredCorrectly = true;
              if (state.firstTry) score++;
              document.querySelectorAll('.ord-controls').forEach(el => el.style.display = 'none');
              checkBtn.style.display = 'none';
           } else {
              state.firstTry = false;
           }
        };
      }
    }
    
    function showResults() {
      const app = container.querySelector('.quiz-app');
      let msg = "Hoàn thành xuất sắc!";
      const ratio = score / questions.length;
      if (ratio < 0.5) msg = "Cần cố gắng học kỹ lý thuyết hơn nhé!";
      else if (ratio < 0.8) msg = "Khá tốt! Bạn đã nắm được cơ bản.";
      
      app.innerHTML = `
        <div class="quiz-result">
           <h3 class="quiz-title" style="margin-bottom: 20px;">Kết quả Trắc nghiệm</h3>
           <div class="quiz-score">${score} / ${questions.length}</div>
           <div class="quiz-score-text">${msg}</div>
           <button class="quiz-btn quiz-btn-check" onclick="initQuiz(document.querySelector('[data-chapter=\\'${chapterId}\\']'))">Làm lại từ đầu</button>
        </div>
      `;
    }
  };

  // Autoload for docsify
  window.$docsify = window.$docsify || {};
  window.$docsify.plugins = [].concat(
    function (hook, vm) {
      hook.doneEach(function () {
        document.querySelectorAll('#quiz-container').forEach(el => {
          window.initQuiz(el);
        });
      });
    },
    window.$docsify.plugins || []
  );
})();
