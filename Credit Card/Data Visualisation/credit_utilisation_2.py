import pandas as pd
import numpy as np
from tqdm import tqdm
tqdm.pandas()
df = pd.read_csv('./Credit_Card.csv')
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.boxplot([df[df['default.payment.next.month'] == 0]['AGE'], df[df['default.payment.next.month'] == 1]['AGE']], labels=['Not Default', 'Default'], patch_artist=True, showmeans=True)
plt.xlabel('Default Status')
plt.ylabel('Age (AGE)')
plt.title('Age vs. Default Status')
plt.show()

import pandas as pd
import numpy as np
from tqdm import tqdm
tqdm.pandas()
df = pd.read_csv('./Credit_Card.csv')
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.boxplot([df[df['default.payment.next.month'] == 0]['LIMIT_BAL'], df[df['default.payment.next.month'] == 1]['LIMIT_BAL']], labels=['Not Default', 'Default'], patch_artist=True, showmeans=True)
plt.xlabel('Default Status')
plt.ylabel('Credit Limit (LIMIT_BAL)')
plt.title('Credit Limit vs. Default Status')
plt.show()


import pandas as pd
import numpy as np
from tqdm import tqdm
tqdm.pandas()
df = pd.read_csv('./Credit_Card.csv')
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.bar(df['PAY_0'].unique(), df['PAY_0'].value_counts(), color=['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray', 'cyan', 'magenta', 'yellow', 'black'])
plt.xlabel('Payment Status (PAY_0)')
plt.ylabel('Frequency')
plt.title('Distribution of Payment Status (PAY_0)')
plt.show()


import pandas as pd
import numpy as np
from tqdm import tqdm
tqdm.pandas()
df = pd.read_csv('./Credit_Card.csv')
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
for i in df['PAY_0'].unique():
    plt.bar(i,df[df['default.payment.next.month'] == 0]['PAY_0'].value_counts()[i], label='Not Default', color='blue')
    plt.bar(i,df[df['default.payment.next.month'] == 1]['PAY_0'].value_counts()[i], label='Default', color='red', bottom=df[df['default.payment.next.month'] == 0]['PAY_0'].value_counts()[i])
plt.xlabel('Payment Status (PAY_0)')
plt.ylabel('Frequency')
plt.title('Payment Status vs. Default Status')
plt.legend()
plt.show()