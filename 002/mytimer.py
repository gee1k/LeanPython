import time


class MyTimer:
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = '未开始定时器'
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        prompt = 'all总共运行了'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

    def start(self):
        self.begin = time.localtime()
        self.prompt = '请先停止计时'
        print('开始计时...')

    def stop(self):
        if not self.begin:
            print('请先开始计时！')
            return
        self.end = time.localtime()
        self._calc()
        self.begin = 0
        self.end = 0
        print('计时结束...')

    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if (self.lasted[index]):
                self.prompt += (str(self.lasted[index]) + self.unit[index])

        print(self.prompt)


t1 = MyTimer()
t1
t1.start()
time.sleep(5.0)
t1.stop()
print(t1)



t2 = MyTimer()
t2
t2.start()
time.sleep(3.0)
t2.stop()
print(t2)


print(t1 + t2)