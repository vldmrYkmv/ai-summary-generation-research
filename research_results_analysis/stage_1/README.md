<h1>Results for the first research experiment</h1>

[Українською](README_ukr.md)

<b>Shortcuts:</b>
<ul>
    <li><b>TS</b> - Text Score</li>
    <li><b>IS-D</b> - Image Score - Dalle</li>
    <li><b>IS-SD</b> - Image Score - SD</li>
    <li><b>IS-MJ</b> - Image Score - MidJourney</li>
    <li><b>Ln</b> - Length</li>
</ul>

<h2>1. Scores for all test pages and books</h2>
<table>
  <tr>
    <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
  </tr>
  <tr>
    <td colspan="26">
      Alexandre Dumas and Auguste Maquet - The Count of Monte Cristo
    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="5">Random page  1</td>
    <td colspan="5">Random page 2</td>
    <td colspan="5">Random page 3</td>
    <td colspan="5">Random page 4</td>
    <td colspan="5">Random page 5</td>
  </tr>
  <tr>
    <td>co-occurance-semantic</td><td>4</td><td>10</td><td>6</td><td>7</td><td>5</td><td>4</td><td>10</td><td>5</td><td>4</td><td>2</td><td>6</td><td>10</td><td>7</td><td>3</td><td>5</td><td>6</td><td>10</td><td>7</td><td>3</td><td>6</td><td>3</td><td>10</td><td>2</td><td>2</td><td>2</td>
  </tr>
  <tr>
    <td>openapi-sum-gpt-3</td><td>10</td><td>29</td><td>9</td><td>7</td><td>9</td><td>10</td><td>37</td><td>8</td><td>6</td><td>8</td><td>10</td><td>28</td><td>6</td><td>8</td><td>error</td><td>9</td><td>35</td><td>8</td><td>6</td><td>10</td><td>9</td><td>37</td><td>7</td><td>8</td><td>9</td>
  </tr>
  <tr>
    <td>openapi-keywords-gpt-3</td><td>6</td><td>10</td><td>7</td><td>4</td><td>4</td><td>5</td><td>10</td><td>2</td><td>2</td><td>2</td><td>6</td><td>10</td><td>7</td><td>7</td><td>7</td><td>7</td><td>10</td><td>7</td><td>5</td><td>5</td><td>3</td><td>10</td><td>2</td><td>2</td><td>2</td>
  </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>9</td><td>31</td><td>9</td><td>7</td><td>8</td><td>10</td><td>41</td><td>9</td><td>7</td><td>8</td><td>10</td><td>36</td><td>9</td><td>8</td><td>8</td><td>10</td><td>41</td><td>9</td><td>7</td><td>9</td><td>8</td><td>35</td><td>3</td><td>7</td><td>9</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>6</td><td>10</td><td>8</td><td>4</td><td>4</td><td>5</td><td>10</td><td>2</td><td>2</td><td>2</td><td>6</td><td>10</td><td>6</td><td>6</td><td>6</td><td>7</td><td>10</td><td>9</td><td>5</td><td>5</td><td>5</td><td>10</td><td>2</td><td>3</td><td>6</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>5</td><td>10</td><td>7</td><td>4</td><td>4</td><td>6</td><td>10</td><td>3</td><td>1</td><td>3</td><td>5</td><td>10</td><td>4</td><td>3</td><td>4</td><td>7</td><td>10</td><td>7</td><td>5</td><td>5</td><td>6</td><td>10</td><td>5</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>4</td><td>7</td><td>6</td><td>error</td><td>1</td><td>6</td><td>7</td><td>7</td><td>3</td><td>7</td><td>6</td><td>10</td><td>6</td><td>6</td><td>7</td><td>7</td><td>12</td><td>7</td><td>5</td><td>5</td><td>5</td><td>6</td><td>5</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>6</td><td>20</td><td>5</td><td>1</td><td>7</td><td>6</td><td>50</td><td>4</td><td>5</td><td>5</td><td>5</td><td>26</td><td>4</td><td>4</td><td>4</td><td>6</td><td>17</td><td>6</td><td>5</td><td>5</td><td>4</td><td>11</td><td>4</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>4</td><td>10</td><td>2</td><td>2</td><td>2</td><td>5</td><td>10</td><td>1</td><td>1</td><td>2</td><td>2</td><td>10</td><td>1</td><td>2</td><td>1</td><td>3</td><td>10</td><td>3</td><td>2</td><td>2</td><td>5</td><td>10</td><td>4</td><td>6</td><td>4</td>
    </tr>
    <tr>
        <td>wordnet</td><td>5</td><td>10</td><td>7</td><td>error</td><td>6</td><td>4</td><td>10</td><td>1</td><td>1</td><td>2</td><td>3</td><td>10</td><td>3</td><td>3</td><td>3</td><td>5</td><td>10</td><td>6</td><td>5</td><td>5</td><td>3</td><td>10</td><td>2</td><td>2</td><td>2</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Arthur Conan Doyle - The Sign of the Four</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>6</td><td>10</td><td>6</td><td>3</td><td>4</td><td>6</td><td>10</td><td>6</td><td>1</td><td>4</td><td>4</td><td>10</td><td>4</td><td>2</td><td>3</td><td>7</td><td>10</td><td>5</td><td>4</td><td>6</td><td>5</td><td>10</td><td>5</td><td>2</td><td>4</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>7</td><td>10</td><td>7</td><td>6</td><td>6</td><td>3</td><td>10</td><td>4</td><td>3</td><td>4</td><td>5</td><td>10</td><td>5</td><td>4</td><td>4</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>8</td><td>10</td><td>8</td><td>4</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>7</td><td>10</td><td>8</td><td>4</td><td>7</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td><td>3</td><td>10</td><td>2</td><td>2</td><td>2</td><td>5</td><td>10</td><td>6</td><td>4</td><td>7</td><td>3</td><td>10</td><td>1</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>10</td><td>36</td><td>7</td><td>4</td><td>7</td><td>8</td><td>37</td><td>1</td><td>1</td><td>4</td><td>9</td><td>27</td><td>5</td><td>4</td><td>5</td><td>9</td><td>31</td><td>7</td><td>8</td><td>9</td><td>10</td><td>42</td><td>10</td><td>6</td><td>8</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>9</td><td>26</td><td>3</td><td>7</td><td>6</td><td>7</td><td>38</td><td>3</td><td>2</td><td>3</td><td>9</td><td>32</td><td>3</td><td>3</td><td>6</td><td>9</td><td>42</td><td>6</td><td>5</td><td>6</td><td>9</td><td>29</td><td>9</td><td>5</td><td>7</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>4</td><td>10</td><td>6</td><td>3</td><td>4</td><td>3</td><td>10</td><td>3</td><td>1</td><td>2</td><td>3</td><td>10</td><td>4</td><td>2</td><td>2</td><td>3</td><td>10</td><td>3</td><td>2</td><td>3</td><td>2</td><td>11</td><td>1</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>7</td><td>9</td><td>6</td><td>4</td><td>4</td><td>3</td><td>3</td><td>3</td><td>2</td><td>3</td><td>7</td><td>8</td><td>5</td><td>4</td><td>5</td><td>2</td><td>4</td><td>2</td><td>2</td><td>2</td><td>4</td><td>8</td><td>3</td><td>2</td><td>2</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>5</td><td>80</td><td>4</td><td>2</td><td>6</td><td>6</td><td>80</td><td>4</td><td>1</td><td>2</td><td>6</td><td>50</td><td>7</td><td>4</td><td>5</td><td>6</td><td>44</td><td>3</td><td>4</td><td>5</td><td>8</td><td>44</td><td>9</td><td>4</td><td>7</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>3</td><td>10</td><td>1</td><td>1</td><td>3</td><td>4</td><td>10</td><td>3</td><td>1</td><td>3</td><td>2</td><td>11</td><td>1</td><td>1</td><td>1</td><td>3</td><td>11</td><td>3</td><td>2</td><td>2</td><td>3</td><td>11</td><td>1</td><td>1</td><td>2</td>
    </tr>
    <tr>
        <td>wordnet</td><td>6</td><td>10</td><td>4</td><td>3</td><td>7</td><td>5</td><td>10</td><td>2</td><td>1</td><td>2</td><td>3</td><td>10</td><td>2</td><td>1</td><td>1</td><td>4</td><td>10</td><td>4</td><td>2</td><td>4</td><td>3</td><td>10</td><td>2</td><td>2</td><td>2</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Bram Stoker - Dracula</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>6</td><td>11</td><td>5</td><td>6</td><td>7</td><td>6</td><td>10</td><td>7</td><td>5</td><td>6</td><td>6</td><td>10</td><td>6</td><td>5</td><td>5</td><td>6</td><td>10</td><td>7</td><td>5</td><td>6</td><td>5</td><td>10</td><td>3</td><td>2</td><td>4</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>5</td><td>10</td><td>1</td><td>1</td><td>1</td><td>6</td><td>10</td><td>8</td><td>6</td><td>7</td><td>6</td><td>10</td><td>5</td><td>5</td><td>5</td><td>6</td><td>10</td><td>6</td><td>6</td><td>6</td><td>5</td><td>10</td><td>5</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>5</td><td>10</td><td>5</td><td>4</td><td>4</td><td>5</td><td>10</td><td>2</td><td>5</td><td>5</td><td>5</td><td>10</td><td>6</td><td>4</td><td>5</td><td>6</td><td>10</td><td>6</td><td>6</td><td>6</td><td>5</td><td>10</td><td>6</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>10</td><td>29</td><td>9</td><td>7</td><td>8</td><td>10</td><td>30</td><td>1</td><td>2</td><td>2</td><td>9</td><td>29</td><td>7</td><td>5</td><td>6</td><td>9</td><td>19</td><td>9</td><td>4</td><td>8</td><td>9</td><td>22</td><td>5</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>10</td><td>33</td><td>6</td><td>8</td><td>8</td><td>10</td><td>33</td><td>7</td><td>7</td><td>7</td><td>10</td><td>54</td><td>7</td><td>5</td><td>6</td><td>10</td><td>43</td><td>6</td><td>7</td><td>8</td><td>10</td><td>38</td><td>7</td><td>6</td><td>7</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>6</td><td>12</td><td>7</td><td>6</td><td>8</td><td>7</td><td>10</td><td>6</td><td>7</td><td>7</td><td>5</td><td>10</td><td>6</td><td>4</td><td>4</td><td>6</td><td>14</td><td>6</td><td>5</td><td>6</td><td>5</td><td>13</td><td>2</td><td>2</td><td>2</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>5</td><td>5</td><td>5</td><td>6</td><td>7</td><td>6</td><td>7</td><td>3</td><td>3</td><td>6</td><td>5</td><td>7</td><td>5</td><td>4</td><td>4</td><td>5</td><td>9</td><td>5</td><td>3</td><td>3</td><td>6</td><td>10</td><td>6</td><td>4</td><td>error</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>8</td><td>41</td><td>8</td><td>7</td><td>9</td><td>5</td><td>68</td><td>5</td><td>3</td><td>5</td><td>5</td><td>42</td><td>1</td><td>1</td><td>2</td><td>5</td><td>55</td><td>1</td><td>1</td><td>1</td><td>4</td><td>26</td><td>1</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td><td>3</td><td>11</td><td>1</td><td>1</td><td>1</td><td>3</td><td>11</td><td>2</td><td>1</td><td>2</td><td>4</td><td>10</td><td>6</td><td>5</td><td>6</td><td>3</td><td>10</td><td>3</td><td>2</td><td>3</td>
    </tr>
    <tr>
        <td>wordnet</td><td>3</td><td>10</td><td>1</td><td>2</td><td>4</td><td>7</td><td>10</td><td>7</td><td>3</td><td>6</td><td>3</td><td>10</td><td>2</td><td>2</td><td>2</td><td>2</td><td>10</td><td>2</td><td>2</td><td>2</td><td>4</td><td>10</td><td>5</td><td>3</td><td>3</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Charles Dickens - A Christmas Carol in Prose; Being a Ghost Story of Christmas</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>5</td><td>10</td><td>7</td><td>5</td><td>7</td><td>8</td><td>10</td><td>7</td><td>4</td><td>5</td><td>8</td><td>10</td><td>9</td><td>7</td><td>8</td><td>4</td><td>10</td><td>2</td><td>2</td><td>2</td><td>7</td><td>10</td><td>9</td><td>4</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>10</td><td>10</td><td>10</td><td>9</td><td>9</td><td>8</td><td>10</td><td>10</td><td>5</td><td>8</td><td>8</td><td>10</td><td>7</td><td>6</td><td>7</td><td>3</td><td>10</td><td>1</td><td>2</td><td>2</td><td>7</td><td>10</td><td>9</td><td>5</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>8</td><td>10</td><td>8</td><td>7</td><td>8</td><td>6</td><td>10</td><td>8</td><td>5</td><td>5</td><td>8</td><td>10</td><td>5</td><td>6</td><td>7</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td><td>7</td><td>10</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>10</td><td>27</td><td>9</td><td>6</td><td>8</td><td>10</td><td>23</td><td>9</td><td>7</td><td>9</td><td>8</td><td>21</td><td>8</td><td>6</td><td>7</td><td>7</td><td>25</td><td>7</td><td>5</td><td>7</td><td>9</td><td>21</td><td>7</td><td>5</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>10</td><td>30</td><td>8</td><td>6</td><td>10</td><td>10</td><td>40</td><td>9</td><td>7</td><td>9</td><td>10</td><td>21</td><td>8</td><td>6</td><td>9</td><td>10</td><td>50</td><td>5</td><td>7</td><td>8</td><td>10</td><td>38</td><td>5</td><td>6</td><td>7</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>8</td><td>14</td><td>8</td><td>7</td><td>8</td><td>7</td><td>10</td><td>9</td><td>5</td><td>7</td><td>4</td><td>10</td><td>2</td><td>4</td><td>2</td><td>2</td><td>11</td><td>1</td><td>1</td><td>1</td><td>7</td><td>10</td><td>7</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>9</td><td>11</td><td>9</td><td>9</td><td>8</td><td>8</td><td>8</td><td>9</td><td>3</td><td>9</td><td>7</td><td>8</td><td>2</td><td>5</td><td>7</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>6</td><td>9</td><td>5</td><td>5</td><td>7</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>6</td><td>45</td><td>3</td><td>5</td><td>7</td><td>4</td><td>55</td><td>3</td><td>2</td><td>3</td><td>7</td><td>19</td><td>9</td><td>6</td><td>8</td><td>7</td><td>40</td><td>7</td><td>5</td><td>6</td><td>7</td><td>28</td><td>8</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>6</td><td>13</td><td>6</td><td>2</td><td>6</td><td>4</td><td>11</td><td>3</td><td>2</td><td>2</td><td>4</td><td>13</td><td>3</td><td>4</td><td>4</td><td>2</td><td>11</td><td>1</td><td>1</td><td>1</td><td>2</td><td>10</td><td>2</td><td>2</td><td>1</td>
    </tr>
    <tr>
        <td>wordnet</td><td>8</td><td>10</td><td>7</td><td>8</td><td>6</td><td>6</td><td>10</td><td>7</td><td>5</td><td>5</td><td>7</td><td>10</td><td>7</td><td>5</td><td>5</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td><td>8</td><td>10</td><td>8</td><td>8</td><td>7</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Daniel Defoe - The Life and Adventures of Robinson Crusoe</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>6</td><td>10</td><td>6</td><td>5</td><td>6</td><td>4</td><td>10</td><td>2</td><td>2</td><td>2</td><td>7</td><td>10</td><td>8</td><td>6</td><td>7</td><td>6</td><td>10</td><td>4</td><td>error</td><td>5</td><td>8</td><td>10</td><td>8</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>8</td><td>10</td><td>6</td><td>5</td><td>7</td><td>3</td><td>10</td><td>2</td><td>2</td><td>2</td><td>8</td><td>10</td><td>9</td><td>2</td><td>9</td><td>7</td><td>10</td><td>6</td><td>4</td><td>6</td><td>9</td><td>10</td><td>6</td><td>8</td><td>9</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>7</td><td>10</td><td>6</td><td>6</td><td>7</td><td>3</td><td>10</td><td>2</td><td>1</td><td>2</td><td>8</td><td>10</td><td>8</td><td>8</td><td>8</td><td>7</td><td>10</td><td>6</td><td>4</td><td>6</td><td>8</td><td>10</td><td>8</td><td>8</td><td>9</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>9</td><td>39</td><td>6</td><td>5</td><td>6</td><td>9</td><td>30</td><td>3</td><td>3</td><td>5</td><td>9</td><td>38</td><td>8</td><td>8</td><td>8</td><td>9</td><td>34</td><td>7</td><td>6</td><td>8</td><td>9</td><td>42</td><td>8</td><td>3</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>9</td><td>39</td><td>7</td><td>7</td><td>8</td><td>10</td><td>51</td><td>3</td><td>3</td><td>6</td><td>9</td><td>42</td><td>8</td><td>8</td><td>8</td><td>9</td><td>39</td><td>5</td><td>3</td><td>4</td><td>9</td><td>36</td><td>8</td><td>4</td><td>7</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>2</td><td>10</td><td>2</td><td>2</td><td>2</td><td>3</td><td>12</td><td>5</td><td>3</td><td>3</td><td>7</td><td>13</td><td>7</td><td>7</td><td>8</td><td>4</td><td>15</td><td>4</td><td>2</td><td>2</td><td>6</td><td>10</td><td>6</td><td>3</td><td>3</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>2</td><td>3</td><td>2</td><td>2</td><td>3</td><td>2</td><td>4</td><td>1</td><td>1</td><td>1</td><td>6</td><td>8</td><td>6</td><td>6</td><td>7</td><td>3</td><td>6</td><td>3</td><td>3</td><td>3</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>8</td><td>70</td><td>7</td><td>5</td><td>9</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>6</td><td>73</td><td>7</td><td>4</td><td>6</td><td>1</td><td>5</td><td>1</td><td>1</td><td>1</td><td>4</td><td>35</td><td>1</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>2</td><td>10</td><td>2</td><td>2</td><td>2</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td><td>4</td><td>10</td><td>5</td><td>1</td><td>4</td><td>3</td><td>10</td><td>1</td><td>1</td><td>1</td><td>5</td><td>12</td><td>4</td><td>3</td><td>3</td>
    </tr>
    <tr>
        <td>wordnet</td><td>5</td><td>10</td><td>5</td><td>5</td><td>6</td><td>5</td><td>10</td><td>1</td><td>5</td><td>1</td><td>5</td><td>10</td><td>5</td><td>4</td><td>5</td><td>3</td><td>10</td><td>3</td><td>3</td><td>3</td><td>5</td><td>10</td><td>6</td><td>3</td><td>3</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">F. Scott Fitzgerald - The Great Gatsby</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>4</td><td>11</td><td>2</td><td>2</td><td>2</td><td>5</td><td>10</td><td>4</td><td>5</td><td>5</td><td>7</td><td>10</td><td>8</td><td>6</td><td>7</td><td>7</td><td>10</td><td>7</td><td>6</td><td>7</td><td>7</td><td>10</td><td>7</td><td>6</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>7</td><td>10</td><td>7</td><td>6</td><td>7</td><td>5</td><td>10</td><td>5</td><td>3</td><td>3</td><td>6</td><td>10</td><td>6</td><td>5</td><td>6</td><td>6</td><td>10</td><td>4</td><td>6</td><td>6</td><td>8</td><td>10</td><td>8</td><td>8</td><td>8</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>6</td><td>10</td><td>6</td><td>3</td><td>6</td><td>6</td><td>10</td><td>6</td><td>5</td><td>7</td><td>7</td><td>10</td><td>7</td><td>5</td><td>7</td><td>8</td><td>10</td><td>7</td><td>7</td><td>8</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>8</td><td>36</td><td>7</td><td>7</td><td>7</td><td>8</td><td>37</td><td>3</td><td>3</td><td>3</td><td>8</td><td>24</td><td>7</td><td>5</td><td>7</td><td>9</td><td>31</td><td>4</td><td>8</td><td>8</td><td>10</td><td>34</td><td>7</td><td>9</td><td>9</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>9</td><td>52</td><td>4</td><td>7</td><td>6</td><td>10</td><td>42</td><td>2</td><td>3</td><td>5</td><td>8</td><td>52</td><td>6</td><td>6</td><td>6</td><td>10</td><td>39</td><td>4</td><td>5</td><td>8</td><td>10</td><td>37</td><td>7</td><td>7</td><td>8</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>3</td><td>10</td><td>3</td><td>3</td><td>3</td><td>4</td><td>10</td><td>2</td><td>2</td><td>2</td><td>6</td><td>12</td><td>6</td><td>4</td><td>6</td><td>4</td><td>10</td><td>4</td><td>3</td><td>4</td><td>7</td><td>10</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>3</td><td>7</td><td>3</td><td>3</td><td>3</td><td>5</td><td>7</td><td>5</td><td>4</td><td>4</td><td>4</td><td>3</td><td>6</td><td>4</td><td>6</td><td>6</td><td>6</td><td>7</td><td>7</td><td>7</td><td>4</td><td>5</td><td>2</td><td>3</td><td>4</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>5</td><td>43</td><td>4</td><td>4</td><td>4</td><td>5</td><td>65</td><td>2</td><td>2</td><td>2</td><td>4</td><td>52</td><td>1</td><td>1</td><td>1</td><td>4</td><td>34</td><td>3</td><td>1</td><td>3</td><td>4</td><td>56</td><td>1</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>5</td><td>10</td><td>3</td><td>1</td><td>3</td><td>6</td><td>11</td><td>5</td><td>5</td><td>4</td><td>3</td><td>10</td><td>1</td><td>1</td><td>1</td><td>3</td><td>11</td><td>2</td><td>1</td><td>2</td><td>4</td><td>12</td><td>2</td><td>2</td><td>2</td>
    </tr>
    <tr>
        <td>wordnet</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td><td>4</td><td>10</td><td>2</td><td>1</td><td>1</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td><td>4</td><td>10</td><td>2</td><td>2</td><td>2</td><td>3</td><td>10</td><td>2</td><td>error</td><td>2</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Franz Kafka - Metamorphosis</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>8</td><td>10</td><td>7</td><td>4</td><td>4</td><td>6</td><td>10</td><td>2</td><td>2</td><td>2</td><td>6</td><td>11</td><td>4</td><td>2</td><td>2</td><td>5</td><td>10</td><td>4</td><td>4</td><td>4</td><td>6</td><td>10</td><td>6</td><td>2</td><td>4</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>8</td><td>10</td><td>1</td><td>3</td><td>3</td><td>6</td><td>10</td><td>6</td><td>2</td><td>3</td><td>6</td><td>10</td><td>4</td><td>1</td><td>1</td><td>5</td><td>10</td><td>4</td><td>5</td><td>5</td><td>5</td><td>10</td><td>4</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>8</td><td>10</td><td>3</td><td>2</td><td>3</td><td>5</td><td>10</td><td>5</td><td>2</td><td>3</td><td>5</td><td>10</td><td>2</td><td>2</td><td>2</td><td>5</td><td>10</td><td>4</td><td>4</td><td>4</td><td>5</td><td>10</td><td>3</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>9</td><td>33</td><td>6</td><td>2</td><td>5</td><td>9</td><td>30</td><td>5</td><td>5</td><td>5</td><td>9</td><td>26</td><td>7</td><td>4</td><td>4</td><td>10</td><td>38</td><td>9</td><td>error</td><td>9</td><td>10</td><td>26</td><td>7</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>10</td><td>54</td><td>5</td><td>4</td><td>5</td><td>9</td><td>31</td><td>2</td><td>3</td><td>3</td><td>10</td><td>50</td><td>8</td><td>6</td><td>10</td><td>9</td><td>45</td><td>7</td><td>4</td><td>5</td><td>10</td><td>45</td><td>7</td><td>6</td><td>9</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>5</td><td>10</td><td>6</td><td>5</td><td>3</td><td>7</td><td>10</td><td>7</td><td>5</td><td>6</td><td>6</td><td>12</td><td>1</td><td>2</td><td>3</td><td>5</td><td>10</td><td>6</td><td>5</td><td>5</td><td>7</td><td>12</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>6</td><td>5</td><td>4</td><td>3</td><td>3</td><td>7</td><td>8</td><td>6</td><td>5</td><td>6</td><td>9</td><td>20</td><td>3</td><td>2</td><td>4</td><td>7</td><td>8</td><td>3</td><td>5</td><td>5</td><td>6</td><td>7</td><td>4</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>5</td><td>62</td><td>5</td><td>4</td><td>5</td><td>7</td><td>33</td><td>5</td><td>4</td><td>7</td><td>7</td><td>83</td><td>2</td><td>2</td><td>4</td><td>6</td><td>75</td><td>4</td><td>3</td><td>5</td><td>6</td><td>58</td><td>4</td><td>2</td><td>4</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>4</td><td>11</td><td>1</td><td>1</td><td>1</td><td>4</td><td>11</td><td>4</td><td>4</td><td>4</td><td>2</td><td>10</td><td>1</td><td>2</td><td>2</td><td>4</td><td>10</td><td>1</td><td>1</td><td>1</td><td>1</td><td>11</td><td>1</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <td>wordnet</td><td>4</td><td>10</td><td>4</td><td>4</td><td>4</td><td>6</td><td>10</td><td>5</td><td>5</td><td>6</td><td>4</td><td>10</td><td>2</td><td>2</td><td>2</td><td>4</td><td>10</td><td>4</td><td>3</td><td>4</td><td>5</td><td>10</td><td>4</td><td>2</td><td>5</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">H. G. Wells - The Time Machine</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>2</td><td>10</td><td>2</td><td>2</td><td>2</td><td>6</td><td>10</td><td>6</td><td>6</td><td>6</td><td>7</td><td>10</td><td>6</td><td>5</td><td>5</td><td>7</td><td>11</td><td>7</td><td>7</td><td>7</td><td>5</td><td>10</td><td>5</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>8</td><td>10</td><td>5</td><td>7</td><td>6</td><td>6</td><td>10</td><td>6</td><td>4</td><td>6</td><td>6</td><td>10</td><td>5</td><td>5</td><td>5</td><td>6</td><td>10</td><td>6</td><td>6</td><td>6</td><td>4</td><td>10</td><td>4</td><td>2</td><td>4</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>8</td><td>10</td><td>6</td><td>7</td><td>6</td><td>6</td><td>10</td><td>6</td><td>5</td><td>5</td><td>4</td><td>10</td><td>3</td><td>5</td><td>4</td><td>3</td><td>10</td><td>3</td><td>3</td><td>3</td><td>5</td><td>10</td><td>4</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>9</td><td>34</td><td>6</td><td>7</td><td>6</td><td>9</td><td>28</td><td>7</td><td>7</td><td>7</td><td>8</td><td>27</td><td>6</td><td>6</td><td>6</td><td>8</td><td>18</td><td>7</td><td>7</td><td>7</td><td>8</td><td>24</td><td>6</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>10</td><td>47</td><td>2</td><td>7</td><td>3</td><td>10</td><td>44</td><td>9</td><td>8</td><td>8</td><td>8</td><td>27</td><td>6</td><td>6</td><td>7</td><td>6</td><td>10</td><td>6</td><td>5</td><td>5</td><td>10</td><td>52</td><td>6</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>5</td><td>15</td><td>5</td><td>5</td><td>6</td><td>6</td><td>10</td><td>6</td><td>4</td><td>4</td><td>7</td><td>11</td><td>3</td><td>4</td><td>5</td><td>6</td><td>10</td><td>5</td><td>6</td><td>6</td><td>5</td><td>12</td><td>4</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>6</td><td>10</td><td>4</td><td>7</td><td>4</td><td>6</td><td>8</td><td>5</td><td>4</td><td>4</td><td>7</td><td>19</td><td>5</td><td>5</td><td>6</td><td>6</td><td>10</td><td>6</td><td>5</td><td>5</td><td>4</td><td>10</td><td>4</td><td>3</td><td>4</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>4</td><td>48</td><td>3</td><td>2</td><td>4</td><td>4</td><td>52</td><td>2</td><td>2</td><td>2</td><td>5</td><td>48</td><td>2</td><td>2</td><td>2</td><td>5</td><td>56</td><td>6</td><td>4</td><td>5</td><td>6</td><td>62</td><td>3</td><td>error</td><td>3</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td><td>5</td><td>11</td><td>5</td><td>4</td><td>5</td><td>5</td><td>13</td><td>6</td><td>4</td><td>5</td><td>4</td><td>10</td><td>4</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <td>wordnet</td><td>3</td><td>10</td><td>3</td><td>3</td><td>3</td><td>6</td><td>10</td><td>4</td><td>4</td><td>4</td><td>5</td><td>10</td><td>5</td><td>4</td><td>5</td><td>5</td><td>10</td><td>5</td><td>3</td><td>3</td><td>3</td><td>10</td><td>1</td><td>3</td><td>3</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">H. P. Lovecraft - At the mountains of madness</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>6</td><td>13</td><td>5</td><td>4</td><td>4</td><td>7</td><td>12</td><td>7</td><td>5</td><td>7</td><td>7</td><td>11</td><td>5</td><td>2</td><td>5</td><td>6</td><td>10</td><td>6</td><td>4</td><td>5</td><td>6</td><td>11</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>6</td><td>10</td><td>6</td><td>5</td><td>error</td><td>7</td><td>10</td><td>7</td><td>3</td><td>5</td><td>8</td><td>10</td><td>8</td><td>7</td><td>8</td><td>6</td><td>10</td><td>6</td><td>4</td><td>6</td><td>6</td><td>10</td><td>6</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>6</td><td>10</td><td>5</td><td>5</td><td>error</td><td>7</td><td>10</td><td>7</td><td>5</td><td>5</td><td>9</td><td>10</td><td>9</td><td>7</td><td>8</td><td>6</td><td>10</td><td>6</td><td>5</td><td>6</td><td>6</td><td>10</td><td>6</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>9</td><td>32</td><td>error</td><td>6</td><td>8</td><td>9</td><td>36</td><td>7</td><td>7</td><td>8</td><td>9</td><td>35</td><td>7</td><td>7</td><td>7</td><td>9</td><td>35</td><td>6</td><td>4</td><td>7</td><td>9</td><td>35</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>9</td><td>22</td><td>error</td><td>6</td><td>8</td><td>8</td><td>37</td><td>8</td><td>7</td><td>8</td><td>10</td><td>51</td><td>6</td><td>5</td><td>7</td><td>9</td><td>43</td><td>6</td><td>4</td><td>7</td><td>9</td><td>40</td><td>8</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>6</td><td>15</td><td>6</td><td>5</td><td>6</td><td>6</td><td>14</td><td>7</td><td>5</td><td>5</td><td>5</td><td>11</td><td>5</td><td>3</td><td>3</td><td>6</td><td>14</td><td>4</td><td>4</td><td>4</td><td>6</td><td>11</td><td>7</td><td>4</td><td>6</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>2</td><td>3</td><td>2</td><td>1</td><td>1</td><td>5</td><td>6</td><td>6</td><td>error</td><td>5</td><td>6</td><td>9</td><td>3</td><td>2</td><td>3</td><td>6</td><td>7</td><td>6</td><td>5</td><td>5</td><td>6</td><td>11</td><td>5</td><td>3</td><td>6</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>7</td><td>36</td><td>6</td><td>3</td><td>7</td><td>5</td><td>70</td><td>5</td><td>2</td><td>5</td><td>4</td><td>41</td><td>1</td><td>1</td><td>1</td><td>7</td><td>34</td><td>6</td><td>3</td><td>6</td><td>4</td><td>27</td><td>3</td><td>3</td><td>3</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>6</td><td>14</td><td>6</td><td>5</td><td>6</td><td>5</td><td>10</td><td>4</td><td>2</td><td>5</td><td>3</td><td>11</td><td>3</td><td>3</td><td>2</td><td>3</td><td>12</td><td>3</td><td>3</td><td>3</td><td>3</td><td>10</td><td>1</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <td>wordnet</td><td>6</td><td>15</td><td>5</td><td>5</td><td>6</td><td>5</td><td>10</td><td>5</td><td>4</td><td>4</td><td>3</td><td>10</td><td>1</td><td>1</td><td>1</td><td>2</td><td>10</td><td>2</td><td>2</td><td>2</td><td>7</td><td>10</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Herman Melville - Moby Dick; Or, The Whale</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>4</td><td>10</td><td>3</td><td>2</td><td>3</td><td>7</td><td>10</td><td>7</td><td>5</td><td>6</td><td>8</td><td>11</td><td>7</td><td>4</td><td>5</td><td>7</td><td>10</td><td>8</td><td>6</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>7</td><td>10</td><td>7</td><td>6</td><td>7</td><td>8</td><td>10</td><td>6</td><td>6</td><td>5</td><td>8</td><td>10</td><td>8</td><td>7</td><td>7</td><td>8</td><td>10</td><td>8</td><td>5</td><td>7</td><td>9</td><td>10</td><td>9</td><td>7</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>7</td><td>10</td><td>8</td><td>7</td><td>7</td><td>8</td><td>10</td><td>5</td><td>3</td><td>5</td><td>8</td><td>10</td><td>8</td><td>6</td><td>8</td><td>8</td><td>10</td><td>7</td><td>6</td><td>7</td><td>9</td><td>10</td><td>8</td><td>6</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>10</td><td>26</td><td>7</td><td>7</td><td>7</td><td>9</td><td>27</td><td>8</td><td>6</td><td>7</td><td>9</td><td>49</td><td>7</td><td>7</td><td>8</td><td>10</td><td>45</td><td>8</td><td>6</td><td>8</td><td>8</td><td>31</td><td>8</td><td>6</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>10</td><td>33</td><td>7</td><td>6</td><td>6</td><td>10</td><td>46</td><td>7</td><td>6</td><td>7</td><td>10</td><td>55</td><td>8</td><td>7</td><td>7</td><td>10</td><td>34</td><td>8</td><td>7</td><td>8</td><td>10</td><td>34</td><td>9</td><td>8</td><td>7</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>5</td><td>10</td><td>6</td><td>error</td><td>6</td><td>6</td><td>10</td><td>6</td><td>error</td><td>6</td><td>7</td><td>12</td><td>8</td><td>7</td><td>8</td><td>8</td><td>14</td><td>7</td><td>6</td><td>6</td><td>6</td><td>10</td><td>6</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>4</td><td>4</td><td>4</td><td>1</td><td>1</td><td>2</td><td>6</td><td>1</td><td>1</td><td>1</td><td>3</td><td>1</td><td>3</td><td>2</td><td>3</td><td>6</td><td>7</td><td>6</td><td>3</td><td>5</td><td>7</td><td>8</td><td>8</td><td>3</td><td>4</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>5</td><td>28</td><td>5</td><td>4</td><td>5</td><td>2</td><td>16</td><td>1</td><td>2</td><td>5</td><td>7</td><td>47</td><td>7</td><td>7</td><td>7</td><td>5</td><td>8</td><td>5</td><td>5</td><td>5</td><td>7</td><td>37</td><td>8</td><td>2</td><td>8</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td><td>2</td><td>10</td><td>3</td><td>1</td><td>error</td><td>2</td><td>10</td><td>2</td><td>2</td><td>2</td><td>4</td><td>11</td><td>error</td><td>1</td><td>4</td><td>2</td><td>12</td><td>1</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <td>wordnet</td><td>6</td><td>10</td><td>5</td><td>error</td><td>6</td><td>4</td><td>10</td><td>3</td><td>4</td><td>4</td><td>7</td><td>10</td><td>7</td><td>7</td><td>5</td><td>5</td><td>10</td><td>4</td><td>4</td><td>4</td><td>6</td><td>10</td><td>6</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Jack London - The Call of the Wild</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>7</td><td>10</td><td>2</td><td>5</td><td>3</td><td>7</td><td>10</td><td>6</td><td>6</td><td>6</td><td>7</td><td>10</td><td>3</td><td>error</td><td>3</td><td>7</td><td>10</td><td>7</td><td>6</td><td>7</td><td>7</td><td>11</td><td>7</td><td>7</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>8</td><td>10</td><td>7</td><td>8</td><td>8</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>8</td><td>10</td><td>6</td><td>7</td><td>7</td><td>8</td><td>10</td><td>8</td><td>error</td><td>8</td><td>9</td><td>10</td><td>8</td><td>8</td><td>9</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>8</td><td>10</td><td>7</td><td>6</td><td>6</td><td>7</td><td>10</td><td>7</td><td>6</td><td>7</td><td>8</td><td>10</td><td>8</td><td>6</td><td>7</td><td>8</td><td>10</td><td>8</td><td>7</td><td>8</td><td>9</td><td>10</td><td>8</td><td>8</td><td>9</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>9</td><td>23</td><td>8</td><td>7</td><td>7</td><td>10</td><td>46</td><td>6</td><td>7</td><td>7</td><td>9</td><td>23</td><td>7</td><td>8</td><td>7</td><td>10</td><td>37</td><td>7</td><td>7</td><td>7</td><td>10</td><td>48</td><td>10</td><td>8</td><td>9</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>10</td><td>30</td><td>8</td><td>8</td><td>8</td><td>9</td><td>58</td><td>8</td><td>8</td><td>7</td><td>10</td><td>40</td><td>8</td><td>8</td><td>9</td><td>10</td><td>35</td><td>8</td><td>7</td><td>8</td><td>10</td><td>37</td><td>6</td><td>8</td><td>9</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>9</td><td>10</td><td>7</td><td>6</td><td>6</td><td>7</td><td>10</td><td>5</td><td>6</td><td>6</td><td>5</td><td>10</td><td>3</td><td>3</td><td>3</td><td>6</td><td>10</td><td>2</td><td>6</td><td>6</td><td>7</td><td>14</td><td>2</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>4</td><td>7</td><td>1</td><td>1</td><td>1</td><td>6</td><td>6</td><td>5</td><td>6</td><td>6</td><td>4</td><td>7</td><td>3</td><td>2</td><td>error</td><td>4</td><td>5</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td><td>2</td><td>2</td><td>2</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>7</td><td>49</td><td>7</td><td>1</td><td>1</td><td>6</td><td>32</td><td>5</td><td>1</td><td>1</td><td>7</td><td>71</td><td>8</td><td>6</td><td>7</td><td>3</td><td>36</td><td>3</td><td>3</td><td>3</td><td>8</td><td>25</td><td>6</td><td>7</td><td>7</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>5</td><td>12</td><td>2</td><td>2</td><td>2</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td><td>3</td><td>10</td><td>1</td><td>1</td><td>1</td><td>3</td><td>10</td><td>1</td><td>1</td><td>1</td><td>2</td><td>10</td><td>2</td><td>error</td><td>2</td>
    </tr>
    <tr>
        <td>wordnet</td><td>6</td><td>10</td><td>6</td><td>5</td><td>4</td><td>6</td><td>10</td><td>6</td><td>6</td><td>6</td><td>6</td><td>10</td><td>3</td><td>3</td><td>3</td><td>5</td><td>10</td><td>3</td><td>3</td><td>3</td><td>6</td><td>10</td><td>6</td><td>4</td><td>6</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Jacob Grimm and Wilhelm Grimm - Grimms' Fairy Tales</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>7</td><td>10</td><td>7</td><td>5</td><td>6</td><td>7</td><td>12</td><td>7</td><td>6</td><td>6</td><td>7</td><td>10</td><td>7</td><td>5</td><td>6</td><td>7</td><td>11</td><td>6</td><td>5</td><td>5</td><td>6</td><td>12</td><td>6</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>8</td><td>10</td><td>7</td><td>5</td><td>6</td><td>8</td><td>10</td><td>8</td><td>7</td><td>7</td><td>9</td><td>10</td><td>5</td><td>6</td><td>7</td><td>8</td><td>10</td><td>8</td><td>7</td><td>8</td><td>8</td><td>10</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>9</td><td>10</td><td>9</td><td>7</td><td>9</td><td>8</td><td>10</td><td>6</td><td>4</td><td>6</td><td>9</td><td>10</td><td>8</td><td>7</td><td>8</td><td>8</td><td>10</td><td>7</td><td>7</td><td>7</td><td>7</td><td>10</td><td>8</td><td>5</td><td>8</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>10</td><td>35</td><td>9</td><td>7</td><td>8</td><td>8</td><td>23</td><td>7</td><td>7</td><td>6</td><td>10</td><td>58</td><td>7</td><td>7</td><td>8</td><td>9</td><td>23</td><td>7</td><td>7</td><td>7</td><td>9</td><td>31</td><td>3</td><td>8</td><td>9</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>10</td><td>64</td><td>8</td><td>7</td><td>8</td><td>9</td><td>35</td><td>6</td><td>6</td><td>6</td><td>9</td><td>33</td><td>6</td><td>7</td><td>7</td><td>9</td><td>34</td><td>7</td><td>7</td><td>7</td><td>9</td><td>32</td><td>4</td><td>8</td><td>9</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>7</td><td>10</td><td>6</td><td>6</td><td>6</td><td>7</td><td>13</td><td>7</td><td>5</td><td>6</td><td>6</td><td>12</td><td>6</td><td>5</td><td>5</td><td>7</td><td>15</td><td>7</td><td>7</td><td>7</td><td>7</td><td>13</td><td>7</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>4</td><td>10</td><td>3</td><td>3</td><td>2</td><td>7</td><td>10</td><td>7</td><td>6</td><td>7</td><td>6</td><td>5</td><td>6</td><td>6</td><td>6</td><td>4</td><td>9</td><td>2</td><td>3</td><td>3</td><td>7</td><td>14</td><td>5</td><td>5</td><td>7</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>5</td><td>26</td><td>3</td><td>1</td><td>3</td><td>8</td><td>24</td><td>8</td><td>8</td><td>8</td><td>5</td><td>34</td><td>5</td><td>6</td><td>5</td><td>5</td><td>31</td><td>2</td><td>2</td><td>2</td><td>5</td><td>29</td><td>5</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>2</td><td>10</td><td>2</td><td>2</td><td>2</td><td>4</td><td>10</td><td>1</td><td>1</td><td>1</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td><td>3</td><td>10</td><td>1</td><td>1</td><td>1</td><td>2</td><td>11</td><td>1</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <td>wordnet</td><td>6</td><td>10</td><td>5</td><td>5</td><td>5</td><td>5</td><td>10</td><td>5</td><td>5</td><td>5</td><td>7</td><td>10</td><td>5</td><td>6</td><td>6</td><td>7</td><td>10</td><td>6</td><td>6</td><td>6</td><td>7</td><td>10</td><td>7</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">James Fenimore Cooper - The Last of the Mohicans</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>4</td><td>10</td><td>4</td><td>4</td><td>4</td><td>6</td><td>10</td><td>6</td><td>4</td><td>2</td><td>6</td><td>10</td><td>3</td><td>2</td><td>6</td><td>7</td><td>11</td><td>5</td><td>5</td><td>5</td><td>7</td><td>10</td><td>6</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>7</td><td>10</td><td>7</td><td>6</td><td>7</td><td>4</td><td>10</td><td>3</td><td>4</td><td>4</td><td>8</td><td>10</td><td>7</td><td>8</td><td>8</td><td>7</td><td>10</td><td>8</td><td>7</td><td>7</td><td>7</td><td>10</td><td>6</td><td>6</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>8</td><td>10</td><td>6</td><td>8</td><td>8</td><td>7</td><td>10</td><td>error</td><td>4</td><td>4</td><td>9</td><td>10</td><td>8</td><td>8</td><td>8</td><td>8</td><td>10</td><td>7</td><td>7</td><td>8</td><td>7</td><td>10</td><td>7</td><td>7</td><td>8</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>9</td><td>18</td><td>9</td><td>9</td><td>9</td><td>7</td><td>30</td><td>6</td><td>6</td><td>6</td><td>10</td><td>36</td><td>8</td><td>9</td><td>9</td><td>9</td><td>29</td><td>6</td><td>5</td><td>6</td><td>9</td><td>30</td><td>6</td><td>3</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>10</td><td>44</td><td>9</td><td>8</td><td>9</td><td>9</td><td>49</td><td>6</td><td>5</td><td>6</td><td>10</td><td>36</td><td>8</td><td>6</td><td>9</td><td>9</td><td>32</td><td>7</td><td>6</td><td>7</td><td>9</td><td>38</td><td>7</td><td>5</td><td>7</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>7</td><td>12</td><td>7</td><td>3</td><td>3</td><td>4</td><td>11</td><td>4</td><td>2</td><td>3</td><td>7</td><td>11</td><td>8</td><td>6</td><td>8</td><td>6</td><td>12</td><td>6</td><td>6</td><td>2</td><td>7</td><td>11</td><td>1</td><td>error</td><td>7</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>6</td><td>6</td><td>5</td><td>5</td><td>5</td><td>3</td><td>5</td><td>3</td><td>2</td><td>3</td><td>7</td><td>5</td><td>6</td><td>6</td><td>8</td><td>2</td><td>3</td><td>1</td><td>1</td><td>1</td><td>6</td><td>6</td><td>7</td><td>6</td><td>7</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>8</td><td>33</td><td>6</td><td>8</td><td>8</td><td>3</td><td>21</td><td>3</td><td>3</td><td>3</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>7</td><td>57</td><td>8</td><td>5</td><td>8</td><td>6</td><td>61</td><td>7</td><td>5</td><td>7</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>2</td><td>10</td><td>1</td><td>2</td><td>2</td><td>4</td><td>11</td><td>4</td><td>2</td><td>2</td><td>4</td><td>10</td><td>2</td><td>2</td><td>2</td><td>6</td><td>12</td><td>5</td><td>6</td><td>7</td><td>3</td><td>10</td><td>1</td><td>2</td><td>error</td>
    </tr>
    <tr>
        <td>wordnet</td><td>7</td><td>10</td><td>6</td><td>7</td><td>8</td><td>5</td><td>10</td><td>3</td><td>3</td><td>3</td><td>5</td><td>10</td><td>2</td><td>2</td><td>2</td><td>7</td><td>10</td><td>7</td><td>6</td><td>6</td><td>6</td><td>10</td><td>3</td><td>3</td><td>6</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Jane Austen - Pride and Prejudice</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>8</td><td>10</td><td>8</td><td>7</td><td>7</td><td>7</td><td>11</td><td>7</td><td>6</td><td>6</td><td>8</td><td>10</td><td>8</td><td>6</td><td>5</td><td>7</td><td>10</td><td>7</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>7</td><td>10</td><td>8</td><td>6</td><td>7</td><td>6</td><td>10</td><td>6</td><td>5</td><td>5</td><td>8</td><td>10</td><td>6</td><td>6</td><td>7</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>8</td><td>10</td><td>3</td><td>8</td><td>8</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>7</td><td>10</td><td>6</td><td>7</td><td>6</td><td>8</td><td>10</td><td>7</td><td>7</td><td>7</td><td>7</td><td>10</td><td>7</td><td>6</td><td>7</td><td>7</td><td>10</td><td>3</td><td>7</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>8</td><td>21</td><td>6</td><td>7</td><td>7</td><td>9</td><td>27</td><td>8</td><td>7</td><td>7</td><td>9</td><td>23</td><td>7</td><td>5</td><td>7</td><td>10</td><td>21</td><td>8</td><td>8</td><td>8</td><td>9</td><td>19</td><td>9</td><td>7</td><td>9</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>10</td><td>63</td><td>10</td><td>7</td><td>8</td><td>10</td><td>36</td><td>8</td><td>8</td><td>9</td><td>9</td><td>35</td><td>6</td><td>7</td><td>7</td><td>10</td><td>35</td><td>8</td><td>6</td><td>7</td><td>10</td><td>29</td><td>10</td><td>9</td><td>9</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>7</td><td>12</td><td>7</td><td>7</td><td>8</td><td>8</td><td>10</td><td>9</td><td>8</td><td>8</td><td>7</td><td>11</td><td>7</td><td>6</td><td>7</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>4</td><td>10</td><td>2</td><td>2</td><td>2</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>6</td><td>6</td><td>5</td><td>5</td><td>6</td><td>8</td><td>16</td><td>6</td><td>8</td><td>7</td><td>7</td><td>8</td><td>6</td><td>6</td><td>7</td><td>4</td><td>4</td><td>5</td><td>4</td><td>5</td><td>5</td><td>6</td><td>4</td><td>2</td><td>2</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>6</td><td>41</td><td>5</td><td>4</td><td>5</td><td>7</td><td>40</td><td>7</td><td>6</td><td>6</td><td>7</td><td>59</td><td>7</td><td>6</td><td>7</td><td>7</td><td>48</td><td>8</td><td>4</td><td>7</td><td>3</td><td>22</td><td>5</td><td>error</td><td>6</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>6</td><td>10</td><td>2</td><td>2</td><td>2</td><td>4</td><td>10</td><td>4</td><td>4</td><td>4</td><td>3</td><td>11</td><td>1</td><td>1</td><td>1</td><td>6</td><td>11</td><td>3</td><td>6</td><td>6</td><td>5</td><td>10</td><td>1</td><td>1</td><td>5</td>
    </tr>
    <tr>
        <td>wordnet</td><td>6</td><td>10</td><td>6</td><td>5</td><td>5</td><td>7</td><td>10</td><td>3</td><td>7</td><td>5</td><td>3</td><td>10</td><td>2</td><td>4</td><td>2</td><td>6</td><td>10</td><td>1</td><td>7</td><td>3</td><td>2</td><td>10</td><td>1</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Jonathan Swift - Gullivers Travels</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>8</td><td>10</td><td>7</td><td>5</td><td>6</td><td>8</td><td>10</td><td>6</td><td>5</td><td>6</td><td>6</td><td>10</td><td>6</td><td>6</td><td>7</td><td>7</td><td>10</td><td>7</td><td>7</td><td>6</td><td>5</td><td>10</td><td>5</td><td>3</td><td>3</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>6</td><td>10</td><td>4</td><td>4</td><td>4</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>8</td><td>10</td><td>8</td><td>7</td><td>8</td><td>7</td><td>10</td><td>6</td><td>6</td><td>7</td><td>6</td><td>10</td><td>3</td><td>6</td><td>3</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>6</td><td>10</td><td>4</td><td>3</td><td>4</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>8</td><td>10</td><td>8</td><td>7</td><td>8</td><td>7</td><td>10</td><td>6</td><td>6</td><td>7</td><td>4</td><td>10</td><td>4</td><td>3</td><td>3</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>9</td><td>32</td><td>7</td><td>6</td><td>7</td><td>8</td><td>23</td><td>4</td><td>4</td><td>4</td><td>9</td><td>29</td><td>8</td><td>6</td><td>6</td><td>9</td><td>24</td><td>9</td><td>6</td><td>8</td><td>8</td><td>55</td><td>5</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>9</td><td>41</td><td>7</td><td>6</td><td>6</td><td>9</td><td>33</td><td>error</td><td>7</td><td>8</td><td>9</td><td>37</td><td>6</td><td>6</td><td>6</td><td>9</td><td>33</td><td>9</td><td>5</td><td>7</td><td>8</td><td>51</td><td>7</td><td>5</td><td>7</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>6</td><td>10</td><td>5</td><td>5</td><td>5</td><td>6</td><td>12</td><td>5</td><td>5</td><td>5</td><td>6</td><td>11</td><td>4</td><td>5</td><td>5</td><td>7</td><td>11</td><td>5</td><td>5</td><td>7</td><td>5</td><td>13</td><td>4</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>6</td><td>5</td><td>6</td><td>6</td><td>6</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>6</td><td>8</td><td>5</td><td>5</td><td>5</td><td>6</td><td>12</td><td>4</td><td>5</td><td>5</td><td>5</td><td>11</td><td>4</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>6</td><td>20</td><td>3</td><td>3</td><td>3</td><td>6</td><td>66</td><td>6</td><td>5</td><td>6</td><td>5</td><td>89</td><td>5</td><td>5</td><td>5</td><td>8</td><td>113</td><td>5</td><td>3</td><td>6</td><td>4</td><td>90</td><td>4</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>4</td><td>10</td><td>3</td><td>4</td><td>4</td><td>5</td><td>11</td><td>2</td><td>2</td><td>2</td><td>4</td><td>10</td><td>2</td><td>2</td><td>4</td><td>2</td><td>11</td><td>2</td><td>1</td><td>1</td><td>5</td><td>10</td><td>4</td><td>3</td><td>4</td>
    </tr>
    <tr>
        <td>wordnet</td><td>6</td><td>10</td><td>5</td><td>3</td><td>4</td><td>7</td><td>10</td><td>6</td><td>6</td><td>6</td><td>8</td><td>10</td><td>4</td><td>6</td><td>8</td><td>7</td><td>10</td><td>6</td><td>5</td><td>7</td><td>5</td><td>10</td><td>4</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Jules Verne - A Journey to the Centre of the Earth</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>7</td><td>10</td><td>7</td><td>5</td><td>7</td><td>8</td><td>10</td><td>7</td><td>5</td><td>5</td><td>6</td><td>11</td><td>6</td><td>6</td><td>6</td><td>8</td><td>10</td><td>7</td><td>7</td><td>8</td><td>7</td><td>10</td><td>6</td><td>5</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>6</td><td>10</td><td>6</td><td>6</td><td>6</td><td>8</td><td>10</td><td>7</td><td>5</td><td>7</td><td>9</td><td>10</td><td>6</td><td>6</td><td>6</td><td>8</td><td>10</td><td>8</td><td>7</td><td>8</td><td>7</td><td>10</td><td>7</td><td>5</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>7</td><td>10</td><td>5</td><td>5</td><td>6</td><td>8</td><td>10</td><td>8</td><td>7</td><td>8</td><td>7</td><td>10</td><td>9</td><td>5</td><td>6</td><td>7</td><td>10</td><td>7</td><td>5</td><td>5</td><td>8</td><td>10</td><td>8</td><td>7</td><td>9</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>9</td><td>56</td><td>8</td><td>6</td><td>8</td><td>10</td><td>28</td><td>5</td><td>5</td><td>7</td><td>9</td><td>31</td><td>8</td><td>7</td><td>8</td><td>9</td><td>24</td><td>7</td><td>7</td><td>8</td><td>10</td><td>37</td><td>7</td><td>4</td><td>9</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>9</td><td>41</td><td>7</td><td>8</td><td>8</td><td>10</td><td>28</td><td>6</td><td>6</td><td>8</td><td>9</td><td>28</td><td>7</td><td>4</td><td>5</td><td>9</td><td>31</td><td>8</td><td>8</td><td>8</td><td>9</td><td>19</td><td>7</td><td>8</td><td>8</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>6</td><td>14</td><td>5</td><td>4</td><td>5</td><td>8</td><td>12</td><td>6</td><td>6</td><td>6</td><td>6</td><td>12</td><td>6</td><td>6</td><td>6</td><td>8</td><td>10</td><td>7</td><td>8</td><td>8</td><td>7</td><td>12</td><td>5</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>6</td><td>5</td><td>6</td><td>6</td><td>6</td><td>5</td><td>4</td><td>6</td><td>5</td><td>5</td><td>6</td><td>11</td><td>6</td><td>6</td><td>6</td><td>6</td><td>4</td><td>7</td><td>6</td><td>8</td><td>2</td><td>3</td><td>2</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>8</td><td>84</td><td>5</td><td>6</td><td>7</td><td>6</td><td>41</td><td>5</td><td>5</td><td>5</td><td>6</td><td>18</td><td>6</td><td>6</td><td>6</td><td>7</td><td>55</td><td>6</td><td>5</td><td>6</td><td>6</td><td>34</td><td>5</td><td>5</td><td>4</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>6</td><td>11</td><td>6</td><td>3</td><td>6</td><td>5</td><td>11</td><td>3</td><td>3</td><td>3</td><td>6</td><td>14</td><td>6</td><td>6</td><td>6</td><td>6</td><td>10</td><td>6</td><td>3</td><td>3</td><td>5</td><td>12</td><td>2</td><td>2</td><td>2</td>
    </tr>
    <tr>
        <td>wordnet</td><td>5</td><td>10</td><td>5</td><td>5</td><td>5</td><td>6</td><td>10</td><td>6</td><td>5</td><td>5</td><td>6</td><td>10</td><td>6</td><td>5</td><td>6</td><td>7</td><td>10</td><td>7</td><td>6</td><td>7</td><td>6</td><td>10</td><td>4</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">L. Frank Baum - The Wonderful Wizard of Oz</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>9</td><td>10</td><td>9</td><td>6</td><td>9</td><td>8</td><td>10</td><td>7</td><td>7</td><td>7</td><td>6</td><td>10</td><td>6</td><td>5</td><td>5</td><td>9</td><td>11</td><td>9</td><td>6</td><td>7</td><td>8</td><td>12</td><td>8</td><td>5</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>9</td><td>10</td><td>8</td><td>6</td><td>9</td><td>8</td><td>10</td><td>6</td><td>6</td><td>6</td><td>7</td><td>10</td><td>7</td><td>7</td><td>6</td><td>7</td><td>10</td><td>6</td><td>6</td><td>6</td><td>8</td><td>10</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>9</td><td>10</td><td>7</td><td>7</td><td>7</td><td>9</td><td>10</td><td>7</td><td>7</td><td>7</td><td>7</td><td>10</td><td>7</td><td>6</td><td>6</td><td>7</td><td>10</td><td>7</td><td>6</td><td>6</td><td>7</td><td>10</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>10</td><td>20</td><td>8</td><td>9</td><td>9</td><td>9</td><td>27</td><td>8</td><td>6</td><td>5</td><td>9</td><td>41</td><td>7</td><td>5</td><td>6</td><td>10</td><td>28</td><td>8</td><td>5</td><td>7</td><td>9</td><td>35</td><td>7</td><td>6</td><td>8</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>10</td><td>23</td><td>9</td><td>7</td><td>9</td><td>10</td><td>42</td><td>7</td><td>6</td><td>8</td><td>10</td><td>37</td><td>8</td><td>6</td><td>6</td><td>10</td><td>38</td><td>5</td><td>5</td><td>6</td><td>10</td><td>40</td><td>9</td><td>6</td><td>8</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>8</td><td>10</td><td>8</td><td>6</td><td>7</td><td>6</td><td>12</td><td>6</td><td>3</td><td>3</td><td>6</td><td>11</td><td>6</td><td>error</td><td>5</td><td>6</td><td>12</td><td>6</td><td>6</td><td>5</td><td>5</td><td>11</td><td>5</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>8</td><td>5</td><td>9</td><td>6</td><td>6</td><td>7</td><td>6</td><td>7</td><td>6</td><td>6</td><td>6</td><td>9</td><td>6</td><td>6</td><td>6</td><td>6</td><td>4</td><td>7</td><td>5</td><td>5</td><td>9</td><td>16</td><td>7</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>4</td><td>22</td><td>3</td><td>3</td><td>3</td><td>7</td><td>96</td><td>7</td><td>6</td><td>6</td><td>5</td><td>29</td><td>5</td><td>4</td><td>6</td><td>7</td><td>66</td><td>6</td><td>3</td><td>6</td><td>6</td><td>27</td><td>5</td><td>6</td><td>7</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>9</td><td>11</td><td>8</td><td>6</td><td>6</td><td>6</td><td>10</td><td>6</td><td>4</td><td>6</td><td>3</td><td>11</td><td>2</td><td>3</td><td>3</td><td>6</td><td>10</td><td>6</td><td>6</td><td>7</td><td>6</td><td>11</td><td>6</td><td>4</td><td>5</td>
    </tr>
    <tr>
        <td>wordnet</td><td>7</td><td>10</td><td>6</td><td>6</td><td>6</td><td>5</td><td>10</td><td>5</td><td>5</td><td>5</td><td>6</td><td>10</td><td>6</td><td>5</td><td>5</td><td>6</td><td>10</td><td>7</td><td>5</td><td>6</td><td>4</td><td>10</td><td>4</td><td>3</td><td>4</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Lewis Carroll - Alice's Adventures in Wonderland</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>8</td><td>10</td><td>8</td><td>6</td><td>8</td><td>7</td><td>12</td><td>5</td><td>6</td><td>6</td><td>8</td><td>10</td><td>7</td><td>7</td><td>7</td><td>8</td><td>11</td><td>5</td><td>5</td><td>5</td><td>7</td><td>10</td><td>7</td><td>4</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>7</td><td>10</td><td>8</td><td>6</td><td>6</td><td>8</td><td>10</td><td>6</td><td>6</td><td>8</td><td>8</td><td>10</td><td>7</td><td>error</td><td>7</td><td>8</td><td>10</td><td>8</td><td>5</td><td>5</td><td>7</td><td>10</td><td>7</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>7</td><td>10</td><td>6</td><td>6</td><td>8</td><td>8</td><td>10</td><td>9</td><td>6</td><td>8</td><td>7</td><td>10</td><td>8</td><td>6</td><td>6</td><td>8</td><td>10</td><td>7</td><td>5</td><td>5</td><td>9</td><td>10</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>9</td><td>23</td><td>9</td><td>9</td><td>8</td><td>9</td><td>17</td><td>7</td><td>5</td><td>7</td><td>10</td><td>25</td><td>9</td><td>9</td><td>7</td><td>10</td><td>41</td><td>9</td><td>6</td><td>8</td><td>9</td><td>47</td><td>7</td><td>6</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>9</td><td>37</td><td>8</td><td>7</td><td>8</td><td>10</td><td>40</td><td>6</td><td>6</td><td>6</td><td>10</td><td>35</td><td>7</td><td>7</td><td>9</td><td>10</td><td>42</td><td>7</td><td>7</td><td>8</td><td>9</td><td>29</td><td>8</td><td>7</td><td>7</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>7</td><td>10</td><td>8</td><td>6</td><td>7</td><td>7</td><td>13</td><td>5</td><td>5</td><td>6</td><td>6</td><td>14</td><td>7</td><td>6</td><td>7</td><td>6</td><td>16</td><td>5</td><td>5</td><td>5</td><td>6</td><td>10</td><td>6</td><td>6</td><td>5</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>7</td><td>7</td><td>7</td><td>5</td><td>6</td><td>6</td><td>9</td><td>5</td><td>5</td><td>5</td><td>6</td><td>5</td><td>6</td><td>5</td><td>6</td><td>2</td><td>6</td><td>1</td><td>1</td><td>1</td><td>6</td><td>6</td><td>7</td><td>4</td><td>4</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>5</td><td>18</td><td>7</td><td>5</td><td>6</td><td>6</td><td>38</td><td>5</td><td>5</td><td>6</td><td>8</td><td>36</td><td>9</td><td>7</td><td>7</td><td>3</td><td>21</td><td>1</td><td>5</td><td>4</td><td>2</td><td>23</td><td>1</td><td>1</td><td>1</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>4</td><td>11</td><td>4</td><td>3</td><td>4</td><td>8</td><td>10</td><td>8</td><td>6</td><td>7</td><td>7</td><td>10</td><td>7</td><td>5</td><td>7</td><td>5</td><td>11</td><td>3</td><td>2</td><td>4</td><td>6</td><td>11</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>wordnet</td><td>6</td><td>10</td><td>6</td><td>5</td><td>5</td><td>8</td><td>10</td><td>6</td><td>6</td><td>6</td><td>8</td><td>10</td><td>8</td><td>5</td><td>7</td><td>5</td><td>10</td><td>5</td><td>5</td><td>5</td><td>6</td><td>10</td><td>6</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Oscar Wilde - The Picture of Dorian Gray</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>7</td><td>13</td><td>7</td><td>6</td><td>7</td><td>7</td><td>10</td><td>6</td><td>7</td><td>6</td><td>3</td><td>10</td><td>2</td><td>2</td><td>2</td><td>7</td><td>12</td><td>8</td><td>7</td><td>7</td><td>7</td><td>13</td><td>2</td><td>5</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>6</td><td>10</td><td>6</td><td>5</td><td>5</td><td>4</td><td>10</td><td>2</td><td>2</td><td>2</td><td>7</td><td>10</td><td>6</td><td>7</td><td>7</td><td>7</td><td>10</td><td>7</td><td>6</td><td>5</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>6</td><td>10</td><td>6</td><td>6</td><td>6</td><td>4</td><td>10</td><td>2</td><td>2</td><td>2</td><td>8</td><td>10</td><td>8</td><td>7</td><td>7</td><td>8</td><td>10</td><td>8</td><td>7</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>9</td><td>25</td><td>9</td><td>7</td><td>7</td><td>9</td><td>32</td><td>5</td><td>5</td><td>6</td><td>10</td><td>34</td><td>8</td><td>7</td><td>8</td><td>9</td><td>23</td><td>7</td><td>8</td><td>9</td><td>9</td><td>28</td><td>9</td><td>7</td><td>8</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>9</td><td>28</td><td>8</td><td>7</td><td>8</td><td>10</td><td>42</td><td>8</td><td>6</td><td>7</td><td>10</td><td>47</td><td>3</td><td>4</td><td>8</td><td>10</td><td>51</td><td>9</td><td>6</td><td>8</td><td>10</td><td>41</td><td>9</td><td>8</td><td>10</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>8</td><td>14</td><td>8</td><td>7</td><td>7</td><td>7</td><td>13</td><td>6</td><td>5</td><td>5</td><td>3</td><td>12</td><td>3</td><td>1</td><td>2</td><td>7</td><td>13</td><td>7</td><td>7</td><td>7</td><td>6</td><td>11</td><td>5</td><td>6</td><td>4</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>9</td><td>15</td><td>9</td><td>6</td><td>7</td><td>7</td><td>4</td><td>7</td><td>7</td><td>7</td><td>2</td><td>6</td><td>2</td><td>2</td><td>2</td><td>7</td><td>4</td><td>8</td><td>7</td><td>7</td><td>7</td><td>15</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>6</td><td>55</td><td>7</td><td>7</td><td>7</td><td>7</td><td>46</td><td>8</td><td>7</td><td>7</td><td>3</td><td>23</td><td>2</td><td>2</td><td>3</td><td>8</td><td>36</td><td>7</td><td>6</td><td>7</td><td>6</td><td>91</td><td>error</td><td>6</td><td>4</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>3</td><td>11</td><td>2</td><td>2</td><td>2</td><td>5</td><td>11</td><td>4</td><td>2</td><td>4</td><td>4</td><td>11</td><td>4</td><td>2</td><td>4</td><td>6</td><td>11</td><td>6</td><td>6</td><td>7</td><td>7</td><td>11</td><td>7</td><td>6</td><td>6</td>
    </tr>
    <tr>
        <td>wordnet</td><td>7</td><td>10</td><td>5</td><td>5</td><td>5</td><td>4</td><td>10</td><td>2</td><td>4</td><td>2</td><td>4</td><td>10</td><td>3</td><td>3</td><td>4</td><td>7</td><td>11</td><td>6</td><td>7</td><td>7</td><td>5</td><td>10</td><td>3</td><td>5</td><td>3</td>
    </tr>
    <tr>
        <th>Method</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th><th>TS</th><th>Ln</th><th>IS-D</th><th>IS-SD</th><th>IS-MJ</th>
    </tr>
    <tr>
        <td colspan="26">Robert Louis Stevenson - Treasure Island</td>
    </tr>
    <tr>
        <td>co-occurance-semantic</td><td>7</td><td>10</td><td>7</td><td>7</td><td>7</td><td>8</td><td>10</td><td>8</td><td>7</td><td>7</td><td>6</td><td>10</td><td>5</td><td>5</td><td>6</td><td>8</td><td>10</td><td>8</td><td>5</td><td>5</td><td>7</td><td>11</td><td>6</td><td>4</td><td>5</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-3</td><td>8</td><td>10</td><td>8</td><td>8</td><td>8</td><td>9</td><td>10</td><td>7</td><td>7</td><td>7</td><td>7</td><td>10</td><td>6</td><td>6</td><td>6</td><td>8</td><td>10</td><td>9</td><td>5</td><td>8</td><td>6</td><td>10</td><td>6</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <td>openapi-keywords-gpt-4</td><td>8</td><td>10</td><td>9</td><td>7</td><td>7</td><td>9</td><td>10</td><td>7</td><td>7</td><td>7</td><td>7</td><td>10</td><td>7</td><td>6</td><td>6</td><td>8</td><td>10</td><td>7</td><td>5</td><td>5</td><td>6</td><td>10</td><td>5</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-3</td><td>8</td><td>20</td><td>9</td><td>7</td><td>8</td><td>8</td><td>16</td><td>8</td><td>7</td><td>7</td><td>9</td><td>19</td><td>6</td><td>6</td><td>7</td><td>8</td><td>38</td><td>8</td><td>6</td><td>7</td><td>8</td><td>27</td><td>7</td><td>7</td><td>7</td>
    </tr>
    <tr>
        <td>openapi-sum-gpt-4</td><td>9</td><td>30</td><td>9</td><td>7</td><td>9</td><td>9</td><td>27</td><td>6</td><td>6</td><td>7</td><td>9</td><td>33</td><td>7</td><td>7</td><td>9</td><td>10</td><td>42</td><td>6</td><td>5</td><td>7</td><td>9</td><td>24</td><td>8</td><td>7</td><td>8</td>
    </tr>
    <tr>
        <td>textrank-algorithm</td><td>8</td><td>12</td><td>8</td><td>6</td><td>7</td><td>6</td><td>10</td><td>5</td><td>5</td><td>5</td><td>6</td><td>10</td><td>6</td><td>4</td><td>5</td><td>6</td><td>10</td><td>7</td><td>5</td><td>6</td><td>5</td><td>10</td><td>5</td><td>1</td><td>5</td>
    </tr>
    <tr>
        <td>tf-idf-keywords</td><td>7</td><td>5</td><td>7</td><td>7</td><td>7</td><td>5</td><td>6</td><td>5</td><td>4</td><td>4</td><td>5</td><td>6</td><td>5</td><td>2</td><td>5</td><td>6</td><td>7</td><td>5</td><td>3</td><td>6</td><td>6</td><td>9</td><td>6</td><td>5</td><td>5</td>
    </tr>
    <tr>
        <td>tf-idf-sum</td><td>6</td><td>32</td><td>5</td><td>5</td><td>5</td><td>7</td><td>45</td><td>6</td><td>5</td><td>4</td><td>6</td><td>41</td><td>6</td><td>6</td><td>6</td><td>4</td><td>29</td><td>4</td><td>5</td><td>5</td><td>5</td><td>57</td><td>6</td><td>2</td><td>2</td>
    </tr>
    <tr>
        <td>we-spacy</td><td>6</td><td>12</td><td>6</td><td>5</td><td>6</td><td>7</td><td>11</td><td>5</td><td>5</td><td>5</td><td>3</td><td>11</td><td>3</td><td>2</td><td>2</td><td>3</td><td>10</td><td>1</td><td>1</td><td>1</td><td>5</td><td>10</td><td>5</td><td>5</td><td>6</td>
    </tr>
    <tr>
        <td>wordnet</td><td>7</td><td>10</td><td>7</td><td>6</td><td>7</td><td>6</td><td>10</td><td>6</td><td>6</td><td>6</td><td>5</td><td>10</td><td>4</td><td>1</td><td>5</td><td>7</td><td>10</td><td>6</td><td>6</td><td>7</td><td>4</td><td>10</td><td>3</td><td>1</td><td>4</td>
    </tr>
</table>
</br>

<h2>2. Average score for generated book abstract by algorithm</h2>

| Book | Co-Occurance Semantic | OpenApi Summary GPT3 | OpenApi Keywords GPT3 | OpenApi Summary GPT4 | OpenApi Keywords GPT4 | TextRank | TF-IDF Keywords | TF-IDF Summary | WE spaCy | WordNet |
|------|-----------------------|----------------------|----------------------|----------------------|----------------------|----------|------------------|----------------|----------|---------|
| A. Dumas and A. Maquet - The Count of Monte Cristo | 4.6 | 9.6 | 5.4 | 9.4 | 5.8 | 5.8 | 5.6 | 5.4 | 3.8 | 4 |
| A. C. Doyle - The Sign of the Four | 5.6 | 9.2 | 6 | 8.6 | 4 | 3 | 4.6 | 6.2 | 3 | 4.2 |
| B. Stoker - Dracula | 5.8 | 9.4 | 5.6 | 10 | 5.2 | 5.8 | 5.4 | 5.4 | 3 | 3.8 |
| C. Dickens - A Christmas Carol in Prose; Being a Ghost Story of Christmas | 6.4 | 8.8 | 7.2 | 10 | 6.2 | 5.6 | 6.2 | 6.2 | 3.6 | 6.2 |
| D. Defoe - The Life and Adventures of Robinson Crusoe | 6.2 | 9 | 7 | 9.2 | 6.6 | 4.4 | 4 | 4 | 3.2 | 4.6 |
| F. S. Fitzgerald - The Great Gatsby | 6 | 7 | 6.4 | 9.4 | 6.8 | 4.8 | 4.4 | 4.4 | 4.2 | 3 |
| F. Kafka - Metamorphosis | 6.2 | 9.2 | 6 | 9.6 | 5.6 | 6 | 7 | 6.2 | 3 | 4.6 |
| H. G. Wells - The Time Machine | 5.4 | 8.2 | 6 | 8.8 | 5.2 | 5.8 | 5.8 | 4.8 | 3.6 | 4.4 |
| H. P. Lovecraft - At the mountains of madness | 6.4 | 9 | 6.6 | 9 | 6.8 | 5.8 | 5 | 5.4 | 4 | 4.6 |
| H. Melville - Moby Dick; Or, The Whale | 6.6 | 9.2 | 8 | 10 | 8 | 6.4 | 4.4 | 5.2 | 2.4 | 5.6 |
| J. London - The Call of the Wild | 7 | 9.4 | 8 | 9.8 | 8 | 6.8 | 4.6 | 6.2 | 3 | 5.8 |
| J. Grimm and W. Grimm - Grimms' Fairy Tales | 6.8 | 9.2 | 8.2 | 9.2 | 8.2 | 6.8 | 5.6 | 5.6 | 2.6 | 6.4 |
| J. F. Cooper - The Last of the Mohicans | 6 | 8.8 | 6.6 | 9.4 | 7.8 | 6.2 | 4.8 | 5 | 3.8 | 6 |
| J. Austen - Pride and Prejudice | 7.4 | 9 | 7.2 | 9.8 | 7.2 | 6.6 | 6 | 6 | 4.8 | 4.8 |
| J. Swift - Gullivers Travels | 6.8 | 8.6 | 6.8 | 8.8 | 6.4 | 6 | 6 | 5.8 | 4 | 6.6 |
| J. Verne - A Journey to the Centre of the Earth | 7.2 | 9.4 | 7.6 | 9.2 | 7.4 | 7 | 5 | 6.6 | 5.6 | 6 |
| L. F. Baum - The Wonderful Wizard of Oz | 8 | 9.4 | 7.8 | 10 | 7.8 | 6.2 | 7.2 | 5.8 | 6 | 5.6 |
| L. Carroll - Alice's Adventures in Wonderland | 7.6 | 9.4 | 7.6 | 9.6 | 7.8 | 6.4 | 5.4 | 4.8 | 6 | 6.6 |
| O. Wilde - The Picture of Dorian Gray | 6.2 | 9.2 | 6.2 | 9.8 | 6.6 | 6.2 | 6.4 | 6 | 5 | 5.4 |
| R. L. Stevenson - Treasure Island | 7.2 | 8.2 | 7.6 | 9.2 | 7.6 | 6.2 | 5.8 | 5.6 | 4.8 | 5.8 |
|  | Co-Occurance Semantic | OpenApi Summary GPT3 | OpenApi Keywords GPT3 | OpenApi Summary GPT4 | OpenApi Keywords GPT4 | TextRank | TF-IDF Keywords | TF-IDF Summary | WE spaCy | WordNet |
| AVG | 6.47 | 8.96 | 6.89 | 9.44 | 6.75 | 5.89 | 5.46 | 5.53 | 3.97 | 5.2 |

</br>
</br>
<img src="./average_score_book_algorithm_1.svg" width="800px"/>
</br>
<img src="./average_score_book_algorithm_2.svg" width="800px"/>
</br>
<img src="./average_score_book_algorithm_3.svg" width="800px"/>

<h2>3. Average score for images generated by Dall-e for book by algorithm</h2>

| Book | Co-Occurance Semantic | OpenApi Summary GPT3 | OpenApi Keywords GPT3 | OpenApi Summary GPT4 | OpenApi Keywords GPT4 | TextRank | TF-IDF Keywords | TF-IDF Summary | WE spaCy | WordNet |
|------|-----------------------|----------------------|----------------------|----------------------|----------------------|----------|------------------|----------------|----------|---------|
| A. Dumas and A. Maquet - The Count of Monte Cristo | 5.4 | 7.6 | 5 | 7.8 | 5.4 | 5.2 | 6.2 | 4.6 | 2.2 | 3.8 |
| A. C. Doyle - The Sign of the Four | 5.2 | 6 | 6.2 | 4.8 | 3.6 | 3.4 | 3.8 | 5.4 | 1.8 | 2.8 |
| B. Stoker - Dracula | 5.6 | 6.2 | 5 | 6.6 | 5 | 5.4 | 4.8 | 3.2 | 2.6 | 3.4 |
| C. Dickens - A Christmas Carol in Prose; Being a Ghost Story of Christmas | 6.8 | 8 | 7.4 | 7 | 5.8 | 5.4 | 5.2 | 6 | 3 | 6 |
| D. Defoe - The Life and Adventures of Robinson Crusoe | 5.6 | 6.4 | 5.8 | 6.2 | 6 | 4.8 | 3.8 | 3.4 | 2.6 | 4 |
| F. S. Fitzgerald - The Great Gatsby | 5.6 | 5.6 | 6 | 5.2 | 6.6 | 4.4 | 4.6 | 2.2 | 2.6 | 1.6 |
| F. Kafka - Metamorphosis | 4.6 | 5.8 | 3.8 | 5.8 | 3.4 | 5.4 | 4 | 4 | 1.6 | 3.8 |
| H. G. Wells - The Time Machine | 5.2 | 6.2 | 5.2 | 5.8 | 4.4 | 4.6 | 4.8 | 3.2 | 3.2 | 3.6 |
| H. P. Lovecraft - At the mountains of madness | 6 | 6.75 | 6.6 | 7 | 6.6 | 5.8 | 4.4 | 4.2 | 3.4 | 4 |
| H. Melville - Moby Dick; Or, The Whale | 6.4 | 7.6 | 7.6 | 7.8 | 7.2 | 6.6 | 4.4 | 5.2 | 1.75 | 5 |
| J. London - The Call of the Wild | 5 | 7.4 | 7.2 | 7.6 | 7.6 | 3.8 | 3 | 5.8 | 1.4 | 4.8 |
| J. Grimm and W. Grimm - Grimms' Fairy Tales | 6.6 | 6.6 | 7 | 6.2 | 7.6 | 6.6 | 4.6 | 4.6 | 1.2 | 5.6 |
| J. F. Cooper - The Last of the Mohicans | 4.8 | 7 | 6.2 | 7.4 | 7 | 5.2 | 4.4 | 5 | 2.6 | 4.2 |
| J. Austen - Pride and Prejudice | 7.4 | 7.6 | 6 | 8.4 | 6 | 6.4 | 5.2 | 6.4 | 2.2 | 2.6 |
| J. Swift - Gullivers Travels | 6.2 | 6.6 | 5.6 | 7.25 | 5.8 | 4.6 | 5.2 | 4.6 | 2.6 | 5 |
| J. Verne - A Journey to the Centre of the Earth | 6.6 | 7 | 6.8 | 7 | 7.4 | 5.8 | 5.4 | 5.4 | 4.6 | 5.6 |
| L. F. Baum - The Wonderful Wizard of Oz | 7.8 | 7.6 | 6.8 | 7.6 | 7 | 6.2 | 7.2 | 5.2 | 5.6 | 5.6 |
| L. Carroll - Alice's Adventures in Wonderland | 6.4 | 8.2 | 7.2 | 7.2 | 7.4 | 6.2 | 5.2 | 4.6 | 5.8 | 6.2 |
| O. Wilde - The Picture of Dorian Gray | 5 | 7.6 | 5.6 | 7.4 | 6.2 | 5.8 | 6.6 | 6 | 4.6 | 3.8 |
| R. L. Stevenson - Treasure Island | 6.8 | 7.6 | 7.2 | 7.2 | 7 | 6.2 | 5.6 | 5.4 | 4 | 5.2 |
|  | Co-Occurance Semantic | OpenApi Summary GPT3 | OpenApi Keywords GPT3 | OpenApi Summary GPT4 | OpenApi Keywords GPT4 | TextRank | TF-IDF Keywords | TF-IDF Summary | WE spaCy | WordNet |
| AVG | 5.95 | 6.97 | 6.21 | 6.86 | 6.15 | 5.39 | 4.92 | 4.72 | 2.97 | 4.33 |

