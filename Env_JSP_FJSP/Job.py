import numpy as np
class Job:
    def __init__(self, idx, processing_machine, processing_time):
        self.idx = idx
        self.processing_machine = processing_machine
        self.processing_time = processing_time
        self.end = []
        self.cur_op = 0
        self.cur_pt = None
        self._on = []
        self.start = []
        self.endt = 0
        self.ope_num = len(self.processing_time)
        ope_mean_proc_time = []
        for i in range(self.ope_num):
            ope_mean_time = np.mean(self.processing_time[i])
            ope_mean_proc_time.append(ope_mean_time)
        total_mean_time = np.sum(ope_mean_proc_time)
        self.due_date = 0.5 * total_mean_time



    def get_next_info(self, Machine):
        m_idx = self.processing_machine[self.cur_op][Machine]
        self.cur_pt = self.processing_time[self.cur_op][Machine]
        return self.processing_time[self.cur_op][Machine], self.endt, m_idx

    def update(self, s, e, m_idx):  # s:工序开始时间，e:工序结束时间，m_idx:机器序号
        self.endt = e
        self.cur_op += 1
        self.start.append(s)
        self.end.append(e)
        self._on.append(m_idx)