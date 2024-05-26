## Домашнее задание SARSA

1. Был обновлен метод `update` в классе агента согласно правилу метода обучения

```python
def update(self, cur_state, new_state, action, reward):
    # В методе SARSA необходимо знать следующее действие, чтобы обновить данные в таблице 
    next_action = self.chooseAction(new_state)
    # Q(s, a)
    cur_q = self.q_table[tuple(cur_state)][action]
    # Q(s′,a′) - след состояние 
    next_q = self.q_table[tuple(new_state)][next_action]
    # Q(s,a) + α(r + γ * Q(s′,a′) − Q(s,a))
    self.q_table[tuple(cur_state)][action] += self.alpha * (reward + self.gamma * next_q - cur_q)
```

2. Демонстрация работы доступа в файле `./demo.mov`