</br>
</br>
<img src="./average_dalle_score_book_algorithm_1.svg" width="800px"/>
</br>
<img src="./average_dalle_score_book_algorithm_2.svg" width="800px"/>
</br>
<img src="./average_dalle_score_book_algorithm_3.svg" width="800px"/>

<h2>4. Average score for images generated by Stable Diffusion for book by algorithm</h2>

| Book | Co-Occurance Semantic | OpenApi Summary GPT3 | OpenApi Keywords GPT3 | OpenApi Summary GPT4 | OpenApi Keywords GPT4 | TextRank | TF-IDF Keywords | TF-IDF Summary | WE spaCy | WordNet |
|------|-----------------------|----------------------|----------------------|----------------------|----------------------|----------|------------------|----------------|----------|---------|
| A. Dumas and A. Maquet - The Count of Monte Cristo | 3.8 | 7 | 4 | 7.2 | 4 | 3.6 | 4.75 | 3.8 | 2.6 | 2.75 |
| A. C. Doyle - The Sign of the Four | 2.4 | 4.6 | 4.8 | 4.4 | 2.4 | 1.8 | 2.8 | 3 | 1.2 | 1.8 |
| B. Stoker - Dracula | 4.6 | 4.6 | 4.4 | 6.6 | 4.6 | 4.8 | 4 | 2.6 | 2 | 2.4 |
| C. Dickens - A Christmas Carol in Prose; Being a Ghost Story of Christmas | 4.4 | 5.8 | 5.4 | 6.4 | 5 | 4.4 | 4.6 | 4.6 | 2.2 | 5.4 |
| D. Defoe - The Life and Adventures of Robinson Crusoe | 4.75 | 5 | 4.2 | 5 | 5.4 | 3.4 | 3.8 | 2.4 | 1.6 | 4 |
| F. S. Fitzgerald - The Great Gatsby | 5 | 6.2 | 5.8 | 5.6 | 5.4 | 3.6 | 4.2 | 1.8 | 2 | 1.25 |
| F. Kafka - Metamorphosis | 2.8 | 4.25 | 3.2 | 4.6 | 2.8 | 4.6 | 3.8 | 3 | 1.8 | 3.2 |
| H. G. Wells - The Time Machine | 5 | 6.4 | 4.8 | 6.2 | 4.8 | 4.6 | 4.8 | 2.5 | 2.6 | 3.4 |
| H. P. Lovecraft - At the mountains of madness | 4.2 | 6 | 5 | 5.4 | 5.4 | 4.2 | 2.75 | 2.4 | 2.8 | 3.6 |
| H. Melville - Moby Dick; Or, The Whale | 4.8 | 6.4 | 6.2 | 6.8 | 5.6 | 6.333333333 | 2 | 4 | 1.2 | 5.25 |
| J. London - The Call of the Wild | 6 | 7.6 | 7 | 7.8 | 6.6 | 4.4 | 3 | 3.6 | 1.25 | 4.2 |
| J. Grimm and W. Grimm - Grimms' Fairy Tales | 5.4 | 7.2 | 6.2 | 7 | 6 | 5.6 | 4.6 | 4.4 | 1.2 | 5.4 |
| J. F. Cooper - The Last of the Mohicans | 4.2 | 6.4 | 6.2 | 6 | 6.8 | 4.25 | 4 | 4.4 | 2.8 | 4.2 |
| J. Austen - Pride and Prejudice | 6.2 | 6.8 | 6.4 | 7.4 | 6.8 | 6 | 5 | 5 | 2.8 | 4.8 |
| J. Swift - Gullivers Travels | 5.2 | 5.4 | 6 | 5.8 | 5.2 | 4.8 | 5.4 | 4 | 2.4 | 4.8 |
| J. Verne - A Journey to the Centre of the Earth | 5.6 | 5.8 | 5.8 | 6.8 | 5.8 | 5.8 | 4.8 | 5.4 | 3.4 | 5 |
| L. F. Baum - The Wonderful Wizard of Oz | 5.8 | 6.2 | 6.2 | 6 | 6.4 | 5 | 5.6 | 4.4 | 4.6 | 4.8 |
| L. Carroll - Alice's Adventures in Wonderland | 5.6 | 7 | 5.5 | 6.8 | 5.8 | 5.6 | 4 | 4.6 | 4.4 | 5.2 |
| O. Wilde - The Picture of Dorian Gray | 5.4 | 6.8 | 5.4 | 6.2 | 5.8 | 5.2 | 5.6 | 5.6 | 3.6 | 4.8 |
| R. L. Stevenson - Treasure Island | 5.6 | 6.6 | 6.2 | 6.4 | 6 | 4.2 | 4.2 | 4.6 | 3.6 | 4 |
|  | Co-Occurance Semantic | OpenApi Summary GPT3 | OpenApi Keywords GPT3 | OpenApi Summary GPT4 | OpenApi Keywords GPT4 | TextRank | TF-IDF Keywords | TF-IDF Summary | WE spaCy | WordNet |
| AVG | 4.84 | 6.1 | 5.44 | 6.22 | 5.33 | 4.61 | 4.19 | 3.81 | 2.5 | 4.01 |

</br>
</br>
<img src="./average_stable_diffusion_score_book_algorithm_1.svg" width="800px"/>
</br>
<img src="./average_stable_diffusion_score_book_algorithm_2.svg" width="800px"/>
</br>
<img src="./average_stable_diffusion_score_book_algorithm_3.svg" width="800px"/>

<h2>5. Average score for images generated by MidJourney for book by algorithm</h2>

| Book | Co-Occurance Semantic | OpenApi Summary GPT3 | OpenApi Keywords GPT3 | OpenApi Summary GPT4 | OpenApi Keywords GPT4 | TextRank | TF-IDF Keywords | TF-IDF Summary | WE spaCy | WordNet |
|------|-----------------------|----------------------|----------------------|----------------------|----------------------|----------|------------------|----------------|----------|---------|
| A. Dumas and A. Maquet - The Count of Monte Cristo | 4 | 9 | 4 | 8.4 | 4.6 | 4.2 | 5 | 5 | 2.2 | 3.6 |
| A. C. Doyle - The Sign of the Four | 4.2 | 6.6 | 5.6 | 5.6 | 3.6 | 2.4 | 3.2 | 5 | 2.2 | 3.2 |
| B. Stoker - Dracula | 5.6 | 6 | 4.6 | 7.2 | 4.8 | 5.4 | 5 | 3.6 | 2.6 | 3.4 |
| C. Dickens - A Christmas Carol in Prose; Being a Ghost Story of Christmas | 5.8 | 7.6 | 6.6 | 8.6 | 5.4 | 4.8 | 6.4 | 6 | 2.8 | 4.8 |
| D. Defoe - The Life and Adventures of Robinson Crusoe | 5.2 | 6.8 | 6.6 | 6.6 | 6.4 | 3.6 | 4.2 | 3.6 | 2.2 | 3.6 |
| F. S. Fitzgerald - The Great Gatsby | 5.6 | 6.8 | 6 | 6.6 | 7 | 4.2 | 4.8 | 2.2 | 2.4 | 1.4 |
| F. Kafka - Metamorphosis | 3.2 | 5.6 | 3.4 | 6.4 | 3.2 | 4.6 | 4.4 | 5 | 1.8 | 4.2 |
| H. G. Wells - The Time Machine | 5 | 6.4 | 5.4 | 5.8 | 4.4 | 5 | 4.6 | 3.2 | 3.2 | 3.6 |
| H. P. Lovecraft - At the mountains of madness | 5.4 | 7.2 | 6.25 | 7.2 | 6.25 | 4.8 | 4 | 4.4 | 3.4 | 3.8 |
| H. Melville - Moby Dick; Or, The Whale | 5.6 | 7.4 | 6.6 | 7 | 6.8 | 6.4 | 2.8 | 6 | 2 | 5 |
| J. London - The Call of the Wild | 5 | 7.4 | 7.8 | 8.2 | 7.4 | 4.4 | 3.25 | 3.8 | 1.4 | 4.4 |
| J. Grimm and W. Grimm - Grimms' Fairy Tales | 5.8 | 7.6 | 6.8 | 7.4 | 7.6 | 6 | 5 | 4.6 | 1.2 | 5.6 |
| J. F. Cooper - The Last of the Mohicans | 4.6 | 7.4 | 6.6 | 7.6 | 7.2 | 4.6 | 4.8 | 5.4 | 3.25 | 5 |
| J. Austen - Pride and Prejudice | 6.2 | 7.6 | 6.8 | 8 | 6.8 | 6.4 | 5.4 | 6.2 | 3.6 | 3.2 |
| J. Swift - Gullivers Travels | 5.6 | 6 | 5.8 | 6.8 | 5.8 | 5.2 | 5.4 | 4.8 | 3 | 5.8 |
| J. Verne - A Journey to the Centre of the Earth | 6.6 | 8 | 6.8 | 7.4 | 6.8 | 6 | 5.2 | 5.6 | 4 | 5.4 |
| L. F. Baum - The Wonderful Wizard of Oz | 7 | 7 | 6.6 | 7.4 | 6.4 | 5 | 5.8 | 5.6 | 5.4 | 5.2 |
| L. Carroll - Alice's Adventures in Wonderland | 6.4 | 7.4 | 6.2 | 7.6 | 6.6 | 6 | 4.4 | 4.8 | 5.6 | 5.6 |
| O. Wilde - The Picture of Dorian Gray | 5.8 | 7.6 | 5.2 | 8.2 | 5.8 | 5 | 5.8 | 5.6 | 4.6 | 4.2 |
| R. L. Stevenson - Treasure Island | 6 | 7.2 | 7 | 8 | 6 | 5.6 | 5.4 | 4.4 | 4 | 5.8 |
|  | Co-Occurance Semantic | OpenApi Summary GPT3 | OpenApi Keywords GPT3 | OpenApi Summary GPT4 | OpenApi Keywords GPT4 | TextRank | TF-IDF Keywords | TF-IDF Summary | WE spaCy | WordNet |
| AVG | 5.43 | 7.13 | 6.03 | 7.3 | 5.94 | 4.98 | 4.74 | 4.74 | 3.04 | 4.34 |


