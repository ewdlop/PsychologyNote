from psychopy import visual, event, core

win = visual.Window([800, 600], color="black")
text_stim = visual.TextStim(win, text="Remember this word: APPLE", color="white")
text_stim.draw()
win.flip()
core.wait(2)

# 假裝延遲測試後，詢問參與者
win.flip()
question = visual.TextStim(win, text="What was the word?", color="white")
question.draw()
win.flip()

response = event.waitKeys(keyList=["a", "b", "c"])  # 假設記錄按鍵
print(response)
win.close()