</br>
</br>
<img src="./average_midjourney_score_book_algorithm_1.svg" width="800px"/>
</br>
<img src="./average_midjourney_score_book_algorithm_2.svg" width="800px"/>
</br>
<img src="./average_midjourney_score_book_algorithm_3.svg" width="800px"/>

<h2>6. Average score for images generated by Dall-e, Stable Diffusion and MidJourney for book</h2>

| Book | Dall-e | StableDiffusion | MidJourney |
|------|--------|-----------------|------------|
| A. Dumas and A. Maquet - The Count of Monte Cristo | 5.32 | 4.35 | 5 |
| A. C. Doyle - The Sign of the Four | 4.3 | 2.92 | 4.16 |
| B. Stoker - Dracula | 4.78 | 4.06 | 4.82 |
| C. Dickens - A Christmas Carol in Prose; Being a Ghost Story of Christmas | 6.06 | 4.82 | 5.88 |
| D. Defoe - The Life and Adventures of Robinson Crusoe | 4.86 | 3.955 | 4.88 |
| F. Scott Fitzgerald - The Great Gatsby | 4.44 | 4.085 | 4.7 |
| Franz Kafka - Metamorphosis | 4.22 | 3.405 | 4.18 |
| H. G. Wells - The Time Machine | 4.62 | 4.51 | 4.66 |
| H. P. Lovecraft - At the mountains of madness | 5.475 | 4.175 | 5.27 |
| H. Melville - Moby Dick; Or, The Whale | 5.955 | 4.858333333 | 5.56 |
| J. London - The Call of the Wild | 5.36 | 5.145 | 5.305 |
| J. Grimm and W. Grimm - Grimms' Fairy Tales | 5.66 | 5.3 | 5.76 |
| J. F. Cooper - The Last of the Mohicans | 5.38 | 4.925 | 5.645 |
| J. Austen - Pride and Prejudice | 5.82 | 5.72 | 6.02 |
| J. Swift - Gullivers Travels | 5.345 | 4.9 | 5.42 |
| J. Verne - A Journey to the Centre of the Earth | 6.16 | 5.42 | 6.18 |
| L. Frank Baum - The Wonderful Wizard of Oz | 6.66 | 5.5 | 6.14 |
| L. Carroll - Alice's Adventures in Wonderland | 6.44 | 5.45 | 6.06 |
| O. Wilde - The Picture of Dorian Gray | 5.86 | 5.44 | 5.78 |
| R. L. Stevenson - Treasure Island | 6.22 | 5.14 | 5.94 |
|  | Dall-e | StableDiffusion | MidJourney |
| AVG | 5.45 | 4.7 | 5.37 |

</br>
</br>
<img src="./average_score_algorithm_per_diffusion_model_1.svg" width="800px"/>
</br>
<img src="./average_score_algorithm_per_diffusion_model_2.svg" width="800px"/>

<h2>7. Number of errors per algorithm</h2>

| Algorithm | TS | IS-D | IS-SD | IS-MJ |
|-----------|----|------|-------|-------|
| Co-Occurance Semantic | 0 | 0 | 2 | 0 |
| OpenApi Summary GPT3 | 0 | 1 | 1 | 0 |
| OpenApi Summary GPT4 | 0 | 2 | 0 | 0 |
| OpenApi Keywords GPT3 | 0 | 0 | 2 | 1 |
| OpenApi Keywords GPT4 | 0 | 1 | 0 | 1 |
| TextRank | 0 | 0 | 4 | 0 |
| TF-IDF Keywords | 0 | 0 | 1 | 2 |
| TF-IDF Summary | 0 | 1 | 2 | 0 |
| WE spaCy | 0 | 1 | 1 | 2 |
| WordNet | 0 | 0 | 2 | 0 |
| SUM | 0 | 6 | 15 | 6 |

</br>
</br>
<img src="./errors_score_1.svg" width="800px"/>
</br>
<img src="./errors_score_2.svg" width="800px"/>