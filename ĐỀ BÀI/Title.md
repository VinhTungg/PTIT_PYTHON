# ĐỀ BÀI: LẬP TRÌNH VỚI PYTHON

## TỪ ĐIỂN

### ICPC0058 - ĐỈNH THẮT

Cho đồ thị **có hướng** liên thông G có N đỉnh và M cạnh. Với một cặp đỉnh (u,v), đỉnh thắt của cặp đỉnh này được định nghĩa là một đỉnh mà tất cả đường đi từ u tới v đều đi qua nó.

Hãy đếm số đỉnh thắt với cặp đỉnh (u,v).

**Input**

Dòng đầu ghi số bộ test, không quá 100.

Mỗi bộ test bắt đầu với một dòng ghi 4 số N, M, u, v (0&lt; N &lt;= 100; 1 &lt; M &lt;=1000; 1 &lt;= u,v &lt;= N).

Tiếp theo là M dòng ghi các cạnh của đồ thị

**Output**

Với mỗi bộ test, ghi ra số đỉnh thắt của cặp đỉnh (u,v)

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  5 7 1 3  1 2  2 4  2 5  3 1  3 2  4 3  5 4  4 5 1 4  1 2  1 3  2 3  2 4  3 4 | 2  0 |

### PY02064 - BIỂU THỨC TOÁN HỌC

Cho dãy số a\[\] gồm có N phần tử. Nhiệm vụ của bạn là xác định nhóm chỉ số ![](./img/PY02064_0.png) sao cho biểu thức dưới đây đạt giá trị lớn nhất.

![](./img/PY02064_1.png)

**Dữ liệu vào:**

- Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
- Mỗi test bắt đầu bởi hai số nguyên N và K. (0 ≤ 5K ≤ N ≤ 1000).
- Dòng tiếp theo mô tả dãy số ![](./img/PY02064_2.png).
 
**Kết quả:**

- Với mỗi test, in ra giá trị lớn nhất của biểu thức S.
 
**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 2  5 1  1 2 3 4 5  6 1  1 2 3 -3 -2 -1 | 15  13 |

### PY03004 - THỐNG KÊ TỪ KHÁC NHAU

Cho một đoạn văn bản có N dòng trong đó có thể có các dấu câu như dẩy phẩy (,) dấu chấm (.) dấu chấm hỏi (?) dấu chấm cảm (!) dấu hai chấm (:) dấu chấm phẩy (;) dấu ngoặc đơn, dấu gạch ngang (-), dấu gạch chéo (/).

Hãy liệt kê các từ khác nhau xuất hiện trong đoạn văn bản theo thứ tự số lần xuất hiện giảm dần.

Chú ý:

- Khi thống kê thì không phân biệt chữ hoa, chữ thường.
- Bỏ qua các dấu câu đã liệt kê ở trên khi tách từ
 
**Input**

Dòng đầu ghi số N không quá 1000.

Tiếp theo là N dòng mô tả văn bản. Mỗi dòng không quá 500 ký tự.

**Output**

Ghi ra danh sách các từ (ở dạng in thường) theo thứ tự số lần xuất hiện giảm dần.

Trong trường hợp số lần xuất hiện bằng nhau thì liệt kê theo thứ tự từ điển tăng dần.

**Ví dụ**

 | **Input** |
|---|
| 3  PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!  Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT  voi muc ho tro 500000 dong/sinh vien PTIT. |
| **Output** |
| ptit 4  2021 2  dong 2  ho 2  nam 2  sinh 2  tro 2  va 2  vien 2  2019 1  2020 1  2022 1  500000 1  6 1  benh 1  dich 1  dinh 1  duy 1  hien 1  hoc 1  hon 1  khi 1  khong 1  muc 1  on 1  phi 1  tang 1  tri 1  trich 1  trong 1  ty 1  voi 1  xuat 1 |

### PY03005 - THỐNG KÊ TỪ KHÁC NHAU THEO NGƯỠNG K

Cho một đoạn văn bản có N dòng trong đó có thể có các dấu câu như dẩy phẩy (,) dấu chấm (.) dấu chấm hỏi (?) dấu chấm cảm (!) dấu hai chấm (:) dấu chấm phẩy (;) dấu ngoặc đơn, dấu gạch ngang (-), dấu gạch chéo (/).

Nhập thêm số nguyên dương K (1 &lt; K &lt; 50). Hãy liệt kê các từ khác nhau xuất hiện ít nhất K lần trong đoạn văn bản. Danh sách được sắp xếp theo thứ tự số lần xuất hiện giảm dần, nếu số lần xuất hiện bằng nhau thì sắp xếp theo thứ tự từ điển tăng dần.

Chú ý:

- Khi thống kê thì không phân biệt chữ hoa, chữ thường.
- Bỏ qua các dấu câu đã liệt kê ở trên khi tách từ
 
**Input**

Dòng đầu ghi số N không quá 1000 và số K (1 &lt; K &lt; 50).

Tiếp theo là N dòng mô tả văn bản. Mỗi dòng không quá 500 ký tự.

**Output**

Ghi ra danh sách các từ (ở dạng in thường) xuất hiện ít nhất K lần trong dữ liệu vào. Danh sách được sắp xếp theo thứ tự số lần xuất hiện giảm dần. Trong trường hợp số lần xuất hiện bằng nhau thì liệt kê theo thứ tự từ điển tăng dần.

**Ví dụ**

 | **Input** |
|---|
| 3 2  PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!  Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT  voi muc ho tro 500000 dong/sinh vien PTIT. |
| **Output** |
| ptit 4  2021 2  dong 2  ho 2  nam 2  sinh 2  tro 2  va 2  vien 2 |

### PY03007 - XỬ LÝ VĂN BẢN

Cho dữ liệu vào là luồng văn bản bất kỳ, gồm các ký tự viết hoa, viết thường, các ký tự số và các dấu câu, không có các ký tự đặc biệt khác. Người ta muốn tách văn bản thành các câu. Mỗi câu in trên một dòng.

Một câu được định nghĩa là dãy ký tự có *ít nhất 1 ký tự chữ cái hoặc chữ số*, không chứa các dấu ngắt câu gồm: dấu chấm (.), dấu chấm hỏi (?) và dấu chấm cảm (!). Dấu phẩy (,) và dấu hai chấm (:) không được coi là dấu ngắt câu.

Nhiệm vụ của bạn là in ra mỗi câu trên một dòng, ký tự đầu câu viết hoa, các ký tự khác viết thường, các từ cách nhau đúng một khoảng trống. Không có khoảng trống ở đầu và cuối câu, và không in ra các dấu ngắt câu.

**Dữ liệu vào**

Gồm một luồng văn bản không quá 100 dòng, mỗi dòng không quá 200 ký tự.

**Kết quả**

In ra các câu, mỗi câu trên một dòng theo quy tắc đã cho.

**Ví dụ**

 | **Input** |
|---|
| ky thi LAP TRINH ICPC PTIT bat dau to chuc tu nam 2010. nhu vay, nam nay la tron 10 nam!   vay CO PHAI NAM NAY LA KY THI LAN THU 10? khong phai! nam nay la KY THI LAN THU 11. |
| **Output** |
| Ky thi lap trinh icpc ptit bat dau to chuc tu nam 2010  Nhu vay, nam nay la tron 10 nam  Vay co phai nam nay la ky thi lan thu 10  Khong phai  Nam nay la ky thi lan thu 11 |

### PY03008 - ĐỒ THỊ HÌNH SAO

Một đơn đồ thị vô hướng được gọi là Hình Sao nếu có một đỉnh có thể nối đến tất cả các đỉnh còn lại, còn các đỉnh khác thì không có cạnh nối với nhau.

Cho mô tả một đơn đồ thị vô hướng N đỉnh với đúng N-1 cạnh. Hãy kiểm tra xem đồ thị đó có phải dạng Hình Sao hay không.

**Dữ liệu vào**

- Dòng đầu tiên ghi số N là số đỉnh của đồ thị (1 ≤ N ≤ 105).
- N-1 dòng tiếp theo, mỗi dòng ghi ra một cặp (u,v) là cạnh của đồ thị. Dữ liệu đảm bảo u ≠ v.
 
**Kết quả**

- Ghi ra trên một dòng chữ **“Yes”** nếu đồ thị là Hình Sao; chữ **“No”** trong trường hợp ngược lại.
 
**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 5    1 2    1 3    1 4    1 5 | Yes |

### PY03012 - BẢNG XẾP HẠNG

Trên cổng thực hành trực tuyến của Học viện Công nghệ Bưu chính Viễn thông có danh sách sinh viên trong lớp được xếp hạng để đánh giá kết quả. Mỗi sinh viên có họ tên, số bài làm đúng, tổng số lượt submit. Hãy sắp xếp danh sách sinh viên để có bảng xếp hạng môn học

Thứ tự sắp xếp như sau:

- Sinh viên có số bài làm đúng nhiều hơn xếp trước, nếu có cùng số bài làm đúng thì ưu tiên sinh viên có số lượt submit ít hơn.
- Sinh viên có cùng hạng, xếp họ tên ưu tiên theo thứ tự từ điển lên trước.
 
**Input**

Dòng đầu tiên đưa vào sĩ số lớp N.

Những dòng kế tiếp đưa vào N sinh viên. Mỗi sinh viên gồm 2 dòng dữ liệu, dòng thứ nhất là họ tên của sinh viên (S) *đã được chuẩn hóa*, dòng thứ hai gồm hai số nguyên liên tiếp C là số bài làm đúng, T là số lượt submit.

N, S thỏa mãn ràng buộc: 1≤ N ≤100; 1≤ Length(S)≤100

C, T thỏa mãn ràng buộc C&lt;500, T &lt; 109

**Output**

Đưa ra bảng xếp hạng danh sách sinh viên đã sắp xếp

Ví dụ

 | Input: | Output: |
|---|---|
| 2    Nguyen Van Nam    168 600    Tran Thi Ngoc    168 600 | Nguyen Van Nam 168 600    Tran Thi Ngoc 168 600 |

### PY03014 - BIỂU THỨC

Cho một biểu thức đúng, tức là các dấu ngoặc đơn đều đầy đủ mở và đóng, đảm bảo đúng thứ tự. Hãy viết chương trình đánh số các cặp dấu ngoặc theo thứ tự xuất hiện, tính từ 1.

Ví dụ với biểu thức (a + (b \*c) ) + (d/e)

ta có thứ tự của các cặp ‘(‘, ‘)’ là 1 2 2 1 3 3

**Input**:

- Dòng đầu tiên đưa vào số lượng bộ test T (không quá 100).
- Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là một biểu thức số học được đưa vào trên một dòng, độ dài không quá 106.
 
**Output**:

- Đưa ra kết quả mỗi test theo từng dòng.
 
 **Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 2  (a + (b \*c) ) + (d/e)  ( ( () ) ( () ) ) | 1 2 2 1 3 3  1 2 3 3 2 4 5 5 4 1 |

### PY03016 - ĐẾM CẶP SỬ DỤNG STACK

Cho dãy số nguyên A\[\]. Với mỗi giá trị A\[i\], các bạn đã biết ngăn xếp có thể được sử dụng để tìm phần tử đầu tiên bên phải hoặc đầu tiên bên trái lớn hơn giá trị A\[i\].

Bài toán đặt ra như sau: hãy đếm xem có bao nhiêu cặp (i,j) với i&lt;j thỏa mãn từ vị trí i đến vị trí j không có số nào lớn hơn A\[i\] hoặc A\[j\]. Tất nhiên các cặp (i,i+1) luôn thỏa mãn.

**Input**

Dòng đầu ghi số N là số phần tử của A\[\] (1 &lt; N &lt; 500.000).

Tiếp theo là N dòng, mỗi dòng ghi 1 số nguyên dương là các phần tử của dãy A, các số đều không quá 9 chữ số.

**Output**

Ghi ra số cặp (i,j) đếm được.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 7  2  4  1  2  2  5  1 | 10 |

***Giải thích test ví dụ:*** *Các cặp thỏa mãn (với chỉ số tính từ 1) là: (1,2); (2,3); (2,4); (2,5); (2,6); (3,4); (4,5); (4,6); (5,6); (6,7).*

### PY03018 - SỐ BƯỚC DI CHUYỂN ÍT NHẤT

Cho ma trận A kích thước N\*M.

Hãy tìm **số bước đi ít nhất** để di chuyển từ vị trí A\[1\]\[1\] đến vị trí A\[N\]\[M\].

Biết rằng mỗi bước từ vị trí (i, j) ta có thể di chuyển theo một trong ba hướng:

- Hướng xuống dưới với số ô di chuyển là hiệu hai giá trị A\[i\]\[j\] và A\[i+1\]\[j\]
- Hướng sang phải với số ô di chuyển là hiệu hai giá trị A\[i\]\[j\] và A\[i\]\[j+1\]
- Hướng chéo xuống với số ô di chuyển là hiệu của hai giá trị A\[i\]\[j\] và A\[i+1\]\[j+1\]
 
**Input:**

- Dòng đầu tiên đưa vào số lượng test T.
- Dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm hai phần: phần thứ nhất là hai số N, M; phần thứ hai là các phần tử của ma trận A\[\]\[\]; các số được viết cách nhau một vài khoảng trống.
- T, N, M, A\[i\]\[j\] thỏa mãn ràng buộc: 1≤T≤100; 1≤ N, M, A\[i\]\[j\]≤103.
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
- Nếu không tìm được đường đi ghi ra -1
 
**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 1  3 3  2 1 2  1 2 4  1 3 2 | 3 |

### PY0314 - XẾP NHÓM

Có N quốc gia, mỗi quốc gia có dân số xác định. Hãy xác định có thể xếp được tối đa bao nhiêu nhóm có đúng k thành viên mà các thành viên từ các nước khác nhau.

**Input:**

Gồm nhiều test (không quá 20), mỗi test có định dạng như sau:

Dòng đầu tiên chứa số nguyên N và k(1 ≤ k ≤ N ≤ 105):

Dòng tiếp theo chứa N số nguyên không âm là dân số từng nước, các giá trị này không vượt quá 1012

**Ouput**

Với mỗi test, in ra 1 số nguyên là đáp án của bài toán.

**Ví dụ:**

 | **INPUT** | **OUTPUT** |
|---|---|
| 5  5 4  4 4 4 4 4  6 5  1 2 3 4 5 6  2 2  1000000000000 1000000000000  17 7  96 17 32 138 112 50 7 19 412 23 14 50 47 343 427 22 39  50 10  638074479 717901019 910893151 924124222 991874870 919392444 729973192 607898881 838529741 907090878 632877562 678638852 749258866 949661738 784641190 815740520 689809286 711327114 658017649 636727234 871088534 964608547 867960437 964911023 642411618 868318236 793328473 849540177 960039699 998262224 775720601 634685437 743766982 826321850 846671921 712570181 676890302 814283264 958273130 899003369 909973864 921987721 978601888 633027021 896400011 725078407 662183572 629843174 617774786 695823011 | 5  3  1000000000000  166  3983180234 |

### PYKT058 - ĐỈNH THẮT

Cho đồ thị **có hướng** liên thông G có N đỉnh và M cạnh. Với một cặp đỉnh (u,v), đỉnh thắt của cặp đỉnh này được định nghĩa là một đỉnh mà tất cả đường đi từ u tới v đều đi qua nó.

Hãy đếm số đỉnh thắt với cặp đỉnh (u,v).

**Input**

Dòng đầu ghi số bộ test, không quá 100.

Mỗi bộ test bắt đầu với một dòng ghi 4 số N, M, u, v (0&lt; N &lt;= 100; 1 &lt; M &lt;=1000; 1 &lt;= u,v &lt;= N).

Tiếp theo là M dòng ghi các cạnh của đồ thị

**Output**

Với mỗi bộ test, ghi ra số đỉnh thắt của cặp đỉnh (u,v)

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  5 7 1 3  1 2  2 4  2 5  3 1  3 2  4 3  5 4  4 5 1 4  1 2  1 3  2 3  2 4  3 4 | 2  0 |

### PYKT059 - THÀNH PHẦN LIÊN THÔNG

Cho đồ thị vô hướng G có N đỉnh, M cạnh.

Hãy liệt kê các đỉnh không cùng thành phần liên thông với một đỉnh cho trước.

**Input**

Dòng đầu ghi 3 số N, M và X (0 &lt; N &lt; 300; 1 ≤ M ≤ N\*(N-1)/2), 0 &lt; X &lt; N).

Tiếp theo là M dòng, mỗi dòng ghi một cạnh của đồ thị. Các cạnh được liệt kê với thứ tự bất kỳ.

**Output**

Ghi ra các đỉnh không liên thông với đỉnh X theo thứ tự tăng dần, mỗi dòng ghi một đỉnh. Nếu không có đỉnh nào thì ghi ra số 0.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 6 4 2  1 3  2 3  1 2  4 5 | 4  5  6 |

### PYKT060 - ĐỒ THỊ ĐẦY ĐỦ

Một đồ thị được coi là **đầy đủ** nếu tất cả các cặp đỉnh đều có cạnh nối trực tiếp đến nhau.

Cho đồ thị vô hướng G với N đỉnh và M cạnh.

Giả sử mỗi bước người ta lấy một đỉnh rồi xóa tất cả các cạnh nối với đỉnh đó, sau đó thiết lập cạnh tới tất cả các đỉnh mà trước đó chưa kết nối với nó.

Hãy kiểm tra xem bằng cách này thì có thể đến một bước nào đó đồ thị trở thành **đầy đủ** hay không?

**Input**

Dòng đầu ghi số đỉnh N (không quá 1000)

Dòng thứ 2 ghi số M là số cạnh (M &lt; N\*(N-1)/2)

Tiếp theo là M dòng, mỗi dòng ghi một cạnh của đồ thị.

**Output**

Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  2  1 2  2 3 | NO |
| 4  2    1 3    2 4 | YES |

### PYKT064 - KHÔNG CÙNG THÀNH PHẦN LIÊN THÔNG

Cho đồ thị vô hướng G có N đỉnh, M cạnh.

Hãy liệt kê các đỉnh không cùng thành phần liên thông với một đỉnh cho trước.

**Input**

Dòng đầu ghi 3 số N, M và X (0 &lt; N &lt; 300; 1 ≤ M ≤ N\*(N-1)/2), 0 &lt; X &lt; N).

Tiếp theo là M dòng, mỗi dòng ghi một cạnh của đồ thị. Các cạnh được liệt kê với thứ tự bất kỳ.

**Output**

Ghi ra các đỉnh không liên thông với đỉnh X theo thứ tự tăng dần, mỗi dòng ghi một đỉnh. Nếu không có đỉnh nào thì ghi ra số 0.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 6 4 2  1 3  2 3  1 2  4 5 | 4  5  6 |

### PYKT068 - DANH SÁCH MÔN THI

Học viện Hoàng gia tổ chức thi thời kỳ giãn cách theo các hình thức thi linh hoạt, phù hợp với từng môn học.

Thông tin về mỗi môn học gồm:

- Mã môn: xâu ký tự không có khoảng trống, không quá 15 ký tự
- Tên môn: xâu ký tự không có thể có khoảng trống, không quá 100 ký tự
- Hình thức thi: xâu ký tự không có thể có khoảng trống, không quá 100 ký tự
 
Hãy nhập danh sách và in danh sách sắp xếp theo mã môn.

**Input**

Dòng đầu ghi số môn học. Mỗi môn ghi trên 3 dòng lần lượt là mã môn, tên môn, hình thức thi.

**Output**

Ghi ra danh sách đã sắp xếp theo mã môn, thứ tự từ điển.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  MUL1320  Nhap mon da phuong tien  Bai tap lon + Van dap truc tuyen  BAS1203  Giai tich 1  Thi viet + Van dap truc tuyen | BAS1203 Giai tich 1 Thi viet + Van dap truc tuyen  MUL1320 Nhap mon da phuong tien Bai tap lon + Van dap truc tuyen |

### PYKT098 - LOẠI BỎ SỐ NGUYÊN

Cho file dữ liệu dạng văn bản DATA.in có thể chứa cả số và ký tự.

Hãy loại bỏ các số nguyên int, sắp xếp các nội dung còn lại trong file theo thứ tự từ điển và in ra trên một dòng.

Chú ý: file dữ liệu có rất nhiều dòng với rất nhiều số và ký tự xen kẽ nhau.

**Input**

File văn bản DATA.in có không quá 1000 dòng. Dữ liệu đảm bảo số lượng các từ trong dãy kết quả nhỏ hơn 10000.

**Output**

Ghi ra các nội dung không thỏa mãn kiểu int trên một dòng, sắp xếp theo thứ tự từ điển, mỗi từ cách nhau một khoảng trống.

**Ví dụ**

 | **DATA.in** | **Output** |
|---|---|
| 12 3 4 5 6 7  Aaa 1 1 Bbb XXX yyy 5 5  999999999999999999999999  9 | 999999999999999999999999 Aaa Bbb XXX yyy |

### PYKT13006 - TÌM CHỮ SỐ

Hãy tìm 3 chữ số đầu tiên trước dấu phẩy của số (3+sqrt(5))^n.

Ví dụ:

Với n = 5, (3+sqrt(5))^5 = 3935.73982… Đáp số là 935.

Với n = 2, (3+sqrt(5))^2 = 27.4164079… Đáp số là 027.

**Input:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 100).

Mỗi test gồm một số nguyên n (n ≤ 2 000 000 000).

**Output:**

Với mỗi test in ra STT và đáp án tìm được. In ra đủ 3 chữ số như test ví dụ (n = 2, in ra 027).

**Ví dụ:**

 | Input | Output |
|---|---|
| 2  5  2 | Case #1: 935  Case #2: 027 |

### PYKT13011 - QUÂN MÃ

Cho bàn cờ có kích thước M x N. Hãy đếm xem có bao nhiêu cách đặt các con mã lên bàn cờ mà không có xung đột nào xảy ra (tính cả trường hợp không đặt quân nào lên bàn cờ).

**Input:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 20).

Mỗi test gồm 2 số nguyên M và N (1 ≤ M ≤ 4, 1 ≤ N ≤ 109).

**Output:**

Với mỗi test, in ra đáp án tìm được theo modulo 109+7.

**Ví dụ :**

 | **Input** | **Output** |
|---|---|
| 4  1 2  2 2  2 3  4 10 | 4  16  36  18702843 |

Giải thích test 1: Với x là vị trí quân mã, ta có:

oo, ox, xo, xx

Giải thích test 2:

Đặt K = 0 quân mã à 1 cách

Đăt K = 1 quân mã à 4 cách

Đăt K = 2 quân mã à 6 cách

Đặt K = 3 quân mã à 4 cách

Đặt K = 4 quân mã à 1 cách

### PYKT14003 - HEXAGRAM

Hexagram được định nghĩa là một ngôi sao 6 cánh đặc biệt. Mỗi giao điểm trong ngôi sao ghi một số nguyên dương sao cho tổng các số trong mỗi cạnh đều bằng nhau.

Ví dụ với dãy số: 3 17 15 18 11 22 12 23 21 7 9 13

Thì ta sẽ có 4 cách sắp xếp các số trên vào ngôi sao là:

![](./img/PYKT14003_0.png)

Bài toán đặt ra là cho trước dãy 12 số nguyên. Hãy đếm số cách xếp các số đó vào ngôi sao sáu cạnh để được dạng Hexagram như mô tả trên.

Chú ý: Không xét các trường hợp là xoay của nhau hoặc lấy đối xứng.

**Input**

Dòng đầu ghi số bộ test.

Mỗi bộ test ghi trên một dòng 12 số nguyên dương, mỗi số cách nhau một khoảng trống. Các số đều được đảm bảo nhỏ hơn 1000000.

**Output**

Với mỗi bộ test, in ra màn hình số cách xếp các số trên để tạo thành HEXAGRAM như mô tả trên.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 2  3 17 15 18 11 22 12 23 21 7 9 13  1 2 3 4 5 6 7 8 9 10 11 13 | 4  0 |

### PYKT2047 - THIẾT KẾ ĐẬP THỦY ĐIỆN

Trên thượng lưu sông High River, một con đập lớn đang được xây dựng. Do dòng sông chảy xiết, các kĩ sư thiết kế N bức tường chắn nước tại các vị trí L\[i\], có độ cao tương ứng bằng H\[i\]. Thiết diện mặt cắt của con đập được biểu diễn như hình vẽ. Mỗi bức tường có độ dày bằng 1 đơn vị.

Do tính phức tạp của con đập, một số bức tường vẫn đang được xây dựng tiếp theo ở phía dưới. Do đó, các kĩ sư cần có hệ thống cảnh báo để xác định giới hạn vùng an toàn cho công việc xây dựng ở phía sau.

Giả sử lưu lượng nước đổ về là K đơn vị thể tích. Các bạn giúp các kĩ sư hãy tính toán xem vị trí bức tường cuối cùng sẽ bị nước tràn qua?

![Alt text](./img/PYKT2047_1.jpg)

**Input**

- Dòng đầu tiên là số lượng bộ test T (T &lt;= 20).
- Mỗi test bắt đầu bởi số lượng bức tường N (N &lt;= 10^5).
- Dòng thứ hai gồm N số nguyên L\[\] mô tả vị trí của các bức tường (1 &lt;= L\[i\] &lt;= 10^9, L\[i\] &gt; L\[i-1\]+1).
- Dòng thứ ba gồm N số nguyên H\[\] mô tả chiều cao của các bức tường (1 &lt;= H\[i\] &lt;= 10^5).
- Tiếp theo là số lượng truy vấn Q (Q &lt;= 10^5).
- Q dòng tiếp theo, mỗi dòng gồm một số nguyên K (1 &lt;= K &lt;= 10^15).
 
**Output**

- Với mỗi truy vấn, hãy in ra đáp án trên một dòng. Nếu bức tường thứ nhất không bị vượt qua, in ra 0.
 
**Test ví dụ:**

 | Input | Output |
|---|---|
| 1  4  1 3 5 8  2 5 3 1  3  17  3  13 | 3  1  1 |

Giải thích test:

 | ![Alt text](./img/PYKT2047_2.jpg) | ![Alt text](./img/PYKT2047_3.jpg) | ![Alt text](./img/PYKT2047_4.jpg) |
|---|---|---|

### PYKT2048 - ỨNG DỤNG STACK TRONG PYTHON

Biểu thức ngoặc là xâu chỉ gồm các ký tự ‘(’ hoặc ‘)’. Biểu thức ngoặc đúng và bậc của biểu thức ngoặc được định nghĩa một cách đệ qui như sau:

- Biểu thức rỗng là biểu thức ngoặc đúng và có bậc bằng 0,
- Nếu A là biểu thức ngoặc đúng có bậc bằng k thì (A) cũng là một biểu thức ngoặc đúng có bậc bằng k+1,
- Nếu A và B là hai biểu thức ngoặc đúng và có bậc tương ứng là k\_1 và k\_2 thì AB cũng là một biểu thức ngoặc đúng có bậc bằng max(k\_1,k\_2).
 
Ví dụ, ‘()(())’ là một biểu thức ngoặc đúng có bậc bằng 2 còn ‘(()(()))’ là một biểu thức ngoặc đúng và có bậc bằng 3.

Cho số nguyên K và xâu S là một xâu chỉ gồm các ký tự ‘(‘, ‘)’ và ‘?’, hãy đếm số cách cách thay các ký tự ‘?’ trong xâu S thành ký tự ‘(‘ hoặc ‘)’ để nhận được xâu T là biểu thức ngoặc đúng có bậc bằng K.

**Input**

- Dòng đầu chứa số nguyên dương K.
- Dòng thứ hai chứa xâu S chỉ gồm các ký tự ‘(‘, ‘)’ và ‘?’.
 
**Giới hạn:**

Subtask 1 (50%) độ dài xâu S không vượt quá 20.

Subtask 2 (50%) độ dài xâu S không vượt quá 200.

**Output**

- Hãy in ra đáp án trên một dòng.
 
**Test ví dụ:**

 | Input | Output |
|---|---|
| 2  ????(? | 1 |
| 1  ((???( | 0 |
| 2  ((???()???(? | 4 |

### PYKT2049 - BÌNH THÔNG NHAU

Có N thùng nước được đánh số từ 1 đến N, giữa 2 thùng bất kỳ đều có một ống nối có một van có thể khóa hoặc mở. Ở trạng thái ban đầu tất cả các van đều đóng.

Bạn được cho một số yêu cầu, trong đó mỗi yêu cầu có 2 dạng:

- Dạng X Y 1 có ý nghĩa là bạn cần mở van nối giữa 2 thùng X và Y.
- Dạng X Y 2 có ý nghĩa là bạn cần cho biết với trạng thái các van đang mở / khóa như hiện tại thì 2 thùng X và Y có thuộc cùng một nhóm bình thông nhau hay không?
 
Hai thùng được coi là thuộc cùng một nhóm bình thông nhau nếu nước từ bình nàycó thể chảy đến được bình kia qua một số ống có van đang mở.

**Input:**

Dòng đầu tiên là số lượng truy vấn Q (Q &lt;= 100 000).

Mỗi truy vấn gồm 3 số nguyên X, Y, Z (X, Y &lt;= 100 000).

**Output:**

Với mỗi truy vấn, in ra đáp án tìm được trên một dòng.

**Test ví dụ:**

 | Input: | Output |
|---|---|
| 9  1 2 2  1 2 1  3 7 2  2 3 1  1 3 2  2 4 2  1 4 1  3 4 2  1 7 2 | 0  0  1  0  1  0 |

### PYKT2052 - XỬ LÝ RỜI RẠC HÓA DỮ LIỆU

Cho ma trận A\[\]\[\] kích thước N x M. Nhiệm vụ của bạn là hãy ánh xạ mỗi phần tử A\[i\]\[j\] thành một phần tử B\[i\]\[j\] để thu được ma trận B\[\]\[\] mới thỏa mãn:

1. B có số lượng phần tử riêng biệt ít nhất có thể
2. Với mỗi hàng i (1 &lt;= i &lt;= N),
 
- nếu A\[i\]\[j\] == A\[i\]\[k\] thì B\[i\]\[j\] = B\[i\]\[k\];
- nếu A\[i\]\[j\] &lt; A\[i\]\[k\] thì B\[i\]\[j\] &lt; B\[i\]\[k\].
 
3. Với mỗi cột j (1 &lt;= j &lt;= M)
 
- nếu A\[i\]\[j\] == A\[k\]\[j\] thì B\[i\]\[j\] = B\[k\]\[j\];
- nếu A\[i\]\[j\] &lt; A\[k\]\[j\] thì B\[i\]\[j\] &lt; B\[k\]\[j\].
 
**Input**

- Dòng đầu tiên chứa 2 số nguyên N và M (N x M &lt;= 10^6).
- N dòng tiếp theo, mỗi dòng gồm M số nguyên mô tả ma trận A (0 &lt;= A\[i\]\[j\] &lt;= 10^9)
 
**Output**

- In ra đáp án là số lượng phần tử riêng biệt trong ma trận B tìm được.
 
**Test ví dụ:**

 | Input | Output |
|---|---|
| 2 3  8 11 16  16 21 5 | 3 |
| 2 3  8 11 16  16 21 16 | 4 |

Giải thích test 1:

1 2 3

3 2 1

Giải thích test 2:

1 2 3

3 4 3

### PYKT2053 - PHÂN HOẠCH TẬP HỢP

Cho dãy số A\[\] có N phần tử. Bạn cần đếm số cách phân hoạch A thành 3 tập hợp con, sao cho tổng các phần tử trong mỗi tập hợp con là bằng nhau.

**Input:**

Dòng đầu tiên là số lượng bộ test (T ≤ 10).

Mỗi test bắt đầu bởi số nguyên N (N ≤ 15)

Dòng tiếp theo gồm N số nguyên dương A\[i\] (1 ≤ A\[i\] ≤ 106).

**Output:**

Với mỗi test, in ra đáp án tìm được trên một dòng.

**Ví dụ:**

 | **Input:** | **Output** |
|---|---|
| 2  5  10 20 25 5 30  3  1 2 3 | 6  0 |

  
 Giải thích test 1:

11223

11332

22113

22331

33112

33221

### PYKT2079 - SỐ LỘC PHÁT (BẢN KHÓ)

Theo quan niệm Á Đông, số 6 và 8 đọc là lục, bát, do vậy người ta hay liên tưởng tới lộc phát, là phát tài phát lộc.

Nhiệm vụ của bạn là hãy xác định xem trong các số từ 1 à N và chia hết cho 8, tức dãy số 8, 16, 24, 32, … , tổng số lần xuất hiện chữ số 6 và 8 là bao nhiêu?

**Input:**

Dòng đầu tiên là số lượng bộ test T (T &lt;= 100 000).

Mỗi test gồm một số nguyên dương N (1 &lt;= N &lt;= 10^18)

**Output:**

Với mỗi test, in ra đáp án tìm được trên một dòng.

**Test ví dụ:**

 | Input: | Output |
|---|---|
| 4  10  18  33  56 | 1  2  2  4 |

Giải thích test 4: Có 4 số thỏa mãn là 8, 16, 48, 56, tổng cộng có 4 chữ số thỏa mãn.

## DANH SÁCH

### ICPC0101 - THU GỌN DÃY SỐ

Cho dãy số A\[\] chỉ bao gồm các số nguyên dương. Người ta thu gọn dần dãy số bằng cách loại bỏ các cặp phần tử kề nhau mà có tổng là chẵn. Sau khi cặp phần tử đó bị loại ra thì dãy số được dồn lại. Cứ tiếp tục như vậy cho đến khi không còn cặp phần tử nào kề nhau có tổng chẵn nữa.

Hãy tính xem cuối cùng dãy A\[\] còn bao nhiêu phần tử.

**Input**

Dòng đâu ghi số N là số phần tử của dãy (1 ≤ N ≤ 105 tức là dãy A có thể có đến 10 nghìn phần tử).

Dòng tiếp theo ghi N số của dãy A (1 ≤ A\[i\] ≤ 100).

**Output**

Ghi ra trên một dòng số phần tử còn lại trong dãy A\[\].

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 5  2 3 4 5 6 | 5 |
| **Input** | **Output** |
| 10  1 5 5 8 6 4 3 5 9 3 | 2 |

### ICPC0104 - TÌM SỐ NHỎ NHẤT

Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9. Nhiệm vụ của bạn là tìm số nhỏ nhất xuất hiện trong xâu. Ví dụ với xâu X\[\]=”12ab29cd19” ta có kết quả là 12.

Input:

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là một xâu ký tự thỏa mãn yêu cầu bài toán.
- T, n thỏa mãn ràng buộc : 1≤T≤100; 1≤ n≤105;
- Dữ liệu vào đảm bảo số lớn nhất cũng không quá 18 chữ số
 
Output:

- Đưa ra kết quả mỗi test theo từng dòng.
 
Ví dụ:

 | Input: | Output: |
|---|---|
| 2    12ab29cd19  ab123gh456cd | 12    123 |

### ICPC0105 - TÌM SỐ LỚN NHẤT

Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9. Nhiệm vụ của bạn là tìm số lớn nhất xuất hiện trong xâu. Ví dụ với xâu X\[\]=”12ab29cd19” ta có kết quả là 29.

Input:

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là một xâu ký tự thỏa mãn yêu cầu bài toán.
- T, n thỏa mãn ràng buộc : 1≤T≤100; 1≤ n≤105;
- Dữ liệu vào đảm bảo số lớn nhất cũng không quá 18 chữ số
 
Output:

- Đưa ra kết quả mỗi test theo từng dòng.
 
Ví dụ:

 | Input: | Output: |
|---|---|
| 2    12ab29cd19  ab123gh456cd | 29    456 |

### ICPC0106 - ĐỔI CƠ SỐ - 2

Cho xâu nhị phân X\[\] có độ dài n. Nhiệm vụ của bạn là hãy đổi xâu nhị phân thành một số ở hệ cơ số b, trong đó b chỉ là một trong các số 2, 4, 8, 16. Ví dụ xâu X =”10010100010010101” và b = 8 ta có kết quả là 224225 là số ở hệ cơ số 8.

**Input:**

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào b là cơ số của hệ đếm; dòng tiếp theo đưa vào xâu nhị phân có độ dài n.
- T, n, X\[\] thỏa mãn ràng buộc : 1≤T≤10; 1≤ n≤105; X\[i\] =0, 1;
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 2    8    10010100010010101  2    10010100010010101 | 224225  10010100010010101 |

### ICPC0107 - THAY ĐỔI CHỮ SỐ

Cho hai số nguyên dương X1, X2. Ta chỉ được phép thay đổi chữ số p thành chữ số q và ngược lại chữ. Hãy đưa ra tổng nhỏ nhất và tổng lớn nhất các số X1 và X2 được tạo ra theo nguyên tắc kể trên.

**Input:**

- Dòng đầu tiên đưa vào số lượng bộ test T.
- Những dòng kế tiếp đưa vào T bộ test. Mỗi bộ test gồm 3 dòng: dòng đầu tiên ghi lại chữ số p và chữ số q; hai dòng kế tiếp ghi lại các số X1 và X2 theo thứ tự.
- T, X1, X2 thỏa mãn ràng buộc: 1≤ T ≤100; 0≤ X1, X2 ≤101000.
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
 | **Input:** | **Output:** |
|---|---|
| 1  5 6    645  666 | 1100 1312 |

### ICPC0108 - SUM TRIPLE ZERO

Cho mảng A\[\] gồm N số nguyên khác nhau. Nhiệm vụ của bạn là đếm số lượng các bộ ba phần tử khác nhau có tổng là 0. Ví dụ A\[\] = {0, -1, 2, -3, 1}, ta nhận được kết quả là 2 vì có hai bộ 3: (0, -1, 1) và (2, -3, 1).

**Input:**

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào N là số lượng phần tử của mảng A\[\]; dòng tiếp theo đưa vào các phần tử A\[i\] của mảng A\[\].
- T, N, A\[i\] thỏa mãn ràng buộc : 1≤T≤100; 1≤ N≤103; -109≤ A\[i\] ≤109;
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 2    5    0 -1 2 -3 1     5    1 -2 1 0 5 | 2    1 |

### ICPC0109 - MIN TRIPLE

Cho mảng A\[\] gồm N số nguyên.

Nhiệm vụ của bạn là tìm tổng nhỏ nhất của bộ ba số trong mảng. Ví dụ A\[\] = {1, 2, 3, 4, 5}, ta nhận được tổng nhỏ nhất của bộ ba số là 1 + 2 + 3 = 6. Chú ý nếu sử dụng kỹ thuật sắp xếp, submit lời giải của bạn sẽ bị fail.

**Input:**

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào N là số lượng phần tử của mảng A\[\]; dòng tiếp theo đưa vào các phần tử A\[i\] của mảng A\[\].
- T, N, A\[i\] thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤106; -108≤ A\[i\] ≤108;
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
Ví dụ:

 | **Input:** | **Output:** |
|---|---|
| 2    7    1 2 3 0 -1 8 10     7    9 8 20 3 4 -1 0 | 0    2 |

### ICPC0110 - MAX TRIPLE

Cho mảng A\[\] gồm N số nguyên.

Nhiệm vụ của bạn là tìm tổng lớn nhất của bộ ba số trong mảng. Chú ý nếu sử dụng kỹ thuật sắp xếp, submit lời giải của bạn sẽ bị fail.

Ví dụ A\[\] = {1, 2, 3, 4, 5}, ta nhận được tổng lớn nhất của bộ ba số là 3 + 4 + 5 = 12.

Input:

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào N là số lượng phần tử của mảng A\[\]; dòng tiếp theo đưa vào các phần tử A\[i\] của mảng A\[\].
- T, N, A\[i\] thỏa mãn ràng buộc : 1≤T≤100; 1≤ N≤106; -108≤ A\[i\] ≤108;
 
Output:

- Đưa ra kết quả mỗi test theo từng dòng.
 
Ví dụ:

 | Input: | Output: |
|---|---|
| 2    7    1 2 3 0 -1 8 10     7    9 8 20 3 4 -1 0 | 21    37 |

### ICPC0111 - XOAY MẢNG

Cho mảng A\[\] gồm N số nguyên và số tự nhiên d. Hãy thực hiện quay mảng A\[\] với d phần tử từ phải qua trái. Ví dụ A\[\] = {1, 2, 3, 4, 5}, d = 2 ta nhận được mảng A\[\] = {3, 4, 5, 1, 2}.

**Input:**

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào N là số lượng phần tử của mảng A\[\] và số d; dòng tiếp theo đưa vào các phần tử A\[i\] của mảng A\[\].
- T, N, d, A\[i\] thỏa mãn ràng buộc : 1≤T≤100; 1≤ d≤ N ≤107; 0≤ A\[i\] ≤109;
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 2    5 2    1 2 3 4 5     10 3    2 4 6 8 10 12 14 16 18 20 | 3 4 5 1 2    8 10 12 14 16 18 20 2 4 6 |

### ICPC0112 - PRIME – TRIPLET

Bộ ba số nguyên tố được gọi là Prime- Triplet nếu nó là bộ ba số nguyên tố dưới dạng (p, p +2, p + 6) hoặc (p, p + 4, p+6), trong đó p là một số nguyên tố. Ví dụ các bộ ba số (5, 7, 11) hoặc (7, 11, 13) đều là các Prime-Triplet. Cho số tự nhiên N, nhiệm vụ của bạn là đếm số các Prime-Triplet nhỏ hơn N.

**Input:**

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
- T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤106;
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 2  15  25 | 2  5 |

### ICPC0113 - EMIRP NUMBER

Một số nguyên dương K được gọi là Emirp Number nếu K là số nguyên tố, đảo các chữ số của K cũng là một số nguyên tố nhưng không phải chính nó (không đối xứng). Ví dụ số 11 không phải là số Emirp Number. Cho số tự nhiên N, nhiệm vụ của bạn là hãy liệt kê tất cả các số Emirp Number nhỏ hơn N.

**Input:**

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
- T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤106;
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
- Chú ý: ghi theo các cặp số thỏa mãn từ nhỏ đến lớn, xem ví dụ để hiểu hơn về cách hiển thị kết quả.
 
**Ví dụ:**

 | Input: | Output: |
|---|---|
| 2  40  100 | 13 31  13 31 17 71 37 73 79 97 |

### ICPC0114 - PERFECT PRIME

Một số nguyên dương N được gọi là Perfect Prime nếu N là số nguyên tố; đảo ngược các chữ số của N cũng là một số nguyên tố; tổng các chữ số của N là một số nguyên tố và mỗi chữ số của N cũng là một số nguyên tố. Cho số nguyên dương N, hãy kiểm tra N có phải là Perfect Prime hay không? Đưa ra “Yes” nếu N là Perfect Prime, ngược lại đưa ra “No”.

**Input:**

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
- T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤107;
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 3  13  753  757 | No  No  Yes |

### ICPC0115 - SỐ KRISH

Một số nguyên dương N được gọi là số Krish nếu tổng giai thừa các chữ số của N bằng chính nó. Ví dụ N = 145 = 1! + 4! + 5! = 145 là một số Krish. Cho số nguyên dương N, hãy kiểm tra N có phải là một số Krish hay không? Đưa ra “Yes” nếu N là một số Krish, ngược lại đưa ra “No”.

**Input:**

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
- T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤108;
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
**Ví dụ:**

 | Input: | Output: |
|---|---|
| 2  145  235 | Yes  No |

### ICPC0116 - CON SỐ DUYÊN NỢ

Con số duyên nợ là con số có chữ số đầu và chữ số cuối giống nhau.

Viết chương trình kiểm tra xem một số nguyên dương n ghi trong hệ thập phân có chữ số đầu và chữ số cuối giống nhau không?

**Input**

Gồm nhiều dòng, mỗi dòng chứa một số nguyên dương n ghi ở hệ thập phân.

Giới hạn:

1≤n≤10^100

**Output**

Ứng với mỗi số nguyên dương n, ghi ra trên một dòng là YES nếu số n tương ứng có chữ số đầu và chữ số cuối giống nhau, NO nếu ngược lại.

**Ví dụ**

 | Input: | Output: |
|---|---|
| 2    12345    123451 | NO    YES |

### ICPC0117 - CHÚC MỪNG NĂM MỚI

Tí năm nay đã lên lớp 1 rồi, Tết đến Tí rất vui vì nhận được rất nhiều lời chúc.

Vì mới tập viết nên Tí đã ghi lại tất cả các lời chúc đó. Cũng vì rất trân trọng các lời chúc nên Tí đã ghi tất cả các lời chúc bằng chữ IN HOA, tuy nhiên do mới tập viết nên Tí ghi không có dấu. Giờ ngồi lật lại cuốn nhật ký ghi các lời chúc, Tí thấy mình đã ghi được n lời chúc.

Tí muốn biết có bao nhiêu lời chúc khác nhau (hai lời chúc được gọi là khác nhau nếu chúng có độ dài khác nhau hoặc tồn tại ít nhất một vị trí mà ký tự ở vị trí đó của hai lời chúc là khác nhau, hay nói cách khác, đó là hai xâu ký tự khác nhau). Bạn hãy lập chương trình giúp Tí đếm xem có bao nhiêu lời chúc khác nhau nhé.

**Input:**

Dòng đầu chứa số nguyên dương n là số lời chúc Tí ghi được;

n dòng tiếp theo, mỗi dòng chứa một xâu ký tự S là một lời chúc.

n, S thỏa mãn ràng buộc: 1 ≤ n ≤ 10^4; Các lời chúc S có độ dài không quá 30 ký tự gồm các chữ cái la tinh IN HOA ‘A’…’Z’ và dấu cách.

**Output:**

Một số nguyên dương duy nhất là số lời chúc khác nhau.

**Ví dụ:**

 | Input: | Output: |
|---|---|
| 4  CHUC MUNG NAM MOI  HAPPY NEW YEAR  CHUC MUNG TUOI MOI  CHUC MUNG NAM MOI | 3 |

### ICPC0118 - CUNG HOÀNG ĐẠO

Trong chiêm tinh học phương Tây, các cung Hoàng Đạo là mười hai cung 30° của Hoàng Đạo, bắt đầu từ điểm phân Vernal (một trong những giao điểm của Hoàng Đạo với Xích đạo thiên cầu), còn được gọi là Điểm Đầu của Bạch Dương. Thứ tự của các cung Hoàng Đạo là Bạch Dương, Kim Ngưu, Song Tử, Cự Giải, Sư Tử, Xử Nữ, Thiên Bình, Thiên Yết, Nhân Mã, Ma Kết, Bảo Bình và Song Ngư. Mỗi khu vực được đặt tên theo chòm sao mà nó đi qua trong lúc đặt tên. Cung hoàng đạo của một người được xác định dựa trên ngày sinh bằng bảng dưới đây:

 | **Cung** | **Tên cung** | **Thời gian** |  |
|---|---|---|---|
|  |
| [![](./img/ICPC0118_0.png)](https://vi.wikipedia.org/wiki/File:Aries.svg) | Bach Duong | 21 tháng 3 - 19 tháng 4 |  |
| [![](./img/ICPC0118_1.png)](https://vi.wikipedia.org/wiki/File:Taurus.svg) | Kim Nguu | 20 tháng 4 - 20 tháng 5 |  |
| [![](./img/ICPC0118_2.png)](https://vi.wikipedia.org/wiki/File:Gemini.svg) | Song Tu | 21 tháng 5 - 20 tháng 6 |  |
| [![](./img/ICPC0118_3.png)](https://vi.wikipedia.org/wiki/File:Cancer.svg) | Cu Giai | 21 tháng 6 - 22 tháng 7 |  |
| [![](./img/ICPC0118_4.png)](https://vi.wikipedia.org/wiki/File:Leo.svg) | Su Tu | 23 tháng 7 - 22 tháng 8 |  |
| [![](./img/ICPC0118_5.png)](https://vi.wikipedia.org/wiki/File:Virgo.svg) | Xu Nu | 23 tháng 8 - 22 tháng 9 |  |
| [![](./img/ICPC0118_6.png)](https://vi.wikipedia.org/wiki/File:Libra.svg) | Thien Binh | 23 tháng 9 - 22 tháng 10 |  |
| [![](./img/ICPC0118_7.png)](https://vi.wikipedia.org/wiki/File:Scorpio.svg) | Thien Yet | 23 tháng 10 - 22 tháng 11 |  |
| [![](./img/ICPC0118_8.png)](https://vi.wikipedia.org/wiki/File:Sagittarius.svg) | Nhan Ma | 23 tháng 11 - 21 tháng 12 |  |
| [![](./img/ICPC0118_9.png)](https://vi.wikipedia.org/wiki/File:Capricorn.svg) | Ma Ket | 22 tháng 12 - 19 tháng 1 |  |
| [![](./img/ICPC0118_10.png)](https://vi.wikipedia.org/wiki/File:Aquarius.svg) | Bao Binh | 20 tháng 1 - 18 tháng 2 |  |
| [![](./img/ICPC0118_11.png)](https://vi.wikipedia.org/wiki/File:Pisces.svg) | Song Ngu | 19 tháng 2 - 20 tháng 3 |  |

Ví dụ: nếu sinh nhật của một người là vào ngày 5 tháng 5, thì họ là Kim Ngưu, vì nó nằm trong khoảng từ ngày 21 tháng 4 đến ngày 20 tháng 5.

Nhiệm vụ của bạn là xác định cung hoàng đạo của một ngày sinh bất kỳ.

**Input:**

Dòng đầu tiên đưa vào số lượng bộ test T.

Những dòng kế tiếp đưa vào T bộ test. Mỗi bộ test gồm 2 số cách nhau bởi một khoảng trống d và m, trong đó d là ngày, m là tháng.

**Output:**

Đưa ra cung hoàng đạo dựa vào bảng đã cho tương ứng với ngày tháng nhập vào.

 | **Input** | **Output** |
|---|---|
| 2  5 5  30 7 | Kim Nguu  Su Tu |

### PY02002 - LIỆT SỐ FIBONACCI

Dãy số Fibonacci được định nghĩa theo công thức như sau:

- F1 = 1
- F2 = 1
- Fn = Fn-1 + Fn-2 với n&gt;2
 
Cho hai số nguyên dương a và b (1 &lt; a &lt; b &lt; 93). Viết chương trình liệt kê các số Fibonacci từ a đến b.

**Input**

Dòng đầu ghi số bộ test, không quá 10.

Mỗi bộ test viết trên một dòng hai số a và b.

**Output**

Ghi ra kết quả của mỗi test trên một dòng, mỗi số cách nhau một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 1  1 10 | 1 1 2 3 5 8 13 21 34 55 |

### PY02003 - DÃY SỐ HAMMING

Dãy số nguyên dương tăng dần trong đó ước số nguyên tố lớn nhất của các số trong dãy đều không vượt quá 5 được gọi là dãy số Hamming. Ví dụ 10 = 2x5 thuộc dãy Hamming còn 26 = 2x13 không thuộc dãy Hamming.

Số 1 được coi là số đầu tiên của dãy Hamming.

Cho số nguyên dương N. Hãy xác định xem N có thuộc dãy Hamming hay không và nếu có thì thứ tự của N trong dãy Hamming là bao nhiêu.

**Input:**

Dòng đầu tiên ghi số bộ test (không quá 105).

Mỗi test ghi một số N (1 ≤ N ≤ 1018).

**Output:**

Nếu giá trị N thuộc dãy Hamming thì ghi ra thứ tự của N (tính từ 1).

Nếu không thì ghi ra “Not in sequence”

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 11  1  2  6  7  8  9  10  11  12  13  14 | 1  2  6  Not in sequence  7  8  9  Not in sequence  10  Not in sequence  Not in sequence |

### PY02004 - DÃY SỐ NHỊ PHÂN

Cho dãy số A\[\] chỉ có các giá trị nhị phân 0 và 1.

Hãy đếm xem có bao nhiêu cặp số khác nhau đứng cạnh nhau trong dãy.

**Input**

Dòng 1 ghi số N là số phần tử của dãy (không quá 100).

Dòng 2 ghi N số nhị phân.

**Output**

Ghi ra kết quả bài toán.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 6  1 0 0 1 1 1 | 2 |

### PY02005 - CẶP NGHỊCH THẾ

Cho dãy số A\[\] gồm có N phần tử.

Một cặp nghịch thế là một cặp số (u, v) sao cho u &lt; v và A\[u\] &gt; A\[v\]. Nhiệm vụ của bạn là hãy đếm số lượng cặp nghịch thế trong dãy số A\[\] ban đầu.

**Input:**

Dòng đầu tiên là N (N ≤ 1000), số lượng phần tử trong dãy số ban đầu.

Dòng tiếp theo gồm N số nguyên A\[i\] (1 ≤ A\[i\] ≤ 109).

**Output:**

In ra một số nguyên là số lượng dãy nghịch thế tìm được.

**Ví dụ:**

 | Input: | Output |
|---|---|
| 5  2 4 1 3 5 | 3 |

**Giải thích test:**

Có 3 cặp nghịch thế là (2, 1), (4,1) và (4, 3).

### PY02006 - DÃY SỐ PHÙ HỢP

Cho hai dãy số A\[\] và B\[\] có cùng N phần tử. Dãy số A\[\] được gọi là phù hợp với dãy số B\[\] khi và chỉ khi tồn tại một phép sắp đặt lại các phần tử trong A\[\] và B\[\] sao cho phần tử thứ i của A\[\] nhỏ hơn hoặc bằng phần tử thứ i của mảng B\[\] (với tất cả vị trí trong dãy).

Hãy xác định hai dãy số A\[\] và B\[\] có phù hợp với nhau hay không?

**Input**:

Dòng đầu tiên đưa vào số lượng bộ test T (T≤100).

Những dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm 3 phần: phần thứ nhất là số N; phần thứ hai là N số của A\[\]; phần thứ 3 là N số của B\[\].

(1≤N≤100, 0≤A\[i\], B\[i\]≤1000)

**Output:**

Đưa ra kết quả mỗi test theo từng dòng. Kết quả “YES” nếu A\[\] phù hợp với B\[\], ngược lại đưa ra “NO”.

**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 2  4  7 5 3 2  5 4 8 7  8  7 5 3 2 5 105 45 10  2 4 0 5 6 9 75 84 | YES  NO |

### PY02007 - CHIA DƯ CHO 42

Cho dãy số A có 10 phần tử là các số nguyên dương. Hãy đếm xem sẽ có bao nhiêu số khác nhau trong dãy nếu tất cả các phần tử đều được chia dư cho 42.

**Input**

Gồm 10 số nguyên dương, viết trên một hoặc nhiều dòng.

**Output**

Ghi ra các số khác nhau tìm được sau khi đã chia dư cho 42.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 | 10 |
| 42 84 252 420 840  126 42 84 420 126 | 1 |
| 39 40 41 42 43 44 82  83 84 85 | 6 |

### PY02008 - KHOẢNG CÁCH NGUYÊN TỐ

Cho hai số nguyên N và X.

Bắt đầu từ số X, hãy liệt kê N +1 số liên tiếp sao cho khoảng cách giữa số trước và số sau lần lượt là các số trong dãy N số nguyên tố đầu tiên.

Ví dụ N=5 và X=4. Vì 5 số nguyên tố đầu tiên là 2 3 5 7 11 nên ta có 6 số trong dãy cần liệt kê là: 4 6 9 14 21 32

**Input**

Chỉ có 1 dòng ghi 2 số N và X. (2 ≤ N ≤ 1000; 1 ≤ X ≤ 100)

**Output**

Ghi ra trên một dòng lần lượt N+1 số của dãy kết quả.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 5 4 | 4 6 9 14 21 32 |

### PY02009 - TRÚNG THƯỞNG

Chung kết Euro 2020, quá nhiều người dự đoán đúng Italia thắng Anh bằng đá luân lưu 11m. Ban tổ chức chương trình *Dự đoán tỉ số trúng Mercedes* thấy rất khó trao giải nên quyết định tìm người được trao thưởng bằng cách chạy đoạn code lựa chọn ngẫu nhiên.

Các người chơi dự đoán đúng được đánh số thứ tự bắt đầu từ 1, giả sử cũng có không quá 1000 người. Chương trình sẽ thực hiện lấy ngẫu nhiên N lần, mỗi lần 1 giá trị từ 1 đến 1000, N cũng không quá 1000.

Sau khi kết thúc N lần ngẫu nhiên, con số nào được chọn nhiều lần nhất sẽ cho biết người trúng thưởng. Trong trường hợp có nhiều số có số lần xuất hiện bằng nhau và lớn nhất thì số có giá trị nhỏ nhất sẽ được chọn.

Hãy giúp BTC tìm ra người được trao thưởng.

**Input**

Dòng đầu ghi số bộ test, không quá 100.

Mỗi bộ test gồm N+1 dòng. Dòng đầu ghi số N. Tiếp theo là N dòng ghi các giá trị ngẫu nhiên nhận được.

**Output**

Với mỗi test, ghi ra số thứ tự của người được trao thưởng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  3  999  999  19  4  13  333  333  13  3  11  12  13 | 999  13  11 |

### PY02010 - LỚN NHẤT VÀ NHỎ NHẤT

Cho dãy số có N số nguyên dương. Các số trong dãy có thể tới 100 chữ số.

Hãy tìm số nhỏ nhất và số lớn nhất trong dãy. Nếu cả dãy bằng nhau thì in ra BANG NHAU.

**Input**

Có nhiều bộ test. Mỗi bộ test bắt đầu với số N (không quá 20). Tiếp theo là N dòng, mỗi dòng ghi một số trong dãy, giá trị đều nguyên dương nhưng có thể có chữ số 0 ở đâu, và có thể tới 100 chữ số.

Input kết thúc khi N = 0.

**Output**

Với mỗi test, ghi ra trên một dòng số nhỏ nhất và lớn nhất. Nếu tất cả dãy bằng nhau thì ghi ra BANG NHAU.

**Ví dụ**

 | Input | Output |
|---|---|
| 5  1  2  3  4  5  3  001  22  33333333333333333333333333333333333  3  1  1  1  0 | 1 5  1 33333333333333333333333333333333333  BANG NHAU |

### PY02011 - BIẾN ĐỔI VỀ DÃY BẰNG NHAU

Cho dãy số A\[\] có N phần tử là các số nguyên dương.

Mỗi bước bạn được phép thay đổi 1 giá trị trong dãy bằng cách tăng lên 1 hoặc giảm đi 1.

Hãy tính xem cần ít nhất bao nhiêu bước để biến đổi dãy về giá trị bằng nhau, với điều kiện giá trị của dãy bằng nhau đó phải là một trong các giá trị ban đầu của dãy.

**Input**

Dòng đầu ghi số N là số phần tử của dãy (không quá 200).

Dòng thứ 2 ghi N phần tử của dãy, các phần tử đều nguyên dương và không quá 10000.

**Output**

Ghi ra tổng số bước ít nhất tìm được và giá trị bằng nhau được chọn.

Trong trường hợp có nhiều giá trị có thể chọn thì chọn số đầu tiên theo thứ tự xuất hiện trong dãy ban đầu.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 8  13 5 8 7 9 15 26 34 | 59 13 |

### PY02012 - SẮP XẾP CHẴN LẺ

Cho dãy số A\[\] có n phần tử. Hãy sắp xếp các số chẵn trong dãy theo thứ tự tăng dần và các số lẻ theo thứ tự giảm dần.

In ra dãy kết quả đã sắp xếp trong đó vị trí số chẵn và vị trí số lẻ không thay đổi so với dãy ban đầu.

**Input**

Dòng đầu ghi số n (1 &lt; n ≤ 1000)

Các dòng tiếp theo ghi đủ n số của dãy A\[\], các số đều nguyên dương và không quá 1000.

**Output**

Ghi ra dãy kết quả đã sắp xếp trong đó các vị trí của số chẵn và số lẻ không thay đổi.

**Ví dụ**

 | **Input** | **Ouput** |
|---|---|
| 10  1 2 3 4 5 6 7 7 9 6 | 9 2 7 4 7 6 5 3 1 6 |

### PY02013 - BIẾN ĐỔI VỀ 1

Cho số nguyên dương N. Mỗi bước thực hiện các phép biến đổi N theo quy tắc sau

- Nếu N chẵn thì N = N/2
- Nếu N lẻ thì N = N\*3 + 1
 
Hãy đếm xem có bao nhiêu giá trị xuất hiện cho đến khi N = 1. Tất nhiên nếu ban đầu N = 1 thì chỉ có một giá trị duy nhất.

Ví dụ: N = 3 thì sẽ có 8 giá trị xuất hiện lần lượt là: 3, 10, 5, 16, 8, 4, 2, 1

**Input**

Có nhiều test, mỗi test ghi trên một dòng số nguyên dương N không quá 100.

Input kết thúc khi N = 0.

**Output**

Với mỗi test, ghi ra kết quả tính được trên một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 1  2  3  0 | 1  2  8 |

### PY02014 - BIẾN ĐỔI NGUYÊN TỐ

Cho dãy số A\[\] có N số nguyên dương. Người ta muốn biến đổi tất cả các số trong dãy về số nguyên tố. Tại mỗi bước, mỗi số chưa nguyên tố được phép tăng hoặc giảm 1 đơn vị để biến đổi dần về số nguyên tố gần nhất.

Hãy tính xem cần ít nhất bao nhiêu bước cần thực hiện để biến đổi tất cả các phần tử của dãy về nguyên tố.

**Input**

Dòng đầu ghi số N là số phần tử của dãy (không quá 200).

Dòng thứ 2 ghi N số của dãy, các giá trị đều nguyên dương và không quá 10000.

**Output**

Ghi ra số bước ít nhất tính được.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 8  13 5 8 7 9 15 26 34 | 3 |

### PY02015 - BIẾN ĐỔI DÃY SỐ

Cho một dãy số A\[\] có 4 số nguyên dương, đánh số vị trí từ 1 đến 4. Tại mỗi bước, giá trị A\[i\] được thay thế bằng abs(A\[i\] – A\[i+1\]), riêng A\[4\] = abs(A\[4\]-A\[1\]).

*Hàm abs (trị tuyệt đối) được sử dụng để đảm bảo các giá trị của dãy số luôn dương.*

Hãy đếm xem sau bao nhiêu bước thì dãy số A\[\] có cả 4 vị trí đều bằng nhau.

**Input**

Có 4 số của dãy A\[\], các giá trị không quá 9 chữ số. Input kết thúc với 4 số 0.

**Output**

Với mỗi test, ghi ra số bước cần thực hiện.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 1 3 5 9  4 3 2 1  0 0 0 0 | 6  4 |

### PY02016 - XUẤT HIỆN NHIỀU LẦN NHẤT

Cho dãy số A\[\] gồm có N phần tử. Nhiệm vụ của bạn là hãy tìm một số có tần số xuất hiện nhiều nhất, yêu cầu lớn hơn N/2 lần xuất hiện trong dãy số.

**Input:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 10).

Mỗi test gồm số nguyên N (1≤ N ≤ 100 000), số lượng phần tử trong dãy số ban đầu.

Dòng tiếp theo gồm N số nguyên A\[i\] (1 ≤ A\[i\] ≤ 1 000 000).

**Output:**

Với mỗi test in ra đáp án của bài toán trên một dòng. Nếu có nhiều số cùng có tần số xuất hiện nhiều nhất như nhau và đều thỏa mãn số lần lớn hơn N/2 thì in ra số nhỏ nhất.

Nếu không tìm được đáp án, in ra “NO”.

**Ví dụ:**

 | Input: | Output |
|---|---|
| 2  9  3 3 4 2 4 4 2 4 4  8  3 3 4 2 4 4 2 4 | 4  NO |

### PY02017 - TÂN SUẤT LẺ

Cho dãy số A\[\] gồm có N phần tử. Các phần tử trong dãy số đều xuất hiện với tần suất chẵn, chỉ có duy nhất 1 số có số lần xuất hiện là số lẻ. Nhiệm vụ của bạn là hãy tìm số này.

**Input:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 10).

Mỗi test gồm số nguyên N (1≤ N ≤ 100 000), số lượng phần tử trong dãy số ban đầu. N là một số lẻ.

Dòng tiếp theo gồm N số nguyên A\[i\] (1 ≤ A\[i\] ≤ 1 000 000).

**Output:**

Với mỗi test in ra trên mỗi dòng một số nguyên là đáp án của bài toán.

**Ví dụ:**

 | Input: | Output |
|---|---|
| 2  7  1 2 3 2 3 1 3  5  1 1 3 3 2 | 3  2 |

### PY02018 - SỐ NHỎ NHẤT CÒN THIẾU

Cho dãy số A\[\] có N phần tử là các số nguyên dương khác nhau. Hãy tìm số nhỏ nhất còn thiếu trong dãy số đó.

**Input**

Dòng đầu ghi số N (1 &lt;= N &lt;= 30000).

Dòng tiếp theo ghi N số của dãy A (1 &lt;= A\[i\] &lt;= 30000).

**Output**

Ghi ra số nhỏ nhất còn thiếu nếu có.

(khi dãy số đầy đủ các số từ 1 đến N thì số nhỏ nhất còn thiếu sẽ là N+1).

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  1 2 4 | 3 |

### PY02019 - NGUYÊN TỐ CÙNG NHAU

Cho dãy số A\[\] có n phần tử là các số nguyên dương khác nhau, giá trị không quá 100. Hãy liệt kê các cặp số nguyên tố cùng nhau xuất hiện trong dãy theo thứ tự tăng dần, mỗi cặp số in trên một dòng.

Một cặp số được gọi là nguyên tố cùng nhau nếu ước chung lớn nhất của chúng bằng 1.

**Input**

Dòng đầu ghi số n (không quá 100).

Dòng thứ 2 ghi n số của dãy A\[\]

**Output**

Ghi lần lượt các cặp số nguyên tố cùng nhau theo thứ tự tăng dần.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 5  3 7 9 6 13 | 3 7    3 13    6 7    6 13    7 9    7 13    9 13 |

### PY02020 - TÍNH ĐIỂM TRUNG BÌNH

Sau khi xem Olympic Tokyo 2020, Nam nhận thấy ở một số nội dung thi có chấm điểm thì điểm được tính cho vận động viên sẽ bỏ qua các giá trị điểm thấp nhất và cao nhất sau đó mới tính trung bình.

Nam mở rộng bài toán như sau: Có N giám khảo, mỗi giám khảo cho một giá trị điểm là một số thực trong đoạn từ 0 đến 10. Hãy loại bỏ các giá trị điểm bằng với điểm thấp nhất hoặc cao nhất, sau đó in ra điểm trung bình của các giá trị còn lại.

Dữ liệu vào của bài toán đảm bảo luôn có ít nhất 3 giá trị khác nhau trong các giá trị điểm ban đầu.

**Input**

Dòng đầu ghi số N là số giám khảo (không quá 100).

Dòng thứ 2 ghi N giá trị điểm, là các số thực trong đoạn \[0,10\] - đảm bảo luôn có ít nhất 3 giá trị khác nhau.

**Output**

Ghi ra giá trị điểm trung bình sau khi đã loại bỏ các giá trị nhỏ nhất và lớn nhất. Kết quả được ghi với đúng 2 số phần thập phân.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 6  6.75 8 9.2 7.25 7.75 6.75 | 7.67 |

### PY02021 - DÃY CON CHUNG CỦA BA DÃY SỐ

Cho dãy số A\[\], B\[\] và C\[\] là dãy không giảm và có lần lượt N, M, K phần tử. Nhiệm vụ của bạn là hãy tìm các phần tử chung của 3 dãy số này.

**Input:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 20).

Mỗi test gồm số nguyên N, M và K (1≤ N, M, K ≤ 100 000).

Dòng tiếp theo gồm N số nguyên A\[i\], rồi M số nguyên B\[i\] và K số nguyên C\[i\].

(0 ≤ A\[i\], B\[i\], C\[i\] ≤ 109).

**Output:**

Với mỗi test, in ra trên một dòng là đáp án thu được. Nếu không tìm được đáp án, in ra “NO”.

**Ví dụ:**

 | Input: | Output |
|---|---|
| 3  6 5 8  1 5 10 20 40 80  5 7 20 80 100  3 4 15 20 30 70 80 120  3 5 4  1 5 5  3 4 5 5 10  5 5 10 20  3 3 3  1 2 3  4 5 6  7 8 9 | 20 80  5 5  NO |

### PY02022 - LIỆT KÊ SỐ NGUYÊN TỐ TRONG DÃY

Cho dãy số nguyên dương A\[\] có N phần tử. Hãy viết chương trình liệt kê các số nguyên tố khác nhau và số lần xuất hiện của số đó trong dãy ban đầu.

Các số được liệt kê theo thứ tự xuất hiện.

**Input**

Dòng đầu ghi số N (không quá 500).

Dòng sau ghi N số của dãy (không quá 6 chữ số).

**Output**

Ghi ra các số nguyên tố khác nhau trong dãy theo thứ tự xuất hiện và số lần xuất hiện. Mỗi số liệt kê trên 1 dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 10  2 4 7 5 7 8 9 3 7 2 | 2 2  7 3  5 1  3 1 |

### PY02023 - SẮP XẾP THEO TỔNG CHỮ SỐ

Cho dãy số A\[\] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.

Hãy sắp xếp dãy số theo tổng chữ số tăng dần. Nếu tổng chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.

**Input**

Dòng đầu ghi số bộ test (không quá 10)

Mỗi bộ test gồm 2 dòng:

- Dòng đầu là số N (N &lt; 100)
- Dòng thứ 2 ghi N số của mảng A\[\], các số đều nguyên dương và không quá 9 chữ số.
 
**Output**

Với mỗi bộ test, ghi trên một dòng dãy số kết quả.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 1  8  143 43 22 99 7 9 1111 10000000 | 10000000 22 1111 7 43 143 9 99 |

### PY02024 - SẮP XẾP THEO TÍCH CHỮ SỐ

Cho dãy số A\[\] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.

Hãy sắp xếp dãy số theo tích các chữ số tăng dần. Nếu tích các chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.

**Input**

Dòng đầu ghi số bộ test (không quá 10)

Mỗi bộ test gồm 2 dòng:

- Dòng đầu là số N (N &lt; 100)
- Dòng thứ 2 ghi N số của mảng A\[\], các số đều nguyên dương và không quá 9 chữ số.
 
**Output**

Với mỗi bộ test, ghi trên một dòng dãy số kết quả.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 1  8  143 43 22 99 7 9 1111 10000000 | 10000000 1111 22 7 9 43 143 99 |

### PY02025 - TẬP HỢP SỐ NGUYÊN

Cho dãy số a\[\] có n phần tử và dãy số b\[\] có m phần tử là các số nguyên dương nhỏ hơn 1000. Gọi tập hợp A là tập các số khác nhau trong a\[\], tập hợp B là tập các số khác nhau trong b\[\].

Hãy tìm tập giao của A và B, hiệu A – B và hiệu B – A. Mỗi tập kết quả viết trên một dòng theo thứ tự từ nhỏ đến lớn.

**Input**

Dòng đầu ghi 2 số n và m (1 &lt; n,m &lt;100).

Dòng thứ 2 ghi n số của a\[\].

Dòng thứ 3 ghi m số của b\[\].

Các số đều dương và nhỏ hơn 1000.

**Output**

Dòng đầu ghi tập giao của A và B

Dòng thứ 2 ghi tập A – B

Dòng thứ 3 ghi tập B - A

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 5 6  1 2 3 4 5  3 4 5 6 7 8 | 3 4 5  1 2  6 7 8 |

### PY02026 - TẬP HỢP SỐ BẰNG NHAU

Cho dãy số a\[\] có n phần tử và dãy số b\[\] có m phần tử là các số nguyên dương nhỏ hơn 1000. Gọi tập hợp A là tập các số khác nhau trong a\[\], tập hợp B là tập các số khác nhau trong b\[\].

Tập A và tập B được coi là bằng nhau nếu số phần tử bằng nhau và tất cả các giá trị số từ nhỏ đến lớn đều bằng nhau từng đôi một. Khi A = B ta cũng có thể kết luận là hai dãy a\[\] và b\[\] chứa các số giống nhau.

Hãy kiểm tra xem A có bằng B hay không?

**Input**

Dòng đầu ghi 2 số n và m (1 &lt; n,m &lt;100).

Dòng thứ 2 ghi n số của a\[\].

Dòng thứ 3 ghi m số của b\[\].

Các số đều dương và nhỏ hơn 1000.

**Output**

Ghi ra kết quả kiểm tra

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 12 18  1 2 3 4 5 1 2 3 5 4 1 2  1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5 | YES |

### PY02027 - TÁCH SỐ VÀ SẮP XẾP

Cho N xâu ký tự bao gồm cả chữ số và chữ cái. Các chữ số liên tiếp sẽ tạo ra một số nguyên. Hãy sắp xếp các số tách được theo thứ tự tăng dần.

Chú ý: các chữ số 0 ở đầu nếu có sẽ không được tính. Ví dụ: các chữ số tách ra được là 00234 thì được tính như số 234, nếu là 00000000 thì được tính như số 0.

**Input**

Dòng đầu ghi số N (không quá 100).

N dòng tiếp theo, mỗi dòng ghi một xâu ký tự, độ dài không quá 100.

Dữ liệu đảm bảo sẽ tách ra được không quá 500 số.

**Output**

Ghi ra các số theo thứ tự sắp xếp tăng dần, mỗi số trên một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  A129h  G07bxjq3  aaaaaaa4aaaa | 3  4  7  129 |

### PY02028 - SẮP XẾP NGUYÊN TỐ

Cho dãy số nguyên dương A\[\] có N phần tử. Các giá trị trong dãy không quá 1000.

Hãy sắp xếp các số nguyên tố trong dãy theo thứ tự tăng dần. Các giá trị không nguyên tố vẫn giữ nguyên vị trí như lúc đầu.

Xem ví dụ để hiểu rõ hơn yêu cầu bài toán.

**Input**

Dòng đầu ghi số N (1 &lt; N &lt; 100), dòng thứ 2 ghi N số của dãy A\[\].

**Output**

Ghi ra dãy số kết quả trên một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 8  4 6 3 8 7 2 5 9 | 4 6 2 8 3 5 7 9 |

### PY02029 - BẦU CỬ

Khu dân cư ABC tiến hành bầu tổ trưởng dân phố. Có M ứng viên và N cử tri. Người dân trong khu dân cư đã chán ngấy với việc các ứng viên vận động tranh cử, câu kéo phiếu bầu trong các nhiệm kỳ trước nên họ quyết định đặt ra quy định mới như sau:

- Các ứng viên được đánh số từ 1 tới M. Mỗi cử tri sẽ viết ra đúng 1 số thứ tự ứng viên mình muốn chọn và bỏ vào hòm phiếu.
- Người trúng cử là người có số phiếu bầu **nhiều thứ hai**
- Nếu không có người đứng thứ hai thì kết quả bầu cử sẽ bị hủy bỏ
- Nếu có nhiều hơn 1 người cùng có số phiếu nhiều thứ hai thì người nào có số thứ tự nhỏ nhất sẽ được chọn.
 
Viết chương trình xác định người trúng cử.

**Input**

Dòng đầu ghi hai số N và M (1 &lt; M &lt; 10, 5 &lt; N &lt; 500).

Dòng thứ 2 ghi N giá trị trong các phiếu bầu. Các giá trị đảm bảo hợp lệ (tức là từ 1 đến M).

**Output**

Ghi ra số thứ tự của người trúng cử.

Hoặc nếu không có ai trúng cử thì ghi ra NONE

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 10 4  2 3 1 2 3 4 1 2 3 2 | 3 |
| 8 4  1 2 3 4 4 3 2 1 | NONE |

### PY02030 - PHÂN CHIA NGUYÊN TỐ

Cho dãy số A\[\] có N phần tử là các số nguyên dương không quá 1000. Sau khi loại bỏ tất cả các giá trị bị lặp lại ở trong A\[\] ta tạo được dãy B\[\] có m phần tử là các giá trị khác nhau theo đúng thứ tự xuất hiện trong dãy A\[\].

Hãy tìm vị trí i nhỏ nhất (tính từ 0) trong dãy B\[\] thỏa mãn:

- Tổng các phần tử từ B\[0\] đến B\[i\] là một số nguyên tố
- Tổng các phần tử từ B\[i+1\] đến B\[m-1\] cũng là một số nguyên tố.
 
**Input**

Dòng đầu ghi số N (1 &lt; N &lt; 500).

Dòng tiếp theo ghi N số của dãy A\[\]

**Output**

Ghi ra vị trí i đầu tiên tìm được.

Nếu không có vị trí thỏa mãn thì ghi ra dòng chữ NOT FOUND

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 10  3 6 7 3 4 7 3 6 4 4 | 0 |
| 10  3 6 7 3 5 7 3 6 6 7 | NOT FOUND |

*Giải thích test 1:*

*Dãy B\[\] = {3, 6, 7, 4}*

*Vị trí 0 thỏa mãn vì 3 là số nguyên tố; 6+7+4 = 17 cũng là số nguyên tố.*

### PY02032 - LIỆT KÊ CÁC SỐ CÓ HAI CHỮ SỐ TĂNG DẦN

Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.

Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A\[\] chỉ bao gồm các số có hai chữ số.

Hãy liệt kê **các số khác nhau xuất hiện trong A\[\]** theo **thứ tự tăng dần**.

**Input**

Chỉ có một dòng ghi dãy ký tự số (độ dài không quá 1000). Dữ liệu vào đảm bảo không có chữ số 0.

**Output**

Ghi ra lần lượt các số khác nhau xuất hiện trong dãy A\[\] theo thứ tự tăng dần, mỗi số viết cách nhau một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 124356141111434356149 | 11 12 14 43 56 |

### PY02033 - LIỆT KÊ CÁC SỐ CÓ HAI CHỮ SỐ THEO THỨ TỰ XUẤT HIỆN

Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.

Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A\[\] chỉ bao gồm các số có hai chữ số.

Hãy liệt kê **các số khác nhau xuất hiện trong A\[\]** theo **thứ tự xuất hiện**.

**Input**

Chỉ có một dòng ghi dãy ký tự số (độ dài không quá 1000). Dữ liệu vào đảm bảo không có chữ số 0.

**Output**

Ghi ra lần lượt các số khác nhau xuất hiện trong dãy A\[\] theo thứ tự xuất hiện, mỗi số viết cách nhau một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 124356141111434356149 | 12 43 56 14 11 |

### PY02034 - ĐẾM CÁC SỐ CÓ HAI CHỮ SỐ

Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.

Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A\[\] chỉ bao gồm các số có hai chữ số.

Hãy liệt kê và đếm **các số khác nhau xuất hiện trong A\[\]** theo **thứ tự xuất hiện**.

**Input**

Chỉ có một dòng ghi dãy ký tự số (độ dài không quá 1000). Dữ liệu vào đảm bảo không có chữ số 0.

**Output**

Ghi ra lần lượt các số khác nhau xuất hiện trong dãy A\[\] và số lần xuất hiện tương ứng, mỗi số viết trên một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 124356141111434356149 | 12 1  43 3  56 2  14 2  11 2 |

### PY02035 - NGƯỠNG TỐI THIỂU

Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.

Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A\[\] chỉ bao gồm các số có hai chữ số.

Nhập thêm số nguyên dương K gọi là giá trị ngưỡng tối thiểu. Hãy liệt kê các số xuất hiện từ K lần trở lên trong dãy A\[\] theo thứ tự từ nhỏ đến lớn.

**Input**

Dòng đầu ghi dãy ký tự số (độ dài không quá 1000). Dữ liệu vào đảm bảo không có chữ số 0.

Dòng thứ 2 ghi số nguyên dương K (không quá 100).

**Output**

Ghi ra lần lượt các số khác nhau của dãy A\[\] thỏa mãn xuất hiện ít nhất K lần và số lần xuất hiện tương ứng, mỗi số viết trên một dòng theo thứ tự tăng dần.

Nếu không có số nào thỏa mãn ghi ra dòng chữ NOT FOUND

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 124356141111434356149  2 | 11 2  14 2  43 3  56 2 |
| 124356141111434356149  10 | NOT FOUND |

### PY02036 - LIỆT KÊ CẶP SỐ NGUYÊN TỐ CÙNG NHAU

Cho dãy số A\[\] có n phần tử là các số nguyên dương khác nhau, giá trị không quá 100. Hãy liệt kê các cặp số nguyên tố cùng nhau xuất hiện trong dãy theo thứ tự tăng dần, mỗi cặp số in trên một dòng.

Một cặp số được gọi là nguyên tố cùng nhau nếu ước chung lớn nhất của chúng bằng 1.

**Input**

Dòng đầu ghi số n (không quá 100).

Dòng thứ 2 ghi n số của dãy A\[\]

**Output**

Ghi lần lượt các cặp số nguyên tố cùng nhau theo thứ tự tăng dần.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 5  3 7 9 6 13 | 3 7    3 13    6 7    6 13    7 9    7 13    9 13 |

### PY02039 - MA TRẬN - 1

Cho ma trận vuông cấp N\*N chỉ bao gồm các số nguyên dương.

Với đường chéo chính, ta sẽ chia ma trận thành 2 nửa, được gọi là nửa trên và nửa dưới của đường chéo chính (không tính các phần tử nằm trên đường chéo chính).

![](./img/PY02039_0.jpg)

Độ chênh lệch của ma trận được tính bằng trị tuyệt đối khi lấy **tổng giá trị các phần tử ở nửa trên** trừ đi **tổng giá trị các phần tử ở nửa dưới**.

Nhập thêm một giá trị K gọi là *ngưỡng cân đối của ma trận*. Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối, nếu lớn hơn K thì không cân đối.

Hãy xác định độ chênh lệch và tính cân đối của ma trận.

**Input**

Dòng đầu ghi số N (2 &lt; N &lt; 50)

N dòng tiếp theo ghi các giá trị của ma trận, các số đều nguyên dương và không quá 1000.

Dòng cuối ghi số K (0 &lt; K &lt;100)

**Output**

Dòng đầu ghi chữ YES hoặc NO

Dòng thứ 2 ghi ra giá trị độ chênh lệch của ma trận

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 5  2 8 10 6 7  6 3 2 6 9  10 2 6 2 8  9 9 7 9 8  9 6 5 6 9  5 | YES  3 |

### PY02040 - MA TRẬN - 2

Cho ma trận vuông cấp N\*N chỉ bao gồm các số nguyên dương.

Với đường chéo phụ, ta sẽ chia ma trận thành 2 nửa, được gọi là nửa trên và nửa dưới của đường chéo phụ (không tính các phần tử nằm trên đường chéo phụ).

![](./img/PY02040_0.jpg)

Độ chênh lệch của ma trận được tính bằng trị tuyệt đối khi lấy **tổng giá trị các phần tử ở nửa trên** trừ đi **tổng giá trị các phần tử ở nửa dưới**.

Nhập thêm một giá trị K gọi là *ngưỡng cân đối của ma trận*. Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối, nếu lớn hơn K thì không cân đối.

Hãy xác định độ chênh lệch và tính cân đối của ma trận.

**Input**

Dòng đầu ghi số N (2 &lt; N &lt; 50)

N dòng tiếp theo ghi các giá trị của ma trận, các số đều nguyên dương và không quá 1000.

Dòng cuối ghi số K (0 &lt; K &lt;100)

**Output**

Dòng đầu ghi chữ YES hoặc NO

Dòng thứ 2 ghi ra giá trị độ chênh lệch của ma trận

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 5  2 8 10 6 7  6 3 2 6 9  10 2 6 2 8  9 9 7 9 8  9 6 5 6 9  5 | NO  11 |

### PY02041 - TỔNG SỐ NGUYÊN LỚN

Cho hai xâu ký tự A và B mô tả hai số nguyên dương lớn có thể có đến 1000 chữ số.

Có thể có các chữ số 0 ở đầu của A và B.  
 Hãy tính tổng A + B.

Kết quả ghi ra cần loại bỏ các chữ số 0 ở đầu nếu có.

**Input**

Có hai dòng ghi 2 số A và B.

**Output**

Ghi ra kết quả A + B.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 121212121212121212  45678978 | 121212121257800190 |

### PY02042 - HIỆU SỐ NGUYÊN LỚN

Cho hai xâu ký tự A và B mô tả hai số nguyên dương lớn có thể có đến 1000 chữ số.

Có thể có các chữ số 0 ở đầu của A và B.  
 Hãy tính A - B.

Kết quả có thể âm, khi ghi ra cần loại bỏ các chữ số 0 ở đầu nếu có.

Tất nhiên nếu kết quả là -0 thì ghi ra là 0.

**Input**

Có hai dòng ghi 2 số A và B.

**Output**

Ghi ra kết quả A - B.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 000123456789012345678901234567890  00000000000000001234567890 | 123456789012345678900000000000 |

### PY02043 - ĐẾM SỐ TRONG XÂU

Cho một ký tự S\[\] chỉ có các chữ số, độ dài không quá 1000, và số nguyên dương N (không quá 9 chữ số). Hãy đếm xem số N xuất hiện bao nhiêu lần trong S\[\].

Chú ý: các ký tự số không được đếm lặp. Tức là mỗi ký tự chỉ được xét một lần.

Ví dụ: S\[\] = “**121**2**121**112211221**121**”, N = **121** thì đáp án là 3.

**Input**

Dòng đầu ghi số bộ test, không quá 20.

Mỗi test gồm hai dòng, dòng đầu là xâu ký tự S\[\], dòng sau là số N.

**Output**

Với mỗi bộ test, ghi ra kết quả tính được trên một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  1212121112211221121  121  2222222222322292  2222 | 3  2 |

### PY02045 - TÁCH ĐÔI VÀ TÍNH TỔNG

Cho một số nguyên dương không quá 200 chữ số. Mỗi bước tách số nguyên thành hai nửa: **nửa đầu** là n/2 chữ số đầu tiên, **nửa sau** là phần còn lại (trong đó n là số chữ số của số ban đầu, nếu n lẻ thì phép chia 2 sẽ tính phần nguyên). Sau đó thực hiện tính tổng của hai nửa này.

Lặp lại các bước trên cho đến khi kết quả chỉ còn là số có 1 chữ số.

Hãy thực hiện tính toán và in kết quả của từng bước.

**Input**

Chỉ có một số nguyên dương không quá 200 chữ số.

**Output**

Ghi ra kết quả từng bước, mỗi bước trên một dòng. Dừng lại khi kết quả chỉ còn 1 chữ số.

**Ví dụ**

 | **Input** | **Ouput** |
|---|---|
| 123456 | 579  84  12  3 |

### PY02046 - PHÂN CHIA NGUYÊN TỐ

Cho dãy số A\[\] có N phần tử là các số nguyên dương không quá 1000. Sau khi loại bỏ tất cả các giá trị bị lặp lại ở trong A\[\] ta tạo được dãy B\[\] có m phần tử là các giá trị khác nhau theo đúng thứ tự xuất hiện trong dãy A\[\].

Hãy tìm vị trí i nhỏ nhất (tính từ 0) trong dãy B\[\] thỏa mãn:

- Tổng các phần tử từ B\[0\] đến B\[i\] là một số nguyên tố
- Tổng các phần tử từ B\[i+1\] đến B\[m-1\] cũng là một số nguyên tố.
 
**Input**

Dòng đầu ghi số N (1 &lt; N &lt; 500).

Dòng tiếp theo ghi N số của dãy A\[\]

**Output**

Ghi ra vị trí i đầu tiên tìm được.

Nếu không có vị trí thỏa mãn thì ghi ra dòng chữ NOT FOUND

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 10  3 6 7 3 4 7 3 6 4 4 | 0 |
| 10  3 6 7 3 5 7 3 6 6 7 | NOT FOUND |

*Giải thích test 1:*

*Dãy B\[\] = {3, 6, 7, 4}*

*Vị trí 0 thỏa mãn vì 3 là số nguyên tố; 6+7+4 = 17 cũng là số nguyên tố.*

### PY02048 - TÁCH NHÓM TỐI ƯU

Cho dãy số A\[\] có N phần tử là các số nguyên dương. Với mỗi số nguyên K, hãy tính xem có thể tách dãy số A thành ít nhất bao nhiêu nhóm sao cho mỗi số trong nhóm đều có thể tìm được ít nhất một số khác **cùng nhóm** có chênh lệch **không vượt quá K.**

Ví dụ: A\[\] = {2, 6, 1, 7, 3, 4, 9}; K = 1 thì kết quả là 3 ứng với 3 nhóm {2,1,3,4}; {6,7}; {9}

**Input**

Dòng đầu ghi hai số N và K (0 &lt;= K &lt;= 105; 0 &lt;= N &lt;= 106).

Dòng thứ 2 ghi ra N số của dãy A\[\], các số nguyên dương và không quá 106.

**Output**

Ghi ra số nhóm ít nhất có thể.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 7 1  2 6 1 7 3 4 9 | 3 |

### PY02050 - ĐOẠN LIÊN TIẾP NHỎ HƠN

Cho dãy số A\[\] có N phần tử. Với mỗi vị trí thứ i trong dãy, hãy tính độ dài của đoạn liên tiếp tính từ i trở về phía trước mà các giá trị đều nhỏ hơn hoặc bằng A\[i\].

**Input:** Dòng đầu ghi số bộ test (không quá 10). Mỗi test có 2 dòng.

- Dòng đầu tiên gồm 1 số nguyên N (1 ≤ N ≤ 105).
- Dòng tiếp theo gồm N số nguyên A1, A2, …, AN (1 ≤ A\[i\] ≤ 106).
 
**Output**

- Với mỗi bộ test, in ra dãy kết quả trên một dòng.
 
**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 1  7  100 80 60 70 60 75 85 | 1 1 1 2 1 4 6 |

### PY02051 - KHÔI PHỤC DÃY SỐ

Bình có sẵn dãy số A có N phần tử và tạo ra ma trận B kích thước N\*N theo quy tắc:

- B\[i\]\[i\] = 0
- B\[i\]\[j\] = A\[i\] + A\[j\] (với i#j)
 
Bình đưa cho Nam ma trận B và đố Nam khôi phục dãy số A ban đầu.

Hãy giúp Nam nhé.

**Input**

Dòng đầu ghi số N (1 &lt; N &lt;= 1000).

N dòng tiếp theo ghi ma trận B, các số đều nguyên dương và không quá 100.000.

**Output**

Ghi ra dãy số A tìm được trên một dòng, mỗi số cách nhau 1 khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  0 2  2 0 | 1 1 |
| 4  0 3 6 7  3 0 5 6  6 5 0 9  7 6 9 0 | 2 1 4 5 |

### PY02052 - TÍNH CÂN ĐỐI CỦA MA TRẬN - 1

Cho ma trận vuông cấp N\*N chỉ bao gồm các số nguyên dương.

Với đường chéo chính, ta sẽ chia ma trận thành 2 nửa, được gọi là nửa trên và nửa dưới của đường chéo chính (không tính các phần tử nằm trên đường chéo chính).

![](./img/PY02052_0.jpg)

Độ chênh lệch của ma trận được tính bằng trị tuyệt đối khi lấy **tổng giá trị các phần tử ở nửa trên** trừ đi **tổng giá trị các phần tử ở nửa dưới**.

Nhập thêm một giá trị K gọi là *ngưỡng cân đối của ma trận*. Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối, nếu lớn hơn K thì không cân đối.

Hãy xác định độ chênh lệch và tính cân đối của ma trận.

**Input**

Dòng đầu ghi số N (2 &lt; N &lt; 50)

N dòng tiếp theo ghi các giá trị của ma trận, các số đều nguyên dương và không quá 1000.

Dòng cuối ghi số K (0 &lt; K &lt;100)

**Output**

Dòng đầu ghi chữ YES hoặc NO

Dòng thứ 2 ghi ra giá trị độ chênh lệch của ma trận

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 5  2 8 10 6 7  6 3 2 6 9  10 2 6 2 8  9 9 7 9 8  9 6 5 6 9  5 | YES  3 |

### PY02053 - TÍNH CÂN ĐỐI CỦA MA TRẬN - 2

Cho ma trận vuông cấp N\*N chỉ bao gồm các số nguyên dương.

Với đường chéo phụ, ta sẽ chia ma trận thành 2 nửa, được gọi là nửa trên và nửa dưới của đường chéo phụ (không tính các phần tử nằm trên đường chéo phụ).

![](./img/PY02053_0.jpg)

Độ chênh lệch của ma trận được tính bằng trị tuyệt đối khi lấy **tổng giá trị các phần tử ở nửa trên** trừ đi **tổng giá trị các phần tử ở nửa dưới**.

Nhập thêm một giá trị K gọi là *ngưỡng cân đối của ma trận*. Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối, nếu lớn hơn K thì không cân đối.

Hãy xác định độ chênh lệch và tính cân đối của ma trận.

**Input**

Dòng đầu ghi số N (2 &lt; N &lt; 50)

N dòng tiếp theo ghi các giá trị của ma trận, các số đều nguyên dương và không quá 1000.

Dòng cuối ghi số K (0 &lt; K &lt;100)

**Output**

Dòng đầu ghi chữ YES hoặc NO

Dòng thứ 2 ghi ra giá trị độ chênh lệch của ma trận

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 5  2 8 10 6 7  6 3 2 6 9  10 2 6 2 8  9 9 7 9 8  9 6 5 6 9  5 | NO  11 |

### PY02054 - BIẾN ĐỔI VỀ MA TRẬN VUÔNG

Cho ma trận A kích thước N\*M chỉ bao gồm các số nguyên dương.

Trong trường hợp N # M, hãy biến đổi ma trận A về dạng ma trận vuông theo quy tắc sau:

- Nếu N &gt; M, hãy loại bỏ các **hàng có thứ tự lẻ** trong ma trận ban đầu (thứ tự hàng tính từ 1) cho đến khi N = M. Ví dụ N = 6, M = 4 thì cần loại bỏ hàng thứ 1 và hàng thứ 3.
- Nếu M &gt; N, hãy loại bỏ các **cột có thứ tự chẵn** trong ma trận ban đầu (thứ tự cột tính từ 1). Ví dụ: N = 4, M = 6 thì cần loại bỏ cột thứ 2 và cột thứ 4.
 
In ra ma trận kết quả sau khi biến đổi.

**Input**

Dòng đầu ghi hai số N và M (1 &lt; N,M &lt; 50).

N dòng tiếp theo ghi các phần tử của ma trận A, các giá trị đều nguyên dương và không quá 1000.

**Output**

Ghi ra ma trận vuông sau khi biến đổi.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 6 4  2 8 7 6  6 3 2 6  7 2 2 8  9 9 9 8  9 6 6 3  7 7 4 9 | 6 3 2 6  9 9 9 8  9 6 6 3  7 7 4 9 |
| 4 6  2 8 7 6 4 3  6 3 2 6 7 2  7 2 2 8 9 1  9 9 9 8 0 7 | 2 7 4 3  6 2 7 2  7 2 9 1  9 9 0 7 |

### PY02055 - SỐ NGUYÊN TỐ LỚN NHẤT TRONG MA TRẬN

Cho ma trận A cỡ N\*M chỉ bao gồm các số nguyên dương.

Hãy tìm số nguyên tố lớn nhất trong ma trận và các vị trí có giá trị bằng số nguyên tố lớn nhất đó.

**Input**

Dòng đầu ghi hai số N và M (1 &lt; N, M &lt; 50)

Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 1000.

**Output**

Ghi ra giá trị của số nguyên tố lớn nhất. Sau đó lần lượt là các vị trí của số nguyên tố lớn nhất, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.

Nếu không tìm thấy số nguyên tố nào thì ghi ra NOT FOUND

**Ví dụ**

 | **Input** | **.Output** |
|---|---|
| 6 4  23 21 26 10  13 13 22 14  28 29 28 23  29 19 11 19  16 26 24 21  13 25 21 29 | 29  Vi tri \[2\]\[1\]  Vi tri \[3\]\[0\]  Vi tri \[5\]\[3\] |

### PY02056 - SỐ THUẬN NGHỊCH LỚN NHẤT TRONG MA TRẬN

Cho ma trận A cỡ N\*M chỉ bao gồm các số nguyên dương.

Một số được coi là thuận nghịch nếu có từ 2 chữ số trở lên và nếu viết theo thứ tự ngược lại giá trị vẫn không thay đổi so với giá trị ban đầu. Ví dụ: 99, 121, 1331

Hãy tìm số thuận nghịch lớn nhất trong ma trận và các vị trí có giá trị bằng số thuận nghịch lớn nhất đó.

**Input**

Dòng đầu ghi hai số N và M (1 &lt; N, M &lt; 50)

Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 10000.

**Output**

Ghi ra giá trị của số thuận nghịch lớn nhất. Sau đó lần lượt là các vị trí của số thuận nghịch lớn nhất, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.

Nếu không tìm thấy số thuận nghịch nào thì ghi ra NOT FOUND

**Ví dụ**

 | **Input** | **.Output** |
|---|---|
| 6 4  23 21 77 10  13 13 22 14  28 29 28 23  29 77 11 19  16 26 24 21  13 25 77 77 | 77  Vi tri \[0\]\[2\]  Vi tri \[3\]\[1\]  Vi tri \[5\]\[2\]  Vi tri \[5\]\[3\] |

### PY02057 - SỐ MAY MẮN TRONG MA TRẬN

Cho ma trận A cỡ N\*M chỉ bao gồm các số nguyên dương.

Một số được coi là số may mắn nếu giá trị của nó đúng bằng khoảng cạch giữa số lớn nhất và số nhỏ nhất của ma trận.

Trong test ví dụ dưới đây, số lớn nhất là 77, số nhỏ nhất là 10. Giá trị may mắn là 67.

Hãy tìm xem trong ma trận có tồn tại số may mắn hay không. Nếu có thì ở các vị trí nào?

**Input**

Dòng đầu ghi hai số N và M (1 &lt; N, M &lt; 50)

Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 10000.

**Output**

Ghi ra giá trị bằng số may mắn nếu tìm được. Sau đó lần lượt là các vị trí tìm thấy, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.

Nếu không tìm thấy giá trị bằng số may mắn nào thì ghi ra NOT FOUND

**Ví dụ**

 | **Input** | **.Output** |
|---|---|
| 6 4  23 21 77 10  13 13 22 14  28 67 28 23  29 77 11 67  16 51 24 21  13 25 77 77 | 67  Vi tri \[2\]\[1\]  Vi tri \[3\]\[3\] |

### PY02058 - SỐ ĐẸP TRONG MA TRẬN

Cho ma trận A cỡ N\*M chỉ bao gồm các số nguyên dương.

Một số được coi là số may mắn nếu giá trị của nó đúng bằng khoảng cách giữa số lớn nhất và số nhỏ nhất của ma trận.

Trong test ví dụ dưới đây, số lớn nhất là 77, số nhỏ nhất là 10. Giá trị may mắn là 67.

Hãy tìm xem trong ma trận có tồn tại số may mắn hay không. Nếu có thì ở các vị trí nào?

**Input**

Dòng đầu ghi hai số N và M (1 &lt; N, M &lt; 50)

Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 10000.

**Output**

Ghi ra giá trị bằng số may mắn nếu tìm được. Sau đó lần lượt là các vị trí tìm thấy, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.

Nếu không tìm thấy giá trị bằng số may mắn nào thì ghi ra NOT FOUND

**Ví dụ**

 | **Input** | **.Output** |
|---|---|
| 6 4  23 21 77 10  13 13 22 14  28 67 28 23  29 77 11 67  16 51 24 21  13 25 77 77 | 67  Vi tri \[2\]\[1\]  Vi tri \[3\]\[3\] |

### PY02059 - SỐ NGUYÊN TỐ TRONG MA TRẬN

Cho ma trận A cỡ N\*M chỉ bao gồm các số nguyên dương.

Hãy tìm số nguyên tố lớn nhất trong ma trận và các vị trí có giá trị bằng số nguyên tố lớn nhất đó.

**Input**

Dòng đầu ghi hai số N và M (1 &lt; N, M &lt; 50)

Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 1000.

**Output**

Ghi ra giá trị của số nguyên tố lớn nhất. Sau đó lần lượt là các vị trí của số nguyên tố lớn nhất, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.

Nếu không tìm thấy số nguyên tố nào thì ghi ra NOT FOUND

**Ví dụ**

 | **Input** | **.Output** |
|---|---|
| 6 4  23 21 26 10  13 13 22 14  28 29 28 23  29 19 11 19  16 26 24 21  13 25 21 29 | 29  Vi tri \[2\]\[1\]  Vi tri \[3\]\[0\]  Vi tri \[5\]\[3\] |

### PY02060 - BÀI D. BỘI SỐ CHUNG NHỎ NHẤT

Bội số chung nhỏ nhất của hai số nguyên x và y (viết tắt LCM(x, y)) là số nguyên dương nhỏ nhất chia hết cho cả x và y. Cho hai số nguyên dương a và b (a ≤ b). Hãy đếm xem có bao nhiêu cặp số nguyên (x, y) sao cho

**LCM(x,y) = a \* (a+1) \* …. \* b**

**Dữ liệu vào:** Dòng đầu ghi số bộ test (không quá 10). Mỗi test ghi trên một dòng hai số a và b (a ≤ b ≤ 106)

**Kết quả:**

Với mỗi bộ test, ghi ra số lượng cặp (x, y) thỏa mãn điều kiện đề bài. Vì kết quả có thể rất lớn nên hãy ghi kết quả theo modulo 109 + 7.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  2 3  5 5 | 9  3 |

### PY02061 - TÍNH TÍCH CHẬP MA TRẬN

Phép tích chập (convolution) là kỹ thuật quan trọng trong xử lý ảnh. Kết quả phép tích chập giữa ma trận x\[\] và ma trận kernel h\[\] được xác định bằng công thức:

![](./img/PY02061_0.png)

Trong đó ma trận kernel có kích thước bằng 2k+1. Với kernel 3x3 thì -1 ≤ u,v ≤ 1, do đó, giá trị các phần tử của ma trận kết quả có dạng:

![](./img/PY02061_1.png)

Cho ma trận ảnh và ma trận kernel 3x3. Nhiệm vụ của bạn là hãy thực hiện phép nhân tích chập của 2 ma trận, sau đó tính **tổng tất cả các phần tử của ma trận thu được.**

![](./img/PY02061_2.png)

Giải thích test: Vị trí ô đầu tiên của ma trận kết quả:

![](./img/PY02061_3.png)

**Dữ liệu vào:**

- Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
- Mỗi test bắt đầu bởi hai số nguyên N và M (3 ≤ N,M ≤ 300).
- Kế tiếp là N dòng, mỗi dòng gồm M số nguyên mô tả ma trận ảnh.
- 3 dòng tiếp theo, mỗi dòng gồm 3 số nguyên mô tả ma trận kernel.
- Giá trị các phần tử của hai ma trận có giá trị tuyệt đối không vượt quá 100.
 
**Kết quả:**

- Với mỗi test, hãy in ra **tổng các phần tử của ma trận mới tìm được.**
 
**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 2  4 4  2 1 0 0  3 2 1 1  4 3 2 1  2 2 1 0  -1 -1 -1  -1 8 -1  -1 -1 -1  3 3  1 2 3  4 5 6  7 8 9  1 1 1  1 1 1  1 1 1 | 10  45 |

### PY02062 - DÃY SỐ ĐỘC ĐẮC

Cho dãy số A\[\] có N phần tử. Một dãy con X chứa các phần tử liên tiếp của A\[\] được gọi là “độc nhất”, nếu như tồn tại một phần tử xuất hiện duy nhất đúng một lần trong X.

Dãy số A\[\] được gọi là “độc đắc” nếu như mọi dãy con liên tiếp có độ dài nhỏ hơn N đều là dãy số độc nhất. Nhiệm vụ của bạn là xác định xem dãy số đã cho có phải là “độc đắc” hay không?

**Dữ liệu vào:**

- Dòng đầu tiên là số lượng bộ test T (1 ≤ T ≤ 20).
- Mỗi test gồm số đầu tiên là số lượng phần tử N (2 ≤ N ≤ 105)
- Dòng tiếp theo gồm N số nguyên không âm A\[i\], có giá trị không vượt quá 109.
 
**Kết quả:**

- Với mỗi test, hãy in ra đáp án tìm được trên một dòng. Nếu dãy số là độc đắc, in ra “YES”. In ra “NO” trong trường hợp ngược lại.
 
**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 5  5  1 2 3 4 5  7  1 2 3 4 3 4 1  5  1 1 1 1 1  5  1 2 5 2 1  5  5 5 2 5 5 | YES  NO  NO  YES    NO |

### PY02063 - TÍCH LỚN NHẤT

Cho dãy số A gồm N phần tử là các số nguyên. Hãy tính tích lớn nhất của **2 hoặc 3** phần tử trong dãy.

**Input**

Dòng đầu tiên ghi số N (3 ≤ N ≤ 10000)

Dòng thứ 2 ghi N số của dãy A (|Ai| ≤ 1000)

**Outpput**

Ghi ra kết quả trên một dòng

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 6  5 10 -2 3 5 2 | 250 |

### PY02065 - DIỆN TÍCH TOÀN PHẦN

Trên mỗi ô của vùng diện tích có kích thước MxN, các khối vuông đơn vị (kích thước 1x1x1) được xếp chồng lên nhau để tạo thành một khối lớn có chiều cao bằng H\[i, j\]. Các khối lớn khi được đặt cạnh nhau sẽ che phủ một phần mặt bên của chúng.

Nhiệm vụ của bạn là hãy tính diện tích toàn phần của khối thể tích thu được, bao gồm cả phần bề mặt trên, mặt đáy và bốn mặt xung quanh.

**Dữ liệu vào:**

- Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
- Mỗi test bắt đầu bởi hai số nguyên M và N. (0 ≤ M, N ≤ 1000).
- M dòng tiếp theo, mỗi dòng gồm N số nguyên mô tả chiều cao của ô (i, j). Chiều cao của mỗi ô không vượt quá 1000.
 
**Kết quả:**

- Với mỗi test, in ra diện tích toàn phẩn của khối thể tích được tạo thành.
 
**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 5  1 1  1  1 2  1 2  1 1  2  3 3  1 1 1  1 1 1  1 1 1  3 3  1 1 1  1 2 0  1 0 2 | 6  14  10  30  38 |

### PY02066 - BÀI TOÁN ĐẾM

Ngày thi chung kết ICPC PTIT 2020, các lập trình viên đang say sưa đọc đề và fix bug trong Hội trường 1, nhưng từ Ký túc xá thì nhóm bạn nữ xinh đẹp nào đó liên tục đồng thanh lặp đi lại lại câu hát quen thuộc:

*“1, 2, 3, 5 anh có đánh rơi nhịp nào không?*

*Nếu câu trả lời là có …”*

Để cho phù hợp với tình hình thời sự và giảm bớt căng thẳng cho các bạn thí sinh, ban tổ chức quyết định thêm một bài toán đơn giản: cho một dãy các số nguyên đếm tăng dần. Hỏi có số nào bị “đánh rơi” khi đếm hay không? Giả sử một dãy đếm chính xác thì luôn luôn đếm bắt đầu từ 1.

**Dữ liệu vào:**

- Dòng đầu ghi số N là số con số được đếm (1 ≤ N ≤ 100)
- Các dòng tiếp theo ghi đủ N số A\[i\] theo thứ tự tăng dần (1 ≤ A\[i\] ≤ 200). Các số phân cách bởi khoảng trống hoặc xuống dòng.
 
**Kết quả:**

- Nếu phép đếm là đầy đủ, chính xác thì ghi ra **Excellent!**
- Hoặc lần lượt liệt kê các số bị đánh rơi, mỗi số trên một dòng.
 
**Ví dụ:**

 | **Input 1** | **Output 1** |
|---|---|
| 4  1 2 3 5 | 4 |
| **Input 2** | **Output 2** |
| 7  4 5 7 8 9  10 11 | 1  2  3  6 |
| **Input 3** | **Output 3** |
| 5  1 2 3  4  5 | Excellent! |

### PY02067 - DÃY SỐ TƯƠNG THÍCH

Cho dãy số nguyên A\[\] gồm có N phần tử. Nhiệm vụ của bạn là tìm dãy số B\[\] có tổng phần tử nhỏ nhất thỏa mãn tính chất A\[i\] **/** B\[i\] = A\[i+1\] **/** B\[i+1\] với mọi chỉ số i (0 ≤ i ≤ N-2).

Phép chia trong bài toán này là phép chia nguyên (tức là chỉ lấy phần nguyên của kết quả: ví dụ 5/3 = 1).

**Dữ liệu vào:**

Dòng đầu tiên là số lượng phần tử N (1 ≤ N ≤ 1000).

Dòng tiếp theo gồm N số nguyên A\[i\] (1 ≤ A\[i\] ≤ 2000).

**Kết quả:**

In ra một số nguyên là tổng các phần tử của dãy số B\[\] tìm được.

**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 5  18 27 16 22 6 | 25 |

*Giải thích test: Dãy B\[\] tìm được là 5, 7, 5, 6, 2.*

### PY02068 - XỬ LÝ ẢNH

Phương pháp làm mịn ảnh được thực hiện bằng cách sử dụng phép tích chập (convolution) giữa ma trận ảnh và một ma trận kernel có dạng:

![](./img/PY02068_0.png)

Ma trận kernel trong ví dụ trên có kích thước bằng 5. Với ma trận kernel có kích thước L = 2k + 1, giá trị điểm ảnh *(i,j)* của ma trận mới sẽ bằng tổng của (2k + 1) x (2k + 1) phần tử (*i+u, j+v)* với mọi –k ≤ u,v ≤ k, sau đó chia cho (2k + 1) x (2k + 1). Kết quả điểm ảnh mới thu được sau khi thực hiện phép chia sẽ được làm tròn xuống.

Cho ma trận ảnh đầu vào và kích thước *L* của ma trận kernel, nhiệm vụ của bạn là hãy in ra ma trận ảnh sau khi được làm mịn.

**Dữ liệu vào:**

Dòng đầu tiên là số lượng bộ test *T* (T ≤ 10).

Mỗi test bắt đầu bởi hai số nguyên *N*, *M* và *L (3 ≤ N,M ≤ 500; L ≤* min*(n,m))*. *L* được đảm bảo là một số nguyên lẻ.

Kế tiếp là *N* dòng, mỗi dòng gồm *M* số nguyên mô tả ma trận ảnh đầu vào, có giá trị trong phạm vi từ 0 tới 255.

**Kết quả:**

Với mỗi test, hãy in ra ma trận ảnh sau khi đã được làm mịn.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 2  4 4 3  2 1 0 0  3 2 1 1  4 5 2 1  2 2 9 0  3 3 3  1 2 3  4 5 6  7 8 9 | 2 1  3 1  5 |

Giải thích test 1: Giá trị phần tử (1,1) = floor\[(2+1+0+3+2+1+4+5+2) / 9\] = floor \[20/9\] = 2.

### PY02069 - SỐ THUẬN NGHỊCHTRONG MA TRẬN

Cho ma trận A cỡ N\*M chỉ bao gồm các số nguyên dương.

Một số được coi là thuận nghịch nếu có từ 2 chữ số trở lên và nếu viết theo thứ tự ngược lại giá trị vẫn không thay đổi so với giá trị ban đầu. Ví dụ: 99, 121, 1331

Hãy tìm số thuận nghịch lớn nhất trong ma trận và các vị trí có giá trị bằng số thuận nghịch lớn nhất đó.

**Input**

Dòng đầu ghi hai số N và M (1 &lt; N, M &lt; 50)

Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 10000.

**Output**

Ghi ra giá trị của số thuận nghịch lớn nhất. Sau đó lần lượt là các vị trí của số thuận nghịch lớn nhất, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.

Nếu không tìm thấy số thuận nghịch nào thì ghi ra NOT FOUND

**Ví dụ**

 | **Input** | **.Output** |
|---|---|
| 6 4  23 21 77 10  13 13 22 14  28 29 28 23  29 77 11 19  16 26 24 21  13 25 77 77 | 77  Vi tri \[0\]\[2\]  Vi tri \[3\]\[1\]  Vi tri \[5\]\[2\]  Vi tri \[5\]\[3\] |

### PY02071 - TỔNG CÁC SỐ TỰ NHIÊN

Cho số nguyên dương N. Nhiệm vụ của bạn là hãy liệt kê tất cả các cách biểu diễn N thành tổng các số tự nhiên nhỏ hơn hoặc bằng N. Phép hoán vị của một cách được xem là giống nhau.

Ví dụ với N = 5 ta có kết quả là: (5), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1) .

**Input:**

- Dòng đầu tiên đưa vào số lượng test T.
- Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là một số tự nhiên N được viết trên một dòng.
- T, n thỏa mãn ràng buộc: 1≤T, N≤10.
 
**Output:**

- Dòng đầu tiên là số lượng cách phân tích thỏa mãn.
- Dòng tiếp theo liệt kê đáp án theo mẫu ví dụ đã cho.
 
 **Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 2  4  5 | 5  (4) (3 1) (2 2) (2 1 1) (1 1 1 1)  7  (5) (4 1) (3 2) (3 1 1) (2 2 1) (2 1 1 1) (1 1 1 1 1) |

### PY02072 - ĐOẠN CON TRUNG BÌNH LỚN NHẤT

Cho dãy số A\[\] có N phần tử, N không quá 105, các số trong dãy đều nguyên dương và không quá 9 chữ số. Hãy tính độ dài của dãy con liên tiếp có trung bình cộng lớn nhất trong dãy.

Trong trường hợp có nhiều dãy con liên tiếp đều có trung bình cộng lớn nhất thì dãy nào dài hơn sẽ được chọn.

**Input**

Dòng đầu ghi số N.

Dòng thứ 2 ghi N số của dãy A\[\]

**Output**

Ghi ra độ dài dãy con liên tiếp có trung bình cộng lớn nhất tìm được.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 5  5 1 6 7 2 | 2 |

### PY02078 - TĂNG - GIẢM

Cho hai dãy số thực A\[\] và B\[\] đều có N phần tử, các giá trị là số thực và không quá 100.

Hãy tính độ dài dài nhất của dãy các vị trí (không cần liên tiếp) thỏa mãn cả hai điều kiện:

- Nếu xét các vị trí đó trên dãy A\[\] thì dãy con thu được thỏa mãn tính chất tăng dần (giá trị bằng nhau không được tính vào dãy tăng).
- Nếu xét các vị trí đó trên dãy B\[\] thì dãy con thu được thỏa mãn tính chất giảm dần (giá trị bằng nhau không được tính vào dãy giảm).
 
**Input**

Dòng đầu ghi số bộ test (không quá 100).

Mỗi bộ test bắt đầu bởi số N (không quá 500).

Tiếp theo là N dòng, mỗi dòng ghi 2 giá trị A\[i\] và B\[i\]

**Output**

Với mỗi test, ghi ra độ dài tính được trên một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  2  1.0 1.0  1.5 0.0  3  1.0 1.0  1.0 1.0  1.0 1.0  6  1.5 9.0  2.0 2.0  2.5 6.0  3.0 5.0  4.0 2.0  10.0 5.5 | 2  1  4 |

### PY02090 - MA TRẬN CON TỔNG BẰNG K

Cho ma trận đơn vị A\[\]\[\] (chỉ có các giá trị 0,1) có kích thước *N*x*M*. Nhiệm vụ của bạn là hãy đếm số lượng ma trận đơn vị con của A\[\]\[\] có tổng các phần tử bằng *K* cho trước.

**Dữ liệu vào:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 10).

Mỗi test gồm số nguyên *N*, *M* và *K (3 ≤ N, M ≤ 1000; 1 ≤ K ≤ 4)* .

*N* dòng tiếp theo, mỗi dòng gồm một xâu có độ dài bằng M, mô tả một hàng của ma trận.

**Kết quả:**

Với mỗi test, in ra số lượng hình chữ nhật có tổng bằng *K* tìm được.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 2  5 5 4  01010  10101  01010  10101  01010  4 4 4  1111  1111  1111  1111 | 21  17 |

### PY02091 - DI CHUYỂN TỐI ƯU

Trên sân thi đấu có giới hạn 109 x 109, các chú robot sử dụng công nghệ dò đường line sẽ di chuyển theo các vạch chỉ đường có sẵn. Mỗi bước, robot sẽ dịch chuyển được 1 ô đơn vị theo một trong 8 hướng. Robot có thể thực hiện được phép quay 45 độ hay 90 độ nếu như ô kế cận cũng đã được kẻ vạch.

Hình vẽ dưới đây minh họa các hướng di chuyển của robot trên một sân thi đấu có sẵn, các vị trí đánh dấu X mô tả robot không được đi theo hướng này.

![](./img/PY02091_0.png)

Nhiệm vụ của bạn là hãy lập chương trình để di chuyển robot vị trí (xA, yA) tới vị trí (xB, yB) với số bước ít nhất. Input đảm bảo hai vị trí A và B chắc chắn đã được kẻ vạch.

**Dữ liệu vào:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 10).

Mỗi test gồm số nguyên xA, yA, xB, yB mô tả tọa độ hai điểm A và B.

Tiếp theo là số nguyên N (N ≤ 105), mô tả số vạch đường chỉ dẫn.

N dòng tiếp theo, mỗi dòng gồm 3 số nguyên x, y1, y2 (y1 ≤ y2) cho biết có một vạch chỉ dẫn từ ô (x, y1) tới (x, y2). Input đảm bảo tổng số lượng số ô được kẻ vạch trên sân thi đấu không vượt quá 105. Giới hạn: 0 ≤ x, y1, y2 ≤ 109.

**Kết quả:**

Với mỗi test, in ra số bước di chuyển ít nhất tìm được.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 2  0 6 2 2  3  0 6 6  1 6 10  2 2 5  1 1 2 10  2  1 1 4  2 8 10 | 5  -1 |

### PY02092 - BÀI TOÁN HÌNH HỌC - 2

Cho N điểm trên mặt phẳng Oxy. Nhiệm vụ của bạn là tìm bao lồi của tập điểm và tính diện tích bao lồi này.

Bao lồi của một tập điểm là một đa giác có các đỉnh thuộc tập điểm đã cho và chứa tất cả N điểm.

**Input:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 100).

Mỗi test bắt đầu bởi số nguyên N (3 ≤ N ≤ 1000).

N dòng tiếp theo, mỗi dòng gồm 2 số nguyên x\[i\], y\[i\] (-1000 ≤ x\[i\], y\[i\] ≤ 1000).

**Output:**

Với mỗi test, in ra diện tích bao lồi tìm được trên một dòng. Kết quả được viết với độ chính xác 3 số sau dấu phẩy.

 | Input: | Output |
|---|---|
| 2  7  0 3  2 2  1 1  2 1  3 0  0 0  3 3  4  0 0  2 0  1 2  1 1 | 9.000  2.000 |

Giải thích test 1: Bao lồi gồm các điểm (0, 0), (3, 0), (3, 3) và (0, 3).

### PY02095 - BÀN CỜ

Một bàn cờ có dạng bảng vuông kích thước 4 \* 4, trên đó có một số quân cờ. Một quân cờ chỉ có thể di chuyển sang 1 ô kề cạnh còn trống, mỗi di chuyển như vậy được gọi là 1 bước di chuyển.

Cho hai trạng thái của bàn cờ, hãy chỉ ra một dãy các bước di chuyển để đưa bảng từ trạng thái xuất phát đến trạng thái đích với số phép di chuyển là ít nhất. Mỗi trạng thái được mô tả là một ma trận 4 \* 4 trong đó số ô ở hàng i, cột j là 1 nếu tại vị trí (i,j) tương ứng có quân cờ đang đứng hoặc bằng 0 nếu không có.

**Input**

- Gồm 2 \* 4 dòng thể hiện ma trận mô tả trạng thái xuất phát và trạng thái đích. 4 dòng đầu tiên thể hiện ma trận xuất phát, 4 dòng tiếp theo là ma trận đích.
- Input luôn đảm bảo là có nghiệm.
 
**Output**

- Dòng đầu tiên ghi k là số ít nhất các phép biến đổi tìm được.
- K dòng tiếp, mỗi dòng mô tả 1 phép biến đổi, theo đúng trình tự biến đổi, gồm 4 số nguyên dương u, v, x, y thể hiện di chuyển quân cờ ở vị trí (u, v) sang vị trí (x, y).
 
**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 1111  1111  0000  0000  0000  0000  1111  1111 | 16  2 1 3 1  1 1 2 1  2 2 3 2  1 2 2 2  2 3 3 3  1 3 2 3  2 4 3 4  1 4 2 4  3 1 4 1  2 1 3 1  3 2 4 2  2 2 3 2  3 3 4 3  2 3 3 3  3 4 4 4  2 4 3 4 |

### PY02096 - VỊ TRÍ CHẴN

Cho trước 1 chữ số d (0 ≤ d ≤ 9) , ta gọi họ số đặc biệt của d là tập các số tự nhiên mà chữ số d chỉ xuất hiện tại vị trí chẵn (không xuất hiện trong vị trí lẻ).

Ví dụ: Số 1717171 là 1 số trong họ số đặc biệt của chữ số 7

Số 20 là 1 số trong họ số đặc biệt của chữ số 2.

Bây giờ, việc của bạn là: Cho trước 1 chữ số d, hãy đếm số lượng các số thuộc họ số đặc biệt của d nằm trong đoạn từ \[a,b\] mà là bội số của 1 số m cho trước.

**Input:**

Dòng đầu tiên gồm 2 số m và d (1 ≤ m ≤ 2000, 0 ≤ d ≤ 9)

Dòng thứ 2 gồm 2 số a và b ( a ≤ b, số chữ số của cả a và b bằng nhau, không vượt quá 2000 và không có chữ số 0 ở đầu).

**Output:**

In ra kết quả bài toán. Vì kết quả bài toán có thể rất lớn nên kết quả in ra phải được lấy dư theo 109 + 7

Ví dụ:

 | **Input** | **Output** |
|---|---|
| 43 3  587 850 | 1 |

Giải thích test:

Trong khoảng từ 587 đến 850 chỉ có duy nhất 1 số thuộc họ số đặc biệt của chữ số 3 mà là bội của 43 đó là 731 (số 3 xuất hiện tại vị trí số 2 là vị trí chẵn)

### PY02097 - DÃY CON TĂNG DÀI NHẤT 2 CHIỀU

Cho N cặp số Ai (xi, yi). Cặp (x1, y1) &lt; (x2,y2) nếu như x1 &lt; x2 và y1 &lt; y2.

Nhiệm vụ của bạn là hãy tìm dãy con tăng dài nhất trên mảng các cặp số này.

**Input:**

Dòng đầu tiên là số nguyên N (N &lt;= 100 000).

N dòng tiếp theo, mỗi dòng gồm 2 số nguyên xi, yi. Các số có giá trị tuyệt đối không vượt quá 109.

**Output:**

In ra một số nguyên là độ dài dãy con tăng dài nhất tìm được.

 | Input: | Output |
|---|---|
| 8  1 3  3 2  1 1  4 5  6 3  9 9  8 7  7 6 | 3 |

### PY03013 - ĐẾM CHỮ SỐ

Cho 2 số nguyên A, B. Nhiệm vụ của bạn là hãy đếm xem mỗi chữ số sẽ xuất hiện bao nhiêu lần nếu như liệt kê tất cả các số từ A đến B.

**Input**

- Số đầu tiên là số lượng bộ test T (T ≤ 5000). Mỗi test gồm 2 số nguyên A và B.
 
**Output**

- Với mỗi test, hãy in ra trên một dòng 10 số nguyên, là tần số xuất hiện của các chữ số từ 0 đến 9.
 
**Example**

 | **Input** | **Output** |
|---|---|
| 3  1 9  10 456  123 2437 | 0 1 1 1 1 1 1 1 1 1  85 195 195 195 152 92 85 84 84 84  661 1738 1206 770 700 662 662 662 661 661 |

**Subtask 1:** 50% số test đầu tiên, 1 ≤ A ≤ B ≤ 104.

**Subtask 2:** 50% số test còn lại, 1 ≤ A ≤ B ≤ 108.

### PYKT039 - DÃY SỐ PHÙ HỢP

Cho hai dãy số A\[\] và B\[\] có cùng N phần tử. Dãy số A\[\] được gọi là phù hợp với dãy số B\[\] khi và chỉ khi tồn tại một phép sắp đặt lại các phần tử trong A\[\] và B\[\] sao cho phần tử thứ i của A\[\] nhỏ hơn hoặc bằng phần tử thứ i của mảng B\[\] (với tất cả vị trí trong dãy).

Hãy xác định hai dãy số A\[\] và B\[\] có phù hợp với nhau hay không?

**Input**:

Dòng đầu tiên đưa vào số lượng bộ test T (T≤100).

Những dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm 3 phần: phần thứ nhất là số N; phần thứ hai là N số của A\[\]; phần thứ 3 là N số của B\[\].

(1≤N≤100, 0≤A\[i\], B\[i\]≤1000)

**Output:**

Đưa ra kết quả mỗi test theo từng dòng. Kết quả “YES” nếu A\[\] phù hợp với B\[\], ngược lại đưa ra “NO”.

**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 2  4  7 5 3 2  5 4 8 7  8  7 5 3 2 5 105 45 10  2 4 0 5 6 9 75 84 | YES  NO |

### PYKT041 - ĐẾM CẶP ĐỒNG XU

Cho một lưới hình vuông kích thước N\*N. Trên một số ô của lưới người ta đặt các đồng xu (ký hiệu bằng chữ cái C (coin)). Hãy đếm xem có thể lấy ra bao nhiêu cặp đồng xu ở cùng một hàng hoặc cùng một cột.

**Input**

Dòng đầu tiên ghi số N (1 ≤ N ≤ 100)

N dòng tiếp theo mô tả trạng thái của lưới, chữ cái C ứng với vị trí có đồng x, dấu chấm tương ứng với ô trống)

**Output**

Ghi ra số cặp đồng xu đếm được.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 4  CC..  C..C  .CC.  .CC. | 9 |

### PYKT066 - DÃY CON NGẮN NHẤT

Cho dãy số A\[\] có N phần tử. Nhiệm vụ của bạn là tìm dãy con liên tiếp có độ dài nhỏ nhất, sao cho Ước số chung lớn nhất của tất cả các phần tử trong dãy đúng bằng K.

**Input**

- Dòng đầu tiên là số lượng bộ test T (T &lt;= 10).
- Mỗi test bắt đầu bằng 2 số nguyên N và K.
- Dòng tiếp theo gồm N số nguyên A\[i\] .
 
**Giới hạn:** 1 &lt;= N &lt;= 1000; 1 &lt;= A\[i\], K &lt;= 10^9

**Output**

- Với mỗi test, hãy in ra đáp án trên một dòng. Nếu không tìm được dãy con nào, in ra -1.
 
**Ví dụ:**

 | Input | Output |
|---|---|
| 3  8 3  6 9 7 10 12 24 36 27  4 3  2 4 6 8  4 6  1 2 3 6 | 2  -1  1 |

### PYKT067 - HOÁN VỊ NGƯỢC

Cho số nguyên dương N. Nhiệm vụ của bạn là hãy liệt kê tất cả các hoán vị của 1, 2, .., N theo thứ tự ngược. Ví dụ với N = 3 ta có kết quả: 321, 312, 231, 213, 132, 123.

**Input:**

- Dòng đầu tiên đưa vào số lượng test T.
- Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là một số tự nhiên N được viết trên một dòng.
- T, n thỏa mãn ràng buộc: 1≤T, N≤10.
 
**Output:**

- Với mỗi test, dòng đầu tiên đưa ra số lượng hoán vị. Dòng thứ hai liệt kê các hoán vị ngược tìm được.
 
 **Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 2  2  3 | 2  21 12  6  321 312 231 213 132 123 |

### PYKT069 - DANH SÁCH CA THI

Học viện Hoàng gia tổ chức thi thời kỳ giãn cách theo các hình thức thi linh hoạt, phù hợp với từng môn học.

Mỗi ca thi gồm các thông tin:

- Mã ca thi: tự động tăng, tính từ C001
- Ngày thi: đúng định dạng dd/mm/yyyy
- Giờ thi: theo đúng định dạng hh:mm
- Phòng thi: một dãy chữ số đại diện cho ID phòng online, không quá 12 chữ số
 
Hãy nhập danh sách các ca thi và sắp xếp theo thời gian thi (từ sớm nhất đến muộn nhất). Nếu hai ca thi cùng giờ thì sắp xếp theo mã ca thi tăng dần.

**Input – file văn bản CATHI.in**

Dòng đầu ghi số ca thi. Mỗi ca thi ghi trên 3 dòng gồm Ngày, Giờ và ID phòng thi.

**Output**

Ghi ra danh sách các ca thi theo thứ tự thời gian, nếu cùng giờ thì sắp xếp theo mã ca thi.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  09/01/2022    15:30    70172  09/01/2022    10:00    70279 | C002 09/01/2022 10:00 70279  C001 09/01/2022 15:30 70172 |

### PYKT070 - SẮP XẾP LỊCH THI

Học viện Hoàng gia tổ chức thi thời kỳ giãn cách theo các hình thức thi linh hoạt, phù hợp với từng môn học.

Thông tin về mỗi môn học gồm:

- Mã môn: xâu ký tự không có khoảng trống, không quá 15 ký tự
- Tên môn: xâu ký tự không có thể có khoảng trống, không quá 100 ký tự
- Hình thức thi: xâu ký tự không có thể có khoảng trống, không quá 100 ký tự
 
Mỗi ca thi gồm các thông tin:

- Mã ca thi: tự động tăng, tính từ C001
- Ngày thi: đúng định dạng dd/mm/yyyy
- Giờ thi: theo đúng định dạng hh:mm
- Phòng thi: một dãy chữ số đại diện cho ID phòng online, không quá 12 chữ số
 
Lịch thi được xây dựng dựa trên mã môn và mã ca thi và mã nhóm lớp. Theo quy định, nhóm lớp đơn giản là các giá trị chữ số, bắt đầu từ 01 và không quá 99. Mỗi nhóm sẽ có số sinh viên tham gia ca thi đó.

Hãy nhập lịch thi và sắp xếp lại theo thứ tự thời gian. Nếu cùng giờ thì sắp theo mã ca thi (thứ tự từ điển).

Input – gồm 3 file văn bản.

**MONTHI.in**

Dòng đầu ghi số môn học. Mỗi môn ghi trên 3 dòng lần lượt là mã môn, tên môn, hình thức thi.

**CATHI.in**

Dòng đầu ghi số ca thi. Mỗi ca thi ghi trên 3 dòng gồm Ngày, Giờ và ID phòng thi.

**LICHTHI.in**

Dòng đầu ghi số lượng các dòng trong lịch thi.

Mỗi dòng tiếp theo ghi 4 thông tin: mã ca thi, mã môn, mã nhóm, số sinh viên. Mỗi thông tin cách nhau một khoảng trống.

**Output**

Ghi ra danh sách lịch thi đã sắp xếp theo yêu cầu, các thông tin cần liệt kê gồm:

- Ngày thi
- Giờ thi
- ID Phòng thi
- Tên môn
- Nhóm
- Số sinh viên
 
Các thông tin liệt kê cách nhau đúng một khoảng trống

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| **MONTHI.in**  2  MUL1320  Nhap mon da phuong tien  Bai tap lon + Van dap truc tuyen  BAS1203  Giai tich 1  Thi viet + Van dap truc tuyen | 09/01/2022 10:00 70279 Giai tich 1 04 72  09/01/2022 15:30 70172 Nhap mon da phuong tien 01 46 |
| **CATHI.in**  2  09/01/2022    15:30    70172  09/01/2022    10:00    70279 |
| **LICHTHI.in**  2  C001 MUL1320 01 46  C002 BAS1203 04 72 |

### PYKT071 - SỐ KHÔNG GIẢM TRONG FILE NHỊ PHÂN

Cho hai file nhị phân DATA1.in và DATA2.in, mỗi file đều chứa một ArrayList&lt;Integer&gt;. Dữ liệu đảm bảo có không quá 100000 số trong mỗi file, và các số đều nguyên dương, không quá 4 chữ số.

Một số nguyên dương có từ 2 chữ số trở lên được gọi là không giảm nếu các chữ số từ trái sang phải của nó thỏa mãn không có chữ số đằng sau nào lại nhỏ hơn chữ số phía trước nó. Ví dụ: 899, 1134; 7778.

Hãy liệt kê các số không giảm xuất hiện trong cả hai file DATA1.in và DATA2.in, các số cần liệt kê theo thứ tự tăng dần và kèm theo số lần xuất hiện trong lần lượt từng file.

**Input**

Hai file nhị phân DATA1.in và DATA2.in

**Output**

Ghi lần lượt từng số thỏa mãn theo thứ tự tăng dần, tiếp theo là số lần xuất hiện trong file 1 rồi đến file 2.

Ví dụ

 | **Input** | **Output** |
|---|---|
| Hai file nhị phân | Lần lượt các số thỏa mãn và số lần tương ứng. Ví dụ:  59 1 19  66 6 12  1228 9 10 |

### PYKT072 - XOAY VÒNG XÂU KÝ TỰ

Cho N xâu S\[1\], S\[2\], …, S\[N\] có độ dài bằng nhau. Mỗi bước, với xâu T, bạn được phép xoay vòng 1 kí tự, tức lấy kí tự đầu tiên của T rồi chuyển xuống cuối. Ví dụ xâu “cool” sẽ chuyển thành “oolc”.

Bạn cần phải xoay N xâu sao cho tất cả chúng đều giống nhau. Hãy xác định số bước ít nhất để hoàn thành được công việc này?

**Input:**

Mỗi test bắt đầu bởi số nguyên N (1 ≤ N ≤ 50).

N dòng tiếp theo, mỗi dòng gồm xâu S\[i\] có độ dài không quá 50.

**Output:**

Với mỗi test, in ra số bước ít nhất tìm được, nếu không thể biến đổi, hãy in ra “NO”.

**Test ví dụ:**

 | Test 1 | Test 2 | Test 3 | Test 4 |
|---|---|---|---|
| Input:  4  xzzwo  zwoxz  zzwox  xzzwo  Output:  5 | Input:  2  molzv  lzvmo  Output:  2 | Input:  3  kc  kc  kc  Output:  0 | Input:  3  aa  aa  ab  Output:  -1 |

Giải thích test 1: Xoay tất cả các xâu thành “zwoxz”.

### PYKT073 - XÁC ĐỊNH THỂ LOẠI THƠ

Trong thơ ca có rất nhiều các thể thơ và những cách gieo vần khác nhau cho các bài thơ. Trong số những thể thơ đó, bạn có thể lựa chọn cho mình một loại thể thơ riêng để đem lại nhiều hiệu quả cho bài thơ và giúp cho bạn có thể thấy được sự hiệu quả trong cách truyền đạt những cung bậc cảm xúc vào trong bài thơ.

Cho danh sách các bài thơ gồm hai thể loại thơ lục bát và thơ thất ngôn tứ tuyệt.

1\. Thơ lục bát

\- Là thể thơ dân tộc.

\- Số chữ và số câu: Một cặp hai câu thơ, câu trên sáu chữ (lục), câu dưới tám chữ (bát). Một bài thơ có thể có nhiều cặp lục bát, số lượng cặp câu không hạn định.

2\. Thơ thất ngôn tứ tuyệt

\- Xuất xứ: Trung Quốc

\- Thơ trung đại, thơ cận đại

\- Là bài thơ mà mỗi dòng 7 tiếng, bài có 4 câu (Khai - Thừa - Chuyển - Hợp)

Nhiệm vụ của bạn là hãy viết chương trình xác định số lượng bài thơ và thể thơ (ghi bằng số) của từng bài từ danh sách các bài thơ có sẵn.

**Input:**

Dòng đầu tiên cho số N là tổng số dòng của tất cả các bài thơ.

N dòng tiếp theo ghi lại các câu thơ của từng bài. Các bài thơ lục bát sẽ đảm bảo không đặt liên tiếp nhau.

**Output:**

In ra kết quả số bài thơ và số tương ứng với thể thơ theo từng dòng.

 | **Input:** | **Output:** |
|---|---|
| 8  Minh ve minh co nho ta  Muoi lam nam ay thiet tha man nong  Minh ve minh co nho khong  Nhin cay nho nui nhin song nho nguon  Mot canh hai canh lai ba canh  Tran troc ban khoan giac chang lanh  Canh bon canh nam vua chop mat  Sao vang nam canh mong hon bay | 2  1  2 |

### PYKT074 - GỬI THÔNG BÁO

Một thông báo (notification) là một tin nhắn, thông điệp được hiển thị trong một thời gian ngắn trên thanh trạng thái của thiết bị nhằm gây sự chú ý của người dùng. Nó tương tự như một tin nhắn thông thường (SMS ), tuy nhiên nó khác SMS là dịch vụ này hiện nay là hoàn toàn miễn phí và cần có kết nối internet mới có thể gửi và nhận notification. và notification chỉ có thể gửi cho ứng dụng mà nhà phát triển đã đăng ký và người dùng có cài ứng dụng đó. Các notification này sẽ hiển thị trên thanh trạng thái của smartphone và tablet, thường thanh trạng thái ở phía trên cùng của màn hình. Thông thường một thông báo là được tự động kích hoạt nhằm thông báo tới người dùng là ứng dụng đó đã hoàn thành một công việc nào đó. Hoặc bạn có thể gửi thông tin khuyến mãi tới cho khách hàng của bạn, mời khách hàng tham gia một sự kiện nào đó...

Theo quy định của một số thiết bị. Nội dung thông báo chỉ được phép chứa tối đa 100 ký tự. Điều này đòi hỏi lập trình viên phải xử lý nội dung các thông báo có độ dài lớn hơn 100 ký tự bằng cách rút gọn thông tin. Tuy nhiên, việc rút gọn phải đảm bảo nguyên tắc không bị cắt giữa từ. Trong trường hợp nếu từ hiện tại làm độ dài thông báo vượt quá 100 ký tự sẽ loại bỏ từ đó khỏi thông báo.

Nhiệm vụ của bạn là hãy viết chương trình xử lý yêu cầu trên.

**Input:**

Dòng đầu tiên là số bộ test T &lt; 100.

T dòng tiếp theo mỗi dòng là một xâu ký tự có độ dài tối đa 1000 ký tự.

**Output:**

In ra kết quả các thông báo đã xử lý

 | **Input:** | **Output:** |
|---|---|
| 2    Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021    Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen | Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va    Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen |

### PYKT075 - SAO CHÉP DANH BẠ

Có một cuốn sổ tay ghi ghép tên liên lạc và số điện thoại của bạn bè, người thân.

Do quá trình ghi chép, thứ tự được ghi lại dựa vào ngày ghi chép nên chưa được sắp xếp theo họ tên.

Để thuận lợi trong quá trình lưu trữ và sử dụng, người ta đã chuyển toàn bộ thông tin từ sổ tay lên lưu trữ trên điện thoại.

Dữ liệu trên điện thoại khi hiển thị đã được sắp xếp theo tên liên lạc. Lưu ý, nếu tên trùng nhau thì sắp xếp theo họ đệm.

Cho thông tin danh sách liên lạc được ghi chép như mẫu từ tập tin SOTAY.txt, hãy đưa ra dữ liệu hiển thị trên điện thoại vào tập tin DIENTHOAI.txt

Input: Lịch sử ghi chép theo ngày, mỗi ngày có thể ghi chép nhiều thông tin liên lạc. Họ tên tối đa 100 ký tự, số điện thoại có 10 chữ số.

Ví dụ:

 | SOTAY.txt | DIENTHOAI.txt |
|---|---|
| Ngay 15/11/2021  Nguyen Van A  0914141581  Nguyen Van B  0921241515  Ngay 16/11/2021  Tran Van C  0935141141 | Nguyen Van A: 0914141581 15/11/2021  Nguyen Van B: 0921241515 15/11/2021  Tran Van C: 0935141141 16/11/2021 |

### PYKT078 - SẮP XẾP DÃY SỐ

Cho dãy số nguyên x1 , x2 , … ,x và số nguyên m

\- Tìm giá trị lớn nhất của dãy số.

\- Chèn m vào trước vị trí đầu tiên có giá trị bằng giá trị lớn nhất.

\- Sắp xếp lại dãy số sau chèn sao cho phần tử âm về đầu dãy, phần tử dương và bằng 0 về cuối dãy sao cho trật tự các phần tử không thay đổi.

**Input:**

Dòng đầu tiên cho T là số lượng bộ test.

Mỗi bộ test bao gồm hai dòng, dòng 1 cho số n &lt; 1000 là số lượng phần tử và số m sao cho -109 &lt; m &lt; 109.

Dòng thứ 2 của bộ test bao gồm m số nguyên -109 &lt; Xi &lt; 109

**Output:**

In ra kết quả theo từng dòng

 | **Input:** | **Output:** |
|---|---|
| 1  5 3  -1 2 3 4 -1 | -1 -1 2 3 3 4 |

### PYKT079 - ĐIỀN SỐ

Cho mảng A\[\] gồm n số nguyên dương. Gọi L, R là max và min các phần tử của A\[\]. Nhiệm vụ của bạn là tìm số phần tử cần thiết cần thêm vào mảng để mảng có đầy đủ các số trong khoảng \[L, R\]. Ví dụ A\[\] = {5, 7, 9, 3, 6, 2 } ta nhận được kết quả là 2 tương ứng với các số còn thiếu là 4, 8.

**Input:**

- Dòng đầu tiên đưa vào số lượng bộ test T.
- Những dòng kế tiếp đưa vào T bộ test. Mỗi bộ test gồm hai dòng: dòng đầu tiên đưa vào n, tương ứng với số phần tử của mảng A\[\]; dòng tiếp theo là n số A\[i\].
- T, n, A\[i\] thỏa mãn ràng buộc: 1≤ T ≤100; 1≤ n, A\[i\] ≤103.
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
 **Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 2    5    4 5 3 8 6    3    2 1 3 | 1    0 |

### PYKT083 - THU PHÍ XE Ô TÔ

Mới đây, Sở Giao thông Vận tải TP Hà Nội đã thông tin chính thức về Đề án "Thu phí phương tiện cơ giới đường bộ đi vào một số khu vực nhằm giảm ùn tắc giao thông" để trình UBND thành phố Hà Nội.

Theo Sở GTVT, phí giảm ùn tắc giao thông là một loại phí mà người điều khiển phương tiện giao thông cơ giới đường bộ (ô tô) phải trả khi đi vào khu vực có nguy cơ ùn tắc giao thông. Nhằm giảm lưu lượng xe ô tô đi vào góp phần giảm ùn tắc giao thông.

Dữ liệu xe ra vào thành phố được lưu trữ đầy đủ trên hệ thống. Thông tin về phương tiện bao gồm.

Loại xe, biển số, số ghế ngồi.

Mức giá áp dụng cho các phương tiện được thực hiện theo bảng giá sau:

 | Loại xe | Số ghế | Đơn giá |
|---|---|---|
| Xe\_con | 5 | 10000 |
| Xe\_con | 7 | 15000 |
| Xe\_tai | 2 | 20000 |
| Xe\_khach | 29 | 50000 |
| Xe\_khach | 45 | 70000 |

Chiều di chuyển có hai hướng là Vào và Ra thành phố (IN và OUT). Khi xe đi vào thành phố thì phải trả phí, xe đi ra khỏi thành phố sẽ không phải trả phí.

Để thống kê lượng phương tiện ra vào thành phố thuận lợi cho quá trình vận hành và khai thác. Bạn hãy viết chương trình thực hiện thống kê theo ngày tổng số tiền thu được.

**Input:**

Dòng đầu tiên cho số N là tổng số bản ghi.

N dòng tiếp theo mỗi dòng ghi lại thông tin về lượt di chuyển của xe lần lượt là biển số, loại xe, số ghế ngồi, hướng di chuyển, ngày di chuyển.

**Output:**

In ra kết quả thống kê theo ngày, thứ tự ngày theo thứ tự xuất hiện trong input.

**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 5  30F-123.15 Xe\_con 5 OUT 06/11/2021  30F-123.15 Xe\_con 5 IN 06/11/2021  30H-123.15 Xe\_con 7 IN 06/11/2021  29H-222.68 Xe\_tai 2 IN 07/11/2021  30G-511.15 Xe\_con 5 IN 07/11/2021 | 06/11/2021: 25000  07/11/2021: 30000 |

### PYKT084 - CÂU HỎI THEO CHỦ ĐỀ - 1

Cho danh sách chủ đề và bộ câu hỏi đi kèm theo chủ đề đó trong một bộ đề bài Tiếng Anh.

Mỗi bộ câu hỏi theo chủ đề sẽ cách nhau một dòng trống. Mỗi câu hỏi được viết trên một dòng.

Ghi ra thống kê số lượng câu hỏi theo từng chủ đề. Thứ tự của chủ đề ở kết quả được giữ nguyên với thứ tự xuất hiện trong dữ liệu vào.

**Input:**

Dòng đầu cho tổng số dòng dữ liệu

Các dòng tiếp theo là danh sách các chủ đề, câu hỏi.

**Output:**

In ra kết quả theo yêu cầu

**Ví dụ**

 | **Input:** | **Output:** |
|---|---|
| 9  Home/accommodation  What kind of housing/accommodation do you live in?  Who do you live with?  How long have you lived there?  Study  Describe your education  What is your area of specialization?  Why did you choose to study that major? | Home/accommodation: 3  Study: 3 |

### PYKT085 - CÂU HỎI THEO CHỦ ĐỀ - 2

Cho danh sách chủ đề và bộ câu hỏi đi kèm theo chủ đề đó trong một bộ đề bài Tiếng Anh.

Mỗi bộ câu hỏi theo chủ đề sẽ cách nhau một dòng trống. Mỗi câu hỏi được viết trên một dòng.

Ghi ra thống kê số lượng câu hỏi theo từng chủ đề. Thứ tự của chủ đề ở kết quả được giữ nguyên với thứ tự xuất hiện trong dữ liệu vào.

**Input:**

Dòng đầu cho tổng số dòng dữ liệu

Các dòng tiếp theo là danh sách các chủ đề, câu hỏi.

**Output:**

In ra kết quả theo yêu cầu

**Ví dụ**

 | **Input:** | **Output:** |
|---|---|
| 9  Home/accommodation  What kind of housing/accommodation do you live in?  Who do you live with?  How long have you lived there?  Study  Describe your education  What is your area of specialization?  Why did you choose to study that major? | Home/accommodation: 3  Study: 3 |

### PYKT086 - CHUYỂN ĐỔI NHỊ PHÂN

Cho xâu nhị phân X\[\] có độ dài n. Nhiệm vụ của bạn là hãy đổi xâu nhị phân thành một số ở hệ cơ số b, trong đó b chỉ là một trong các số 2, 4, 8, 16. Ví dụ xâu X =”10010100010010101” và b = 8 ta có kết quả là 224225 là số ở hệ cơ số 8.

**Input - file văn bản DATA.in:**

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào b là cơ số của hệ đếm; dòng tiếp theo đưa vào xâu nhị phân có độ dài n.
- T, n, X\[\] thỏa mãn ràng buộc : 1≤T≤10; 1≤ n≤105; X\[i\] =0, 1;
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
**Ví dụ:**

 | **DATA.in** | **Output:** |
|---|---|
| 2    8    10010100010010101  2    10010100010010101 | 1121127  10010100010010101 |

### PYKT087 - SỐ ĐẶC BIỆT

Với mỗi số nguyên dương N, số M được coi là số đặc biệt của N nếu M được tạo ra bằng tổng các lũy thừa không âm khác nhau của N. Ví dụ N = 4 thì M = 17 là số đặc biệt vì 17 = 40 + 42.

Viết chương trình nhập số N và số K. Sau đó in ra số đặc biệt thứ K của N nếu sắp xếp các số đặc biệt của N theo thứ tự tăng dần.

Kết quả có thể rất lớn, hãy in ra theo modulo 109 + 7.

**Input**

Dòng đầu tiên chứa một số nguyên duy nhất t (1 ≤ t ≤ 104) - số lượng bộ test.

Dòng tiếp theo chứa hai số nguyên N và K (2 ≤ N ≤ 109; 1 ≤ k ≤ 109).

**Output**

Với mỗi bộ test, ghi ra số đặc biệt thứ K của N theo modulo 109 + 7

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  3 4  2 12  105 564 | 9  12  3595374 |

**Giải thích:** Với N = 3 dãy số đặc biệt là \[1, 3, 4, 9…\]

### PYKT089 - SẮP XẾP CHẴN LẺ

Cho dãy số A\[\] có n phần tử. Hãy sắp xếp các số chẵn trong dãy theo thứ tự tăng dần và các số lẻ theo thứ tự giảm dần.

In ra dãy kết quả đã sắp xếp trong đó vị trí số chẵn và vị trí số lẻ không thay đổi so với dãy ban đầu.

**Input**

Dòng đầu ghi số n (1 &lt; n ≤ 1000)

Các dòng tiếp theo ghi đủ n số của dãy A\[\], các số đều nguyên dương và không quá 1000.

**Output**

Ghi ra dãy kết quả đã sắp xếp trong đó các vị trí của số chẵn và số lẻ không thay đổi.

**Ví dụ**

 | **Input** | **Ouput** |
|---|---|
| 10  1 2 3 4 5 6 7 7 9 6 | 9 2 7 4 7 6 5 3 1 6 |

### PYKT090 - DANH SÁCH EMAIL

Cho danh sách các email trong file CONTACT.in, hãy loại bỏ các email trùng nhau và sắp xếp các email còn lại theo thứ tự từ điển.

Chú ý: địa chỉ email thì không phân biệt chữ hoa, chữ thường. Kết quả in ra cần đưa tất cả về dạng chữ thường.

**Input - file văn bản CONTACT.in**

Gồm không quá 300 dòng, mỗi dòng ghi một địa chỉ email.

Độ dài mỗi email không quá 100 ký tự.

*Chú ý: Dữ liệu vào không có số dòng nên cần đọc đến hết file.*

**Output**

Ghi ra danh sách các email đã loại bỏ trùng nhau và sắp xếp theo thứ tự từ điển.

**Ví dụ**

 | **CONTACT.in** | **Output** |
|---|---|
| nguyenmanhson@gmail.com  sonnm@ptit.edu.vn  NGUYENMANHSON@gmail.com  SonNM@ptit.edu.vn  NguyenManhSon@GMAIL.com | nguyenmanhson@gmail.com  sonnm@ptit.edu.vn |

### PYKT099 - HIỆU CỦA HAI TẬP TỪ

Cho hai file văn bản DATA1.in và DATA2.in.

Một từ được định nghĩa là một dãy ký tự liên tiếp không có khoảng trống, dấu tab hay dấu xuống dòng. Tạm thời chưa xét đến các dấu câu trong bải toán này.

Hãy viết chương trình liệt kê tập hợp các từ có mặt trong file DATA1.in nhưng không có trong file DATA2.in và ngược lại.

Các từ được chuyển hết về dạng chữ thường trước khi so sánh. Kết quả cần liệt kê theo thứ tự từ điển.

**Input**

Hai file văn bản DATA1.in và DATA2.in, có không quá 200 dòng.

**Output**

Dòng 1 ghi các từ khác nhau có mặt trong file DATA1.in nhưng không có trong file DATA2.in.

Dòng 2 ghi các từ khác nhau có mặt trong file DATA2.in nhưng không có trong file DATA1.in.

**Ví dụ**

 | **DATA1.in** | **Output** |
|---|---|
| lap trinh huong doi tuong  ngon ngu lap trinh C++ | c++ doi ngon ngu tuong    ban co phan thanh |
| **DATA2.in** |
| lap trinh co ban  lap trinh huong thanh phan |

### PYKT12005 - PHÂN HOẠCH DÂN CƯ

Thành phố X mới xây dựng xong 2 khu đô thị mới và bắt đầu kế hoạch di chuyển dân cư. Có tổng cộng N người đăng kí chuyển đến khu đô thị mới, trong khi sức chứa của khu đô thị 1 và 2 chỉ là lần lượt C và D.

Chỉ số A\[i\] thể hiện mức độ giàu có của người thứ i. Ban quản lý dự án muốn sự giàu có ở 2 khu đô thị này là lớn nhất có thể. Chỉ số đánh giá được tính bằng tổng trung bình chỉ số giàu có của cư dân ở 2 khu độ thị mới (trung bình của khu đô thị 1 + trung bình khu đô thị 2).

Các bạn hãy tính xem khi sắp xếp tối ưu, chỉ số đánh giá này có giá trị lớn nhất bằng bao nhiêu?

**Input:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 10).

Mỗi test bắt đầu bằng số nguyên N, C và D (1 ≤ N, C, D ≤ 100 000, C + D ≤ N).

Dòng tiếp theo gồm N số nguyên A\[i\] (1≤ A\[i\] ≤ 100 000).

**Output:**

Với mỗi test in ra đáp án trên một dòng, độ chính xác là 6 chữ số sau dấu phảy.

**Ví dụ:**

 | Input: | Output |
|---|---|
| 2  2 1 1  1 5  4 2 1  1 4 2 3 | 6.000000  6.500000 |

Giải thích test 2: Phương án tối ưu là chọn 2 người số 3, 4 tới khu đô thị 1, và người số 2 tới khu đô thị còn lại. Ta có (a\[3\]+a\[4\])/2 + a\[2\] = (3+2)/2 + 4 = 6.5.

### PYKT12006 - KHUYẾN MẠI

Một cửa hàng thời trang đang thực hiện chương trình khuyến mại giảm giá. Ban đầu, giá của sản phẩm i là a\[i\], khi đến tuần giảm giá, giá của chúng giảm xuống còn b\[i\]. Tuy nhiên, chủ cửa hàng rất khôn, nhằm đánh lừa khách hàng, mỗi số sản phẩm giá tăng lên chứ không hề giảm xuống.

Nhận biết được quy luật này, Tí mặc dù cần phải mua tổng cộng N sản phẩm, nhưng cậu quyết định mua ít nhất K sản phẩm trước đợt khuyến mại, và số sản phẩm còn lại sẽ mua trong đợt khuyến mại.

Giả sử rằng Tí chọn tối ưu được các sản phẩm ban đầu, các bạn hãy tính xem số tiền ít nhất Tí cần bỏ ra để mua đủ N sản phẩm là bao nhiêu?

**Input:**

Mỗi test bắt đầu bằng số nguyên N và K (1 ≤ N, K ≤ 100 000).

Dòng thứ hai gồm N số nguyên a\[i\], giá sản phẩm thứ i mà trước đợt giảm giá.

Dòng cuối gồm N số nguyên b\[i\], là giá của sản phẩm sau khi giảm giá.

(1 ≤ a\[i\], b\[i\] ≤ 10^4).

**Output:**

In ra một số nguyên là đáp án của bài toán.

**Ví dụ:**

 | Test 1 | Test 2 |
|---|---|
| Input:  3 1  5 4 6  3 1 5  Output:  10 | Input:  5 4  3 4 7 10 3  4 5 5 12 5  Output:  25 |

Giải thích test 1: Tí mua sản phẩm 3 trước khi giảm giá, và sản phẩm 1, 2 trong thời gian khuyến mại.

Giải thích test 2: Tí mua sản phẩm 1, 2, 4, 5 trước, tới đợt khuyến mại thì mua sản phẩm 3.

### PYKT12007 - TRAINING HỆ THỐNG A.I

Một hệ thống nhận diện khuôn mặt gồm có N module. Mỗi module có khả năng hoạt động chính xác bằng P\[i\]. Xác suất hoạt động chính xác của hệ thống được xác định bằng tích của tất cả các module.

Để tăng độ chính xác của hệ thống, bạn phải thực hiện train dữ liệu cho mỗi module. Tuy nhiên, việc này mất rất nhiều thời gian và bạn chỉ có tổng cộng U đơn vị thời gian. Train một model trong X đơn vị thời gian, độ chính xác của module này tăng lên thêm X (tối đa là bằng 1).

Bạn hãy xác định xem sau khi training, độ chính xác lớn nhất mà hệ thống đạt được là bao nhiêu?

**Input:**

Dòng đầu tiên là số lượng bộ test T (1 ≤ T ≤ 100).

Mỗi test gồm số nguyên dương N (1 ≤ N ≤ 50).

Dòng tiếp theo là số thực U.

Dòng cuối gồm N số thực P\[i\] (0 ≤ P\[i\] ≤ 1).

**Output:**

Với mỗi test in ra trên một dòng đáp án tìm được với độ chính xác 10^-6.

**Ví dụ:**

 | Input: | Output |
|---|---|
| 2  4  1.4000  0.5000 0.7000 0.8000 0.6000  2  1.0000  0.0000 0.0000 | 1.000000  0.250000 |

### PYKT12008 - MUA QUÀ

Tí và Tèo được cô giáo cử đi mua quà để thưởng cho các thành viên trong lớp. Lớp học có tất cả M bạn học sinh, vì vậy hai bạn phải mua M món quà.

Tại cửa hàng quà lưu niệm có tất cả N món quà, món thứ i có giá bán bằng c\[i\]. Tuy nhiên, có A món quà mà Tí thích, và B món quà mà Tèo thích. Hai bạn tranh nhau một hồi, cuối cùng họ quyết định chọn một danh sách quà sao cho có ít nhất K món đồ mà cả 2 bạn cùng thích.

Các bạn hãy xác định xem số tiền ít nhất cần phải chi trả để Tí và Tèo có thể mua được đủ số quà và thỏa mãn điều kiện của hai bạn hay không?

**Input:**

Dòng đầu tiên là N, M, K (1 ≤ N ≤ 100 000, 1 ≤ M, K ≤ N).

Dòng tiếp theo gồm N số nguyên lần lượt là giá bán c\[i\] của món quà thứ i (1 ≤ c\[i\] ≤ 10^9).

Dòng tiếp gồm số nguyên A, theo sau A số nguyên x\[i\], lần lượt là số thứ tự các món quà mà Tí thích.

Dòng tiếp gồm số nguyên B, theo sau B số nguyên y\[i\], lần lượt là số thứ tự các món quà mà Tèo thích. (1 ≤ x\[i\], y\[i\] ≤ N).

**Output:**

In ra một số nguyên là đáp án tìm được. Nếu không có phương án nào thỏa mãn, in ra -1.

**Ví dụ:**

 | Test 1 | Test 2 | Test 2 |
|---|---|---|
| Input:  4 3 2  3 2 2 1  2  1 2  2  1 3  Output:  7 | Input:  4 3 2  3 2 2 1  2  1 2  3  4 1 3  Output:  6 | Input:  4 2 2  3 2 2 1  2  1 2  3  4 1 3  Output:  -1 |

Giải thích test 1: Mua quà 1, 2 và 3.

### PYKT12009 - DÃY SỐ YẾU NHẤT

Cho dãy số A\[\] gồm có N phần tử. Tổng tuyệt đối của một dãy số là giá trị tuyệt đối của tổng tất cả các phần tử (tính tổng xong mới lấy giá trị tuyệt đối).

Độ yếu của dãy số A\[\] được tính bằng giá trị lớn nhất trong số các tổng tuyệt đối của tất cả các dãy con liên tiếp của A.

Bạn hãy xác định số thực X sao cho dãy số A\[1\]-X, A\[2\]-X, …, A\[N\]-X có độ yếu là nhỏ nhất.

**Input:**

Dòng đầu tiên gồm số nguyên N (1 ≤ N ≤ 100 000).

Dòng tiếp theo gồm N số nguyên A\[i\] (-10 000 ≤ A\[i\] ≤ 10 000).

**Output:**

In ra số độ yếu của dãy A\[1\]-X, A\[2\]-X, …, A\[N\] - X.

Kết quả ghi ra với 6 chữ số phần thập phân.

**Ví dụ:**

 | Test 1 | Test 2 | Test 3 |
|---|---|---|
| Input:  3  1 2 3  Output:  1.000000 | Input:  4  1 2 3 4  Output:  2.000000 | Input:  10  1 10 2 9 3 8 4 7 5 6  Output:  4.500000 |

Giải thích test 1:

Với X = 1, dãy số mới thu được là -1, 0, 1. Dãy số này có độ yếu bằng 1.

Giải thích test 2:

Với X = 2.5, dãy số mới là -1.5 -0.5 0.5 1.5. Độ yếu của dãy số bằng 2 (|-1.5-0.5| = |0.5+1.5| = 2).

### PYKT12010 - MÁI NHÀ

Cho dãy số A\[\] gồm có N phần tử. Bạn được phép tăng, giảm một phần tử mỗi lần 1 đơn vị. Nhiệm vụ của bạn là hãy sử dụng ít bước nhất có thể để chuyển dãy số đã cho về dạng dãy số ‘mái nhà’, với các tính chất sau :

- Một phần tử lớn nhất là đỉnh (giả sử là phần tử thứ i)
- Các phần tử bên trái và bên phải giảm dần đi 1 đơn vị, tức là với mọi j, A\[j\] = A\[i\] - |i-j|
- Tất cả các phần tử A\[j\] đều phải lớn hơn 0.
 
**Input:**

Dòng đầu tiên là số nguyên N (N ≤ 5000).

Dòng tiếp theo gồm N phần tử của dãy số (1 ≤ A\[i\] ≤ 5000).

**Output:**

In ra số bước ít nhất để có thể hoàn thành bài toán trên.

**Ví dụ:**

 | Test 1 | Test 2 |
|---|---|
| Input:  5  4 5 6 2 2  Output:  3 | Input:  6  4 5 6 5 4 3  Output:  0 |

Giải thích test 1: Chuyển dãy số về 4 5 4 3 2

### PYKT12011 - XÁC SUẤT CHỌN BIT

Cho chuỗi nhị phân S có chiều dài bằng N và số nguyên K. Chọn ngẫu nhiên 2 số nguyên i, j trong khoảng từ 1 tới N.

Xác suất để S\[i\], S\[j\] đều là bit 1 và |i-j| ≤ K là bao nhiêu?

**Input**

Dòng đầu tiên là số lượng bộ test T (T ≤ 100 000).

Mỗi test bắt đầu bởi 2 số nguyên N và K.

Dòng tiếp theo gồm xâu S chứa các kí tự 0 và 1.

Chú ý: Tổng giá trị của N trong tất cả các test ≤ 100 000.

**Output**

In ra xác suất tìm được dưới dạng phân số tối giản dạng X/Y. Nếu xác suất bằng 0, in ra 0/1.

**Ví dụ:**

 | Input | Output |
|---|---|
| 2  4 3  1011  4 1  1000 | 9/16  1/16 |

### PYKT12012 - VẪN LÀ XÁC SUẤT CHỌN BIT

Chọn ngẫu nhiên một số X trong đoạn \[A, B\], sau đó chọn ngẫu nhiên một bit của X. Xác suất để bit chọn được là bit 1 bằng bao nhiêu?

**Input**

Dòng đầu tiên là số lượng bộ test T (T ≤ 200).

Mỗi test gồm 2 số nguyên A và B (1 ≤ A ≤ B ≤ 10^10).

**Output**

In ra đáp án tìm được với độ chính xác 5 chữ số sau dấu phảy.

**Ví dụ:**

 | Input | Output |
|---|---|
| 3  2 4  3 5  20 40 | 0.61111  0.66667  0.55556 |

Giải thích test 1:

(10) (11) (100)

Xác suất để chọn được bit 1 là : 1/3 x (1/2 + 1 + 1/3) = 11/18.

### PYKT12019 - PHẦN TỬ CHỐT

Cho dãy số A\[\] gồm có N phần tử. Phần tử A\[i\] được gọi là phần tử Pivot (hay phần tử chốt) nếu như nó phân hoạch dãy số thành 2 phần:

- Các phần tử bên trái có giá trị nhỏ hơn hoặc bằng A\[i\],
- Các phần tử bên phải có giá trị lớn hơn A\[i\].
 
Với dãy số A\[\] = {2, 1, 3, 4, 6, 5, 7}, có 3 phần tử chốt là 3, 4, 7. Với phần tử 3, ta có phân hoạch {2, 1}, 3 và {4, 6, 5, 7} thỏa mãn các tính chất nêu trên. Với phần tử 7, tập hợp các phần tử bên phải là một tập rỗng nên cũng thõa mãn yêu cầu.

Việc xác định được phần tử chốt đóng vai trò quan trọng trong thuật toán Quicksort. Các bạn hãy xác định xem dãy số đã cho có bao nhiêu phần tử chốt?

**Input:**

Dòng đầu tiên là số lượng bộ test (T ≤ 10).

Dòng test bắt đầu bởi số nguyên N (1 ≤ N ≤ 100 000) là số lượng phần tử của dãy số.

Dòng tiếp theo gồm N phần tử A\[i\] (0 ≤ A\[i\] ≤ 109).

**Output:**

In ra đáp án là số lượng phần tử chốt tìm được.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 3  3  1 1 1  3  1 2 3  7  2 1 3 4 6 5 7 | 1  3  3 |

### PYKT12022 - PHÉP TOÁN OR

Phép toán trên thao tác bit OR lấy 2 dãy bit có độ dài bằng nhau và thực hiện phép toán lý luận bao hàm OR trên mỗi cặp bit tương ứng. Kết quả ở mỗi vị trí sẽ là 0 nếu cả 2 bit là 0, ngược lại kết quả là 1. Trong C, C++, Java toán tử thao tác bit OR được biểu diễn bằng kí hiệu "|" (vạch đứng )

Ví dụ : 10|17 = 01010|10001=11011=27

Cho một mảng a gồm n phần tử. Một dãy con liên tiếp của a được định nghĩa là một dãy a\[l\], a\[l+\]),a\[l+2\],...,a\[r\] với 1 ≤ l ≤ r ≤ n

Ta định nghĩa phép toán OR của 1 dãy con liên tiếp của mảng a là việc thực hiện phép toán thao tác bit OR của toàn bộ các phần tử trong dãy con đó.

OR(l,r) = a\[l\] | a\[l+1\] | a\[l+2\]|...|a\[r\]

Nhiệm vụ của bạn là tính giá trị OR của toàn bộ các dãy con của một mảng a cho trước và đếm xem có bao nhiêu giá trị khác nhau.

**Input:**

Dòng thứ 1 gồm 1 số n (1 ≤ n ≤ 1e5): số phần tử của mảng a

Dòng thứ 2 gồm n số a\[1\], a\[2\], ..., a\[n\] ( 0 ≤ a\[i\] ≤ 1e9)

**Output:**

Với mỗi testcase, in ra kết quả trên 1 dòng.

**Ví dụ :**

 | Input | Output |
|---|---|
| 3  1 2 3 | 3 |

Giải thích test:

Ta có tất cả 6 dãy con: (các số trong ngoặc là vị trí đầu và cuối )

1. (1,1) -&gt; 1
2. (1,2) -&gt; 1|2 = 2
3. (1,3) -&gt; 1|2|3 = 3
4. (2,2) -&gt; 2
5. (2,3) -&gt; 2|3=3
6. (3,3) -&gt; 3
 
Có 3 giá trị khác nhau là 1, 2, 3-&gt; kết quả là 3.

### PYKT12026 - 2X-Y

Mảng a ban đầu có n số nguyên. Bạn có thể thực hiện thao tác sau nhiều lần:

\- Chọn số 2 số x và y bất kỳ trong mảng và thêm 2x – y vào mảng.

Với 1 số nguyên k, hãy kiểm tra xem bạn có thể tạo ra được số k hay không.

**Input:**

Dòng đầu tiên chứa số bộ test t (t ≤ 20).

Mỗi test có định dạng như sau:

\- Dòng đầu tiên chứa 2 số nguyên n và k (2 ≤ n ≤ 105, -109 ≤ k ≤ 109)

\- Dòng tiếp theo chứa n số nguyên ban đầu (-109 ≤ ai ≤ 109)

**Output:**

Với mỗi test, in ra “YES” nếu có thể và “NO” trong trường hợp còn lại.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 6  2 1  1 2  3 0  2 3 7  2 -1  31415926 27182818  2 1000000000000000000  1 1000000000000000000  2 -1000000000000000000  -1000000000000000000 123  6 80  -5 -20 13 -14 -2 -11 | YES  YES  NO  YES  YES  NO |

### PYKT12027 - ĐẾM CẶP NGHỊCH THẾ

Cho một dãy số a1 ... an. Một nghịch thế là một cặp số u, v sao cho u &lt; v và au &gt; av. Nhiệm vụ của bạn là đếm số nghịch thế.

**Input:**

Dòng đầu tiên chứa 2 số nguyên n (2 ≤ n ≤ 105)

Dòng tiếp theo chứa n số nguyên của mảng a (-109 ≤ ai ≤ 109)

**Output:**

In ra một số nguyên duy nhất là số cặp nghịch thế tìm được.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 3  3 1 2 | 2 |

### PYKT13007 - TỔNG CHUỖI MA TRẬN

Phép cộng hai ma trận có cùng kích thước ![](./img/PYKT13007_0.png) , ma trận tổng ![](./img/PYKT13007_1.png)  có kích thước ![](./img/PYKT13007_0.png) , phần tử đứng ở hàng thứ ![](./img/PYKT13007_3.png) , cột thứ ![](./img/PYKT13007_4.png)  xác định bởi:

![](./img/PYKT13007_5.png)

Phép nhân hai ma trận chỉ thực hiện được khi số cột của ma trận bên trái bằng số dòng của ma trận bên phải. Nếu ma trận ![](./img/PYKT13007_6.png)  có kích thước  ![](./img/PYKT13007_7.png) và ma trận ![](./img/PYKT13007_8.png)  có kích thước ![](./img/PYKT13007_9.png) , thì ma trận tích ![](./img/PYKT13007_10.png)  có kích thước ![](./img/PYKT13007_11.png) , phần tử đứng ở hàng thứ ![](./img/PYKT13007_3.png) , cột thứ ![](./img/PYKT13007_4.png)  xác định bởi:

*,11,,22,+..+*![](./img/PYKT13007_14.png)

Phép nhân ma trận có các tính chất sau:

- Tính chất kết hợp: *×(*![](./img/PYKT13007_15.png) ;
- Tính chất phân phối:
 
![](./img/PYKT13007_16.png) ;

Cần chú ý rằng phép nhân ma trận không giao hoán.

Ví dụ,

*;* ![](./img/PYKT13007_17.png) ; ...

![](./img/PYKT13007_18.png)

***Yêu cầu:*** Cho ma trận ![](./img/PYKT13007_6.png)  kích thước ![](./img/PYKT13007_20.png)  và số nguyên dương ![](./img/PYKT13007_21.png) , hãy tính *+..+*![](./img/PYKT13007_22.png) .

**Input:**

- Dòng đầu chứa hai số nguyên n và k (1 ≤ n ≤ 20, 1 ≤ k ≤ 10^9).
- Dòng tiếp theo, mỗi dòng chứa n số nguyên biểu diễn ma trận A.
 
**Output:**

In ra n dòng, mỗi dòng ![](./img/PYKT13007_23.png)  số mô tả ma trận ![](./img/PYKT13007_8.png) , vì giá trị mỗi phần tử của ma trận ![](./img/PYKT13007_8.png)  có thể rất lớn, do đó chỉ cần đưa ra chữ số cuối cùng của từng phần tử của ma trận ![](./img/PYKT13007_8.png) .

**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 2 3  0 1  1 1 | 2 4  4 6 |

### PYKT13008 - GIẢI HỆ PHƯƠNG TRÌNH TUYẾN TÍNH

Giải hệ phương trình Ax = B trong đó ma trận A có kích thước n x n, x và B là các vector cột có n phần tử:

![](./img/PYKT13008_0.png)

**Input:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 10).

Mỗi test bắt đầu bởi số nguyên N (2 ≤ N ≤ 20).

N dòng tiếp theo, mỗi dòng gồm N phần tử mô tả ma trận A.

Dòng cuối gồm N số nguyên, mô tả vector B.

Các hệ số có giá trị tuyệt đối không vượt quá 1000.

**Output:**

Với mỗi test in ra đáp án tìm được trên một dòng, in ra 3 chữ số sau dấu phảy. Nếu hệ vô nghiệm hoặc có vô số nghiệm, in ra -1.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 3  3  1 2 5  4 5 6  7 8 9  10 11 12  2  1 1  2 2  2 4  2  1 2  1 2  3 4 | -9.333 9.667 0.000  -1  -1 |

### PYKT13009 - TÍNH TỔNG 1

Cho 2 số nguyên n và K. Hãy tính giá trị biểu thức

![](./img/PYKT13009_0.png)

 theo modulo 109+7.

**Input:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 20).

Mỗi test gồm 2 số nguyên dương n và K (n ≤ 109, K ≤ 50).

**Output:**

Với mỗi test, in ra đáp án tìm được theo modulo 109 + 7.

**Ví dụ:**

 | **Input:** | **Output** |
|---|---|
| 3  1 1  4 2  10 3 | 1  30  3025 |

### PYKT13010 - TÍNH TỔNG 2

Cho 2 số nguyên n và K. Hãy tính giá trị biểu thức

![](./img/PYKT13010_0.png)

theo modulo 109+7.

**Input:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 10).

Mỗi test gồm 2 số nguyên n và K (0 ≤ K ≤ 1000, 1 ≤ n ≤ 1016).

**Output:**

Với mỗi test in ra đáp án tìm được trên 1 dòng.

**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 3  5 3  6 2  3 1 | 225  91  6 |

### PYKT13012 - TỔNG FIBONACCI

Cho một dãy số a\[\] có n phần tử, và m truy vấn.

Có 2 loại try vấn.

**Truy vấn loại 1: 1 L R X

tăng tất cả các số trong khoảng L...R thêm X đơn vị.

**Truy vấn loại 2: 2 L R .**

Giả sử f(x) là giá trị của số fibonaci thứ x, tính tổng

**f\[a\[L\]\] + f\[a\[L+1\] + ... + f\[a\[R\]\]**

( vì giá trị rất lớn nên phải chia dữ cho 109 + 7 )

**Input:**

Dòng đầu 2 số n và m. (1 &lt;= n, m &lt;= 100000)

Dòng 2 chứa n số của dãy a\[\].

m dòng sau mỗi dòng chứa một truy vấn của loại 1 hoặc loại 2.

Thời gian cho mỗi test là 1.5s

**Output:**

Mỗi truy vấn của loại 2 in 1 dòng chứa kết quả đã được mod cho 1e9+7.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 3 3  4 3 4  1 2 2 1  2 3 3  2 1 3 | 3  9 |
| 4 3  2 4 1 4  2 2 3  1 3 3 5  2 1 3 | 4  12 |

### PYKT13013 - TÍNH TỔNG TRÊN MA TRẬN

Cho một ma trận N x M (N hàng, M cột). Ban đầu, các phần tử của ma trận được gán giá trị như sau:

1 2 … M

M+1 M+2 … M+N

………………………………………………………….

(N-1)M+1 (N-1)M+2 … NM

Có K loại truy vấn, mỗi truy vấn có dạng:

- “R X Y”: Nhân hàng X của ma trận với Y
- “S X Y”: Nhân cột X của ma trận với Y
 
Nhiệm vụ của bạn là hãy tính tổng các phần tử của ma trận sau K truy vấn trên.

**Input:**

Dòng đầu tiên chứa 3 số nguyên N, M, K (1 ≤ N, M ≤ 106, K ≤ 1000).

K dòng tiếp theo, mỗi dòng chứa một truy vấn (0 ≤ Y ≤ 109).

**Output:**

In ra đáp án của bài toán theo modulo 109 + 7.

**Ví dụ:**

 | Test 1 | Test 2 |
|---|---|
| Input:  3 1 1  S 1 4  Output:  24 | Input:  3 4 4  R 2 4  S 4 2  R 3 3  R 2 0  Output:  176 |

Giải thích test 2: 1+2+3+8+27+30+33+72 = 176

1 2 3 8

0 0 0 0

27 30 33 72

### PYKT13014 - SỐ LỚN NHẤT VÀ NHỎ NHẤT

Cho N số nguyên dương A\[\]. Mỗi lần, bạn chọn một tổ hợp gồm K số, như vậy, có tất cả C(K, N) cách chọn.

Bài toán đặt ra là hãy tính tổng của sự chênh lệch giữa số lớn nhất và nhỏ nhất trong tổ hợp được chọn của tất cả C(K, N) lần.

**Input:**

Dòng đầu tiên là số nguyên N và K (1 ≤ N ≤ 105, 1 ≤ K ≤ N).

Dòng tiếp theo gồm N số nguyên A\[i\] (0 ≤ A\[i\] ≤ 109).

**Output:**

In ra đáp án tìm được theo modulo 109+7.

**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 4 2  10 20 30 40 | 100 |

Giải thích test: Có tất cả 6 khả năng: (10, 20), (20, 30), (30, 40), (10, 30), (20, 40), (10, 40).

Tổng cộng bằng 10+10+10+20+20+30 = 100.

### PYKT13015 - TÍNH LŨY THỪA

Cho các số nguyên a, b, c, d và M.

Hãy tính giá trị biểu thức

![](./img/PYKT13015_0.png)

 theo modulo M.

**Input:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 10000).

Mỗi test gồm 5 số nguyên a, b, c, d, M (0 ≤ a, b, c, d ≤ 109, 1 ≤ M ≤ 107).

**Output:**

Với mỗi test in ra đáp án tìm được trên 1 dòng.

**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 2  3 1 2 2 1000  2 1 2 2 14 | 81  2 |

Giải thích test 1: 34 = 81.

### PYKT13016 - SỐ MŨ

Tìm số nguyên x nhỏ nhất sao cho ax = b modulo M.

**Input:**

Dòng đầu tiên là số lượng bộ test T (1 ≤ T ≤ 10).

Mỗi test gồm 3 số nguyên a, b, M (2 ≤ M ≤ 1010, 1 ≤ a, b, ≤ M).

Input đảm bảo gcd(a, M) = 1.

**Output:**

Với mỗi test in ra số nguyên x nhỏ nhất tìm được. Nếu không có đáp án, in ra -1.

**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 4  3 2 5  2 5 11  3 2 100  53849 260761 306148 | 3  4  -1  7452 |

Giải thích test 1: 33 = 2 (mod 5)

Giải thích test 2: 24 = 5 (mod 11)

### PYKT13017 - BỘ BA SỐ PYTAGO (BẢN KHÓ)

3 số a, b, c được gọi là một bộ số Pytago nếu như a2 + b2 = c2.

Cho số nguyên N, nhiệm vụ của bạn là hãy đếm bộ số (a, b, c) thỏa mãn 1 ≤a, b, c≤ N-1, a ≤b và a2 + b2 = c2 (mod N).

**Input:**

Một số nguyên dương N (2 ≤ N ≤ 500 000).

**Output:**

In ra một số nguyên là số bộ 3 số tìm được.

**Ví dụ:**

 | Test 1 | Test 2 |
|---|---|
| Input:  7  Output:  18 | Input:  15  Output:  64 |

### PYKT13025 - ĐOÀN QUÂN TỐC HÀNH

Tình hình chiến sự ở vùng biển Z đang trở nên cực kì cam go. Nhà vua quyết định gửi thêm quân chi viên tới chiến trường. Trong tay nhà vua đang có quyền triệu tập k đội quân từ khắp mọi miền đất nước. Để tập trung binh lực tốt nhất, nhà vua đã triệu tập cả k đội quân đến kinh thành rồi sau đó mới di chuyển đến chiến trường. Do số lượng đoàn quân khá lớn, nhà vua quyết định để 1 đại tướng đi thuê xe để chở quân lính. Vì tình đoàn kết, tất cả các chiến sĩ từ k quân đoàn tuyên bố: Nếu di chuyển, họ muốn được di chuyển cùng tất cả các đồng đội của mình trên một xe và trên xe đó không được có tới 3 quân đoàn khác nhau vì như vậy rất dễ xảy ra xô xát. Đến đây , tướng quân rất đau đầu trong việc chọn lựa loại xe đưa các đội quân đi vì nhà vua muốn chi phí di chuyển là ít nhất. Chi phí di chuyển sẽ bằng số lượng xe thuê nhân với sức chứa của loại xe. Hãy giúp tướng quân tính toán ra chi phí nhỏ nhất để thuê xe mà thỏa mãn yêu cầu của tất cả quân lính nhé

**Input:**

Dòng đầu tiên gồm số n và k (1 ≤ n ≤ 5.105, 1 ≤ k ≤ 10000). Với n là số lượng quân lính, k là số lượng các quân đoàn. Giả sử các quân đoàn đánh số từ 1 đến k.

Dòng thứ 2 gồm n số nguyên a\[i\] (1 ≤ a\[i\] ≤ k) trong đó a\[i\] là số hiệu quân đoàn của người lính thứ i.

**Output:**

Ghi ra chi phí nhỏ nhất.

**Ví dụ :**

 | **Input** | **Output** |
|---|---|
| 6 3  3 1 2 3 2 3 | 6 |

*Giải thích:*

Có 6 người lính đến từ 3 đội quân khác nhau.

Đội quân 1 có 1 người

Đội 2 có 2 người

Đội 3 có 3 người

Cách tốt nhất là thuê 2 xe có sức chứa 3 người. Khi đó đội quân 1 và 2 sẽ lên cùng 1 xe, đội quân 3 lên 1 xe. Tổng chi phí thuê xe sẽ là 3 x 2 = 6.

### PYKT13026 - GHÉP HÌNH

Chuyện kể rằng ở một hiệu sách nọ, có 1 ông chủ đã già nên trí nhớ kém. Một hôm anh shipper đến để kiểm kê lại sách trước khi đem giao. Xui cho anh shipper là ông chủ trí nhớ lẩm cẩm, lại không nhớ hóa đơn mua sách để đâu và đã quên béng mất số lượng sách cần phải giao. Thật may là ông còn 1 vài chi tiết ông còn nhớ. Ở cửa hàng của mình, ông có các miếng bìa cát tông, khi có sách về, ông sẽ "tái chế " chúng để đựng sách. Với mỗi miếng bìa các tông hình chữ nhật có chiều dài 2 cạnh là a và b, ông sẽ cắt 4 góc của miếng bìa các tông sau đó dựng lên để thành 1 hình hộp chữ nhật. Xem hình dưới để biết thêm chi tiết :

![](./img/PYKT13026_0.png)

Dễ dàng thấy được rằng với mỗi cách cắt 4 góc ta sẽ được 1 hình hộp chữ nhật với thể tích khác nhau (đương nhiên vẫn phải đảm bảo chiều dài các cạnh &gt; 0). Ông chủ nhớ được rằng, với 3 loại hộp có thể tích lớn nhất, khi ông xếp tất cả số sách phải ship vào loại lớn nhất thì sẽ bị dư ra x cuốn sách, nếu xếp vào loại lớn thứ 2 thì sẽ dư ra y cuốn sách, xếp vào loại lớn thứ 3 thì sẽ dư ra z cuốn sách. (Ta coi mỗi cuốn sách là 1 hình lập phương 1x1x1) Ông cũng nhớ là số sách nằm trong khoảng từ l đến r (tính cả l và r). Lần này anh shipper thật sự bất lực và cầu cứu bạn, là một lập trình viên đại tài, bạn có thể giúp anh ấy tìm ra được số sách cần phải ship không ?

**Input:**   
 Dòng đầu thi số bộ test (không quá 10).

Mỗi test ghi trên một dòng 7 số lần lượt là : a,b,x,y,z,l,r

Trong đó : a,b là kích thước của bìa các tông ( 7 ≤ a ≤ b ≤ 100)

x,y,z lần lượt là số sách bị dư ra khi xếp tất cả sách vào 3 loại hộp có thể tích lớn nhất

l,r là khoảng mà số sách cần tìm nằm ở trong

**Output:**

Một số nguyên duy nhất là kết quả bài toán. Nếu có nhiều đáp án thỏa mãn, hãy đưa ra đáp án nhỏ nhất.

Note: Thể tích của hình hộp chữ nhật là : a \* b \* h với a,b là chiều dài 2 cạnh đáy và h là chiều cao

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 1  16 21 407 409 17 20000 30000 | 22457 |

*Giải thích test:*   
 Bìa các tông có kích thước là 16 x 21, 3 thể tích lớn nhất có thể đạt được khi cắt 4 góc của bìa các tông lần lượt là: 450, 416, 408.

Khi xếp 22457 cuốn sách vào loại hộp có thể tích 450 ta sẽ xếp được 49 cuốn sách mỗi hộp và còn dư 409 cuốn sách.

Tương tự với 2 loại còn lại.

### PYKT13034 - DIỆN TÍCH TAM GIÁC - 3

Cho N tam giác trên mặt phẳng Oxy. Nhiệm vụ của bạn là hãy tính diện tích bị che phủ bởi N tam giác này.

![](./img/PYKT13034_0.png)

**Input:**

Dòng đầu tiên là số nguyên N (N ≤ 100).

N dòng tiếp theo, mỗi dòng gồm 6 số nguyên x1, y1, x2, y2, x3, y3 là tọa độ của tam giác thứ i.

(-10^6 ≤ x1, y1, x2, y2, x3, y3 ≤ 106).

**Output:**

In ra đáp án tìm được với độ chính xác 6 chữ số sau dấu phảy.

 | Input: | Output |
|---|---|
| 3  1 1 5 1 3 3  1 2 5 2 5 6  1 6 5 2 1 2 | 15.000000 |

### PYKT14004 - CÂN BẰNG

Công viên PTIT thiết kế trò chơi đu quay có 4 góc. Mỗi góc ngồi được tối đa 3 người. Để chiếc đu quay này có thể vận hành an toàn thì cần sắp xếp sao cho tổng khối lượng của các góc chênh lệch ít nhất có thể.

Có đúng 12 người chơi. Hãy tính chênh lệch ít nhất có thể của nhóm “nặng nhất” và nhóm “nhẹ nhất”.

**Input**

Gồm 12 số (có thể viết trên một dòng hoặc nhiều dòng nhưng không có dòng trống) lần lượt là khối lượng của 12 người chơi (giá trị không quá 106).

**Output**

In ra giá trị chênh lệch ít nhất

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2 3 4  5 6 7 8 9 10  11 12 13 | 1 |

### PYKT14006 - PHÉP TOÁN

Có 2 nhà toán học đại tài là Greek và Macedonia họ hơn thua nhau từng li từng tí, một ngày Greek nghĩ ra bài toán khá là hay ho và này nọ đó là ông đưa ra 1 dãy số và chỉ từ phép cộng trừ để tạo ra 1 số M cho trước, ông yêu cầu Macedonia phải giải nhưng quá thông minh nên Macedonia đã giải rất nhanh và để làm khó Greek nên ông đã biến đổi bài toán của chính Greek ông cho 1 dãy n phần tử ***a1,a2,a3,…….an*** và 1 số M nhưng thay vì 2 phép toán **+,-** ông thêm 1 phép toán nữa thành ***+,** **-,** **\**** và bắt Greek phải tìm ra biểu thức phù hợp để tạo ra số M

Do không kịp suy nghĩ nên nhà toán học đã kêu gọi sự trợ giúp từ các lập trình viên. Bạn hãy tìm cách giúp ông ấy nhé !

### **Input**

- Dòng đầu chứa số n (2 ≤ n ≤ 10) và số m( m ≤ 10^18)
- Dòng thứ 2 là dãy số a1,a2,a3,…..an ( |ai| ≤ 15000 )
 
### **Output**

- Nếu có thể tìm phép toán phù hợp hãy in ra tất cả các phép toán thỏa mãn. Nếu có số âm phải để trong dấu ngoặc ( )
- Nếu không tìm thấy in ra IMPOSSIBLE
 
**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 5 20  1 2 3 4 5 | 1+2+3\*4+5=20  1+2-3+4\*5=20  1+2\*3\*4-5=20 |

### PYKT14019 - ĐẦU BẾP

Một hôm nọ, Tom khám phá ra một loại bánh mới nên mời n người bạn đến nhà để thử tay nghề của mình. Do chưa rành công thức lắm và muốn thử nghiệm nên Tom đã làm ra n chiếc bánh với tỉ lệ nguyên liệu khác nhau. Nhưng Tom biết chắc chắn rằng để chiếc bánh thứ i ngon hoàn hảo thì cần phải nướng ti phút. Tuy nhiên vì số lượng bánh lớn nên Tom đã quyết định sẽ cho hết cả n chiếc bánh vào trong lò nướng. Ở mỗi phút, Tom chỉ có thể đưa 1 và chỉ 1 chiếc bánh ra khỏi lò nướng. Gỉa sử thời điểm lấy chiếc bánh thứ i ra là xi thì độ tệ của chiếc bánh sẽ bằng trị tuyệt đối của (ti - xi). Tom muốn tổng độ tệ của n chiếc bánh là ít nhất có thể. Và giờ Tom đang rất đau đầu với việc đó. Bạn có thể giúp Tom không ?

**Input:**

Dòng đầu tiên gồm 1 số t là số lượng bộ test t (1 ≤ t ≤ 200)

Mỗi bộ test sẽ có dạng như sau:

Dòng đầu tiên gồm số n - số lượng bánh ( 1≤ n ≤ 200)

Dòng thứ 2 gồm n số nguyên t1, t2,..., tn (1 ≤ ti ≤ n) là thời gian mà chiếc bánh thứ i cần nướng để đạt được độ ngon hoàn hảo.

Tổng của n ở tất cả các bộ test ≤ 200.

**Output:**

Với mỗi bộ test, in ra kết quả bài toán ứng với bộ test đó trên 1 dòng.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 2  6  4 2 4 4 5 2  7  7 7 7 7 7 7 7 | 4  12 |

Giải thích:

Ở test 1. Các chiếc bánh sẽ được lấy ra ở thời điểm như sau:

Phút 1: Lấy chiếc bánh thứ 2 (có ti = 2) ra. Độ tệ = abs(2 - 1) = 1

Phút 2: Lấy chiếc bánh thứ 6 (có ti = 2) ra. Độ tệ = abs(2-2) = 0

Phút 3: Lấy chiếc bánh thứ 1 (có ti = 4) ra. Độ tệ = abs(4 - 3) = 1

Phút 4: Lấy chiếc bánh thứ 4 (có ti = 4) ra. Độ tệ = abs(4 - 4) = 0

Phút 5: Lấy chiếc bánh thứ 3 (có ti = 4) ra. Độ tệ = abs(4-5) = 1

Phút 6: Lấy chiếc bánh thứ 5 (có ti = 5) ra. Độ tệ = abs(5 - 6) = 1

Như vậy, tổng độ tệ của n chiếc bánh = 4, và đây cũng là kết quả tốt nhất có thể có được (đương nhiên có nhiều hơn 1 cách lấy các chiếc bánh ra khỏi lò, thứ tự trên chỉ là 1 trong số đó).

### PYKT14020 - ĐỘI QUÂN HOÀNG GIA

Đội quân Hoàng Gia của đảo quốc PTIT đang chuẩn bị tiến hành duyệt binh mừng năm mới. Tất cả các người lính tham gia duyệt bình sẽ được xếp thành k hàng, mỗi hàng sẽ có số lượng các người lính bằng nhau. Tuy nhiên, nhà vua vì muốn đội hình diễu hành được đẹp nhất nên đã ra thêm 1 chỉ thị rằng, những người lính ở cùng 1 hàng không được cao hơn nhau quá 1 đơn vị. Là chỉ huy của quân đội, bạn có được báo cáo về số hàng nhà vua muốn xếp, dải chiều cao của quân lính cũng như số lượng người lính có chiều cao cùng chiều cao. Giờ đây bạn phải tính ra số lượng quân lính nhiều nhất có thể tham gia cuộc duyệt binh này.

**Input:**

Dòng đầu tiên là số bộ test t (1 ≤ t ≤ 1000)

Mỗi bộ test sẽ có dạng như sau:

Dòng đầu tiên gồm 2 số n và k (1 ≤ n ≤ 3\*104, 1 ≤ k ≤ 1012) lần lượt là số mức chiều cao khác nhau của quân lính, số hàng mà nhà vua muốn xếp.

Dòng thứ 2 gồm n số nguyên c1, c2, ..., cn (0 ≤ ci ≤ 1012) với ci tương ứng với số lượng người lính có chiều cao i.

**Output:**

1 số nguyên duy nhất là kết quả bài toán. Mỗi bộ test kết quả in trên 1 dòng.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 1  3 4  7 1 13 | 16 |

Giải thích:

Ở bộ test 1: Ta có 3 mức chiều cao (ta tạm đánh số từ 1 -&gt; 3)

Có 7 người lính cao 1 đơn vị, 2 người lính cao 2 đơn vị, 13 người lính cao 3 đơn vị.

Cần xếp thành 4 hàng.

Có 1 cách xếp đó là 4 hàng mỗi hàng có 4 quân lính như sau:

Hàng 1 : 3 3 3 3

Hàng 2: 1 2 1 1

Hàng 3 : 1 1 1 1

Hàng 4: 3 3 3 3

Vậy có thể có 16 người lính tham gia duyệt binh và đây cũng là số lượng nhiều nhất có thể.

(Chú ý, có thể có nhiều các xếp khác nhau cho ra được kết quả như vậy, đáp án ở giải thích chỉ là 1 trong số đó)

### PYKT14023 - GIÁ TRỊ NHỊ PHÂN

Cho một dãy nhị phân có N phần tử. Ban đầu cả dãy có giá trị toàn 0. Mỗi bước với hai giá trị x và y (1 ≤ x ≤ y ≤ N), bạn sẽ thay đổi tất cả các bit từ vị trí x đến vị trí y (nếu đang là 1 thì thành 0 và ngược lại).

Hãy cho biết sau Q lần thực hiện các truy vấn với 2 cặp số x, y thì trạng thái cuối cùng của dãy nhị phân là gì.

**Input**

- Dòng đầu ghi hai số N và Q
- Q dòng sau mỗi dòng ghi hai số x và y.
 
**Output**

Ghi ra dãy kết quả.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3 2  1 2  1 3 | 0 0 1 |

***Ràng buộc:***

*50% test tương ứng với 1 ≤ N, Q ≤ 1000*

*50% test tương ứng với 1 ≤ N, Q ≤ 100000*

### PYKT14031 - TRÒ CHƠI TRÍ TUỆ

Có N bạn sinh viên được chia thành 2 nhóm A và B và được xếp theo vòng tròn. Luật của trò chơi như sau:

- Giả sử người chơi đầu tiên là người thứ i. Thứ tự lượt chơi là i, i+1, …, N, 1, 2, …, i-1, … tiếp tục cho đến khi nào trò chơi kết thúc.
- Ban đầu khởi tạo số C = 0. Mỗi lượt, người chơi chọn một số có giá trị trong đoạn \[1, K\] để cộng vào giá trị C. Nếu người đội nào làm cho giá trị C lớn hơn hoặc bằng M, đội đó sẽ bị xử thua.
 
Biết rằng cả 2 đội đều có chiến thuật chơi tối ưu. Các bạn hãy xác định xem đội nào là đội chiến thắng với mỗi người chơi đầu tiên khác nhau.

**Input:**

Dòng đầu tiên chứa 3 số nguyên N, M và K (1 ≤ N, M, K ≤ 5000).

Dòng tiếp theo gồm N kí tự, mô tả hai đội chơi. 0 là đội A, 1 là đôi B.

**Output:**

In ra N kí tự. Kí tự thứ i cho biết đội chiến thắng nếu người chơi đầu tiên là người thứ i.

**Test ví dụ:**

 | Test 1 | Test 2 |
|---|---|
| Input:  2 9 2    0 1  Output:  0 1 | Input:  10 100 10  0 0 0 1 1 1 1 0 1 1  Output:  1 1 1 1 1 1 1 1 1 1 |

Giải thích test 1: Người đi trước luôn là người chiến thắng.

### PYKT14034 - DÃY BÍT NHỊ PHÂN

Cho một dãy bit nhị phân gồm có N bit: b\[0\] b\[1\] … b\[N-1\]. Bạn được phép thực hiện K lát cắt.

Có tổng cộng N+1 vị trí có thể cắt: | b\[0\] | b\[1\] | … | b\[N-1\] |.

Xét các dãy bit con kẹp giữa hai lát cắt, hai phần thừa bên ngoài bỏ không tính, như vậy với K lát cắt sẽ tạo ra được K-1 dãy con. Một cách cắt được gọi là đẹp nếu như tập hợp các số này biểu diễn dưới cơ số 10 tạo thành một tập hợp đầy đủ từ 1 à M với M nào đó.

Ví dụ với dãy bit 101101001110 và cách cắt 10 | 11 | 010 | 01 | 1 | 10 là đẹp, vì dãy con thu được là 11, 010, 01, 1 tương ứng với 3, 2, 1, 1 trong cơ số 10.

Kí hiệu f(K) là số cách cắt đẹp với K lát cắt.

Bạn hãy tính giá trị ![](./img/PYKT14034_0.png) theo modulo 109+7.

**Input:**

Dòng đầu tiên là số nguyên N (1 ≤ N ≤ 75).

Dòng tiếp theo gồm dãy bit b có N kí tự.

**Output:**

In ra một số nguyên là đáp án của bài toán.

**Ví dụ:**

 | Test 1 | Test 2 |
|---|---|
| Input:  4  1011  Output:  10 | Input:  2  10  Output:  1 |

Giải thích test 1:

K = 2: | 1 | 011 , 1 | 01 | 1, 10 | 1 | 1, 101 | 1 |.

K = 3: | 1 | 01 | 1, | 10 | 1 | 1, 10 | 1 | 1 |, 1 | 01 | 1 |.

K = 4: | 10 | 1 | 1 |, | 1 | 01 | 1 |.

### PYKT2041 - TAM GIÁC VUÔNG CÂN

Cho vùng tọa độ Oxy bị giới hạn bởi gốc tọa độ (0, 0) và điểm trên cùng bên phải (X, Y). Nhiệm vụ của bạn là hãy xác định xem có bao nhiêu tam giác vuông cân.

**Input:**

Dòng đầu tiên là số lượng bộ test T (T &lt;= 100).

Mỗi test gồm hai số nguyên X và Y.

**Giới hạn:**

Subtask 1 (25%) 0 &lt;= X, Y &lt;= 20.

Subtask 2 (25%) 0 &lt;= X, Y &lt;= 100.

Subtask 3 (50%) 0 &lt;= X, Y &lt;= 1000.

**Output:**

Với mỗi test, in ra số tam giác vuông tìm được trên một dòng.

**Example:**

 | Input | Output |
|---|---|
| 3  0 5  1 2  1 1 | 0  10  4 |

### PYKT2042 - GHÉP CẶP

Cho số nguyên dương N, đếm số cách chia các số từ 1 đến 2N thành N nhóm, mỗi nhóm gồm 2 số mà hiệu hai số trong một nhóm bằng hiệu hai số trong nhóm khác.

I**Input:**

Dòng đầu tiên chứa số lượng bộ test T.

Mỗi test gồm 1 số nguyên dương N.

**Giới hạn:**

Subtask 1 (50%): T, N &lt;= 10000

Subtask 2 (50%): T &lt;= 10^5, N &lt;= 10^6.

**Output:**

Với mỗi test, hãy in ra đáp án tìm được trên một dòng.

**Example:**

 | Input | Output |
|---|---|
| 2  1  2 | 1  2 |

Giải thích test 2: Có 2 cách chia nhóm là:

(1, 2) và (3, 4)

(1, 3) và (2, 4)

### PYKT2077 - SỐ ĐẶC BIỆT (BẢN KHÓ)

Một số được gọi là đặc biệt nếu như tổng các chữ số của nó là một số nguyên tố. Cho số tự nhiên N, hãy đếm số cặp (x, y) nguyên dương thỏa mãn x, y là số đặc biệt và x + 2y = N.

**Input:**

Dữ liệu đầu vào chứa một số nguyên dương N (1&lt;= N &lt;= 10^15).

**Output:**

In ra số cặp (x, y) thỏa mãn yêu cầu của đề bài.

**Test ví dụ:**

 | Input: | Output |
|---|---|
| 100 | 7 |

### PYKT2078 - K BIT 0

Cho số nguyên N. Nhiệm vụ của bạn là hãy xác định xem các số trong phạm vi từ 0 tới N có bao nhiêu số mà biểu diễn nhị phân của nó có đúng K chữ số 0.

Ví dụ N = 20, K = 3, ta có

8 = 1000

17 = 10001

18 = 10010

20 = 10100

**Input:**

Dòng đầu tiên là số lượng bộ test T (T &lt;= 20).

Mỗi test gồm hai số nguyên N và K (0&lt;= N &lt; 2^31, 1 &lt;= K &lt;= 31).

**Output:**

Với mỗi test, in ra số lượng các số thỏa mãn có K bit 0.

**Test ví dụ:**

 | Input: | Output |
|---|---|
| 2  20 3  8 1 | 4  4 |

### PYKT2080 - XÂU CON

Cho 2 số nguyên dương N, M và xâu s. Hãy đếm số lượng các xâu t có độ dài bằng N và xâu s là xâu con của t.

**Input:**

Dòng đầu tiên là số lượng bộ test (T ≤ 20).

Mỗi bộ test bắt đầu bởi 2 số N và M (N, M ≤ 10^12).

Dòng tiếp theo là xâu s có độ dài không quá 50 kí tự, chỉ gồm các chữ cái thường.

**Output:**

Với mỗi test, in ra đáp án tìm được theo modulo M.

**Ví dụ:**

 | Input: | Output |
|---|---|
| 3  2 1000  ab  3 1000  ab  3 1000  aa | 1  52  51 |

Giải thích test 2:

Các xâu có dạng \*ab hoặc ab\*, mỗi loại có 26 cách.

## BIẾN VÀ KIỂU DỮ LIỆU ĐƠN GIẢN

### PY00000 - WELCOME TO PYTHON

In ra màn hình dòng chữ:

Welcome to python.

### Input

Không có dữ liệu vào

### Output

Welcome to python.

### PY01000 - HELLO

Viết chương trình in ra lời chào

**Input:**

Một xâu ký tự họ tên độ dài không quá 50.

**Output:**

in ra màn hình dòng

Hello + tên vừa nhập + dấu chấm than

**Ví dụ:.**

 | **Input** | **output** |
|---|---|
| Nam | Hello Nam! |

### PY01001 - KIỂM TRA CHẴN LẺ

Cho một số nguyên dương N không quá 5 chữ số, hãy kiểm tra và in ra số đó chẵn hay lẻ. Nếu chẵn ghi ra chữ CHAN, nếu ngược lại ghi ra chữ LE.

**Input**

Chỉ có một dòng ghi số N

**Output**

Ghi ra kết quả trên một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2 | CHAN |
| 9999 | LE |

### PY01002 - PHÉP CỘNG

Cho một phép toán có dạng **a + b = c** với a,b,c chỉ là các số nguyên dương có một chữ số.

Hãy kiểm tra xem phép toán đó có đúng hay không.

**Input**

Chỉ có một dòng ghi ra phép toán (gồm đúng 9 ký tự)

**Ouput**

Ghi ra YES nếu phép toán đó đúng. Ghi ra NO nếu sai.

**Ví dụ**

 | **Test 1** | **Test 2** |
|---|---|
| Input  1 + 2 = 3  Output  YES | Input  2 + 2 = 5  Output  NO |

### PY01003 - LÀM TRÒN SỐ

Cho số nguyên dương không quá 9 chữ số. Hãy làm tròn số N theo quy tắc sau:

- Nếu N&gt;10, làm tròn đến số hàng chục gần nhất
- Sau đó nếu kết quả lớn hơn 100 thì làm tròn đến số hàng trăm gần nhất
- Sau đó nếu kết quả lớn hơn 1000 thì làm trong đến số hàng nghìn gần nhất
- Cứ tiếp tục như vậy …
 
Chú ý: Giá trị 5 sẽ được làm tròn lên.

**Input**

Dòng đầu ghi số bộ test (không quá 100)

Mỗi bộ test ghi số N trên một dòng (N nguyên dương và không quá 9 chữ số)

**Output**

Với mỗi test, ghi ra kết quả làm tròn tương ứng trên một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 7  15  14  5  99  12345678  44444445  1445 | 20  10  5  100  10000000  50000000  2000 |

### PY01004 - NGUYÊN TỐ

Trong toán học, một cặp số được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất của 2 số đó là 1. Cho số nguyên dương N, giả sử ta đếm được K số nguyên dương nhỏ hơn N có tính chất nguyên tố cùng nhau với N. Hãy kiểm tra xem K có phải là số nguyên tố hay không.

**Input**

Dòng đầu ghi số bộ test, không quá 10.

Dòng thứ 2 ghi số N (1 &lt; N &lt; 10000)

**Output**

Với mỗi test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  2  3 | NO  YES |

### PY01005 - SỐ MAY MẮN

Chữ số 4 và chữ số 7được xem là các chữ số may mắn.

Cho số nguyên dương N có không quá 18 chữ số. Hãy đếm xem số chữ số 4 cộng với số chữ số 7 trong N có phải bằng 4 hay bằng 7 hay không.

**Input**

Chỉ có số N

**Output**

Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 40047 | NO |
| 7747774 | YES |
| 1000000000000000000 | NO |

### PY01006 - SỐ MAY MẮN - 2

Một số được xem là số may mắn nếu chỉ có các chữ số 4 và 7. Cho số nguyên dương N không quá 200 chữ số. Hãy kiểm tra xem N có phải số may mắn hay không.

**Input**

Dòng đầu ghi số bộ test (không quá 10).

Mỗi test ghi số nguyên dương N không quá 200 chữ số.

**Output**

Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  4477  44444487777777777  47474747474777777777777744444 | YES  NO  YES |

### PY01007 - LÃI SUẤT NGÂN HÀNG

Ngân hàng thông báo lãi suất là X % mỗi năm.

Với số tiền gửi vào là N. Sau mỗi năm, tiền lãi sẽ được cộng dồn.

Hỏi sau bao nhiêu năm thì số tiền đạt được ít nhất là M.

**Input**

Dòng đầu ghi số bộ test.

Mỗi test viết 3 số thực (kiểu double) N, X và M. Trong đó 0&lt;N&lt;M&lt;100000.

**Output**

Ghi ra số năm tính được.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  200.00 6.5 300  500 4 1000.00 | 7  18 |

### PY01008 - CHUYỂN THÀNH CHỮ HOA

Viết chương trình nhập vào một xâu ký tự S có độ dài không quá 100 và chuyển xâu đã nhập thành chữ in hoa.

  
 **Input:**

Chỉ có một dòng ghi xâu S.

**Output:**

Ghi ra kết quả trên một dòng.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| mon thcs 2 | MON THCS 2 |

### PY01009 - CHỮ HOA – CHỮ THƯỜNG

Cho một xâu ký tự chỉ bao gồm các ký tự chữ cái, độ dài không quá 100. Hãy thực hiện:

- Biến đổi tất cả xâu thành viết thường, nếu số lượng chữ cái viết thường lớn hơn hoặc bằng số lượng chữ cái viết hoa.
- Biến đổi tất cả xâu thành chữ hoa, nếu số lượng chữ cái viết hoa lớn hơn số lượng chữ cái viết thường.
 
**Input**

Chỉ có một xâu ký tự độ dài không quá 100, không có khoảng trống

**Output**

Ghi ra xâu kết quả

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| vietHoa | viethoa |
| VIETTHuoNg | VIETTHUONG |

### PY01010 - ĐẦU CUỐI

Viết chương trình kiểm tra xem số nguyên dương N có thỏa mãn tính chất: nếu ta lấy hai chữ số đầu và hai chữ số cuối của nó thì sẽ tạo ra số có hai chữ số giống nhau hay không?

**Input**

Dòng đầu ghi số số test (không quá 20). Mỗi test là 1 số nguyên dương N có ít nhất 4 chữ số, nhưng không quá 18 chữ số.

**Output**

Ghi ra YES hoặc NO

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  12321  1234512  10233211111 | NO  YES  NO |

### PY01011 - LIỆT KÊ SỐ ĐẸP

Cho số nguyên dương N, hãy liệt kê các số thuận nghịch nhỏ hơn N thỏa mãn điều kiện:

- Chỉ có các chữ số 0,2,4,6,8
- Số chữ số của N chia cho 2 dư 1
 
**Input**

Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 &lt; N &lt;106)

**Output**

Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  30  100 | 22  22 44 66 88 |

### PY01012 - CHÈN XÂU

Cho xâu S1 và xâu S2, độ dài không quá 100.

Hãy chèn xâu S2 vào vị trí p trong xâu S1 (vị trí ký tự đầu tiên là vị trí 1).

**Input:**

Dòng thứ nhất ghi xâu S1

Dòng thứ hai ghi xâu S2

Dòng thứ ba ghi số p (giá trị p đảm bảo nằm trong phạm vi xâu S1)

**Output:**

Ghi ra kết quả.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| mon thcs2 hoc de  ngon ngu C.  1 | ngon ngu C.mon thcs2 hoc de |

### PY01013 - ƯỚC SỐ CHUNG NGUYÊN TỐ

Cho hai số nguyên dương a và b. Hãy kiểm tra xem ước số chung lớn nhất của hai số này có tổng chữ số là nguyên tố hay không.

Ví dụ a = 42, b = 28, ước số chung lớn nhất = 14. Tổng chữ số của ước số chung là 1+4=5 là một số nguyên tố.

**Input**

Dòng đầu ghi số bộ test. Mỗi test ghi trên một dòng hai số nguyên dương a,b (không quá 6 chữ số)

**Output**

Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  28 42  123 18  550 55 | YES  YES  NO |

### PY01014 - CHIA HẾT CHO K

Cho ba số nguyên dương a, K, N. Hãy liệt kê tất cả các số nguyên dương b thỏa mãn cả hai điều kiện:

- a + b ≤ N
- a + b chia hết cho K
 
**Input**

Chỉ có một dòng ghi ba số nguyên dương theo thứ tự a, K, N (không quá 9 chữ số).

**Output**

Ghi ra lần lượt các số b tìm được theo thứ tự tăng dần.

Nếu không tìm được số nào in ra -1

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 10 1 10 | -1 |
| 10 6 40 | 2 8 14 20 26 |

### PY01015 - SỐ KHÔNG GIẢM

Một số được gọi là số không giảm nếu không có cặp chữ số cạnh nhau (i, i+1) nào mà số thứ i lớn hơn số thứ i+1.

Viết chương trình kiểm tra số nguyên dương có thỏa mãn là số không giảm hay không.

**Input**

Dòng đầu ghi số bộ test (không quá 10).

Mỗi dòng ghi một số nguyên dương (không quá 500 chữ số).

**Output**

Ghi ra YES nếu đó là số không giảm. NO nếu ngược lại

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  12345678888888888888889  65645645465754765876857685846 | YES  NO |

### PY01016 - GIẢI MÃ

Cho một xâu ký tự độ dài không quá 100 chỉ bao gồm các chữ cái in hoa. Người ta thực hiện mã hóa bằng cách đếm các ký tự cạnh nhau giống nhau và viết số lượng phía sau các chữ cái đó.

Ví dụ xâu AAECCCCGGGD thì được mã hóa thành A2E1C4G3D1

Với giả thiết không có ký tự nào xuất hiện nhiều hơn 9 lần liên tiếp.

Cho trước xâu kết quả mã hóa. Hãy khôi phục xâu ký tự ban đầu tương ứng.

**Input**

Dòng đầu ghi số bộ test. Mỗi bộ test ghi xâu mã hóa.

**Output**

Với mỗi test ghi ra xâu ký tự ban đầu.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  A8  A2E1C4G3D1 | AAAAAAAA  AAECCCCGGGD |

### PY01017 - MÃ HÓA 1

Cho một xâu ký tự có thể có các ký tự chữ cái và chữ số. Người ta thực hiện một phép mã hóa đơn giản, trong đó đếm từ trái qua phải các ký tự giống nhau liên tiếp và viết số đếm trước ký tự đó.

Ví dụ: AACDDPQ được mã hóa thành 2A1C2D1P1Q

 11111147g được mã hóa thành 6114171g

Viết chương trình thực hiện thao tác mã hóa như trên.

**Input**

Dòng đầu ghi số bộ test. Mỗi dòng sau là một xâu ký tự, độ dài không quá 1000.

**Output**

Với mỗi bộ test, ghi ra xâu ký tự mã hóa tương ứng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  AACDDPQ  11111147g  1111111111 | 2A1C2D1P1Q  6114171g  101 |

### PY01018 - MÃ HÓA 2

Cho dãy ký tự chuẩn P\[\] gồm 28 chữ cái, trong đó có 26 chữ cái in hoa từ A đến Z, hai ký tự cuối là gạch dưới ‘\_’ và dấu chấm ‘.’

**P\[\] =** “ABCDEFGHIJKLMNOPQRSTUVWXYZ\_.”

Phép mã hóa với khoảng cách K (0&lt;K&lt;28) được định nghĩa là phép chuyển các ký tự s\[i\] thành ký tự P\[(i+K)%28\] trong dãy ký tự chuẩn P nói trên.

Ví dụ với K = 3 thì ‘A’ chuyển thành ‘D’; ‘B’ chuyển thành ‘E’ và ‘**.**’ chuyển thành ‘C’.

Cho số K và một xâu S (chỉ bao gồm các chữ cái thuộc P\[\], không có khoảng trống). Hãy mã hóa xâu S theo quy tắc trên, sau đó đảo ngược thứ tự các chữ cái.

**Input**

Mỗi dòng ghi số K và xâu S.

Input kết thúc khi K = 0.

**Output**

Ghi ra kết quả cho từng test.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 1 ABCD  14 ROAD  0 | EDCB  ROAD |

### PY01019 - KHOẢNG CÁCH KÝ TỰ

Nhập xâu s1, giả sử gọi xâu đảo là s2. Hãy kiểm tra xem khoảng cách ký tự cạnh nhau trong hai xâu có thỏa mãn công thức sau hay không:

**|**s1\[i\] – s1\[i-1\]**|** = **|**s2\[i\] – s2\[i-1\]**|** với tất cả giá trị 0 &lt; i &lt; N

**Input**

Dòng đầu ghi số bộ test. Mỗi bộ test là một xâu ký tự độ dài không quá 100000. Không có khoảng trống.

**Output**

Ghi ra YES hoặc NO.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  acxz  bcxz | YES  NO |

### PY01020 - SỐ PHÁT LỘC

Một số kết thúc bởi hai chữ số 86 được gọi là số phát lộc. Cho một số nguyên dương không quá 500 chữ số, hãy kiểm tra số đó có phải số phát lộc hay không.

**Input**

Dòng đầu ghi số bộ test. Mỗi bộ test ghi số nguyên dương cần kiểm tra (không quá 500 chữ số)

**Output**

Ghi ra kết quả kiểm tra tương ứng (YES hoặc NO)

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  1539786  1234789  8686 | YES  NO  YES |

### PY01021 - TÍNH TỔNG CÁC CHỮ SỐ

Cho xâu ký tự S bao gồm các ký tự ‘A’,..,’Z’ và các chữ số ‘0’,...,’9’. Nhiệm vụ của bạn in các ký tự từ ’A’,.., ‘Z’ trong S theo thứ tự từ điển và nối với tổng các chữ số trong S ở cuối cùng. Ví dụ S =”ACCBA10D2EW30” ta nhận được kết quả: “AABCCDEW6”.

**Input:**

- Dòng đầu tiên đưa vào số lượng bộ test T.
- Những dòng kế tiếp đưa vào T bộ test. Mỗi bộ test là một xâu ký tự S.
- T, S thỏa mãn ràng buộc: 1≤ T ≤100; 1≤ Length(S)≤105.
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
 **Ví dụ:**

 | Input: | Output: |
|---|---|
| 2    AC2BEW3    ACCBA10D2EW30 | ABCEW5    AABCCDEW6 |

### PY01022 - TỔNG CHỮ SỐ

Cho một số nguyên **(có thể âm)** không quá 100.000 chữ số. Mỗi bước thực hiện thay thế số nguyên này bằng giá trị tổng chữ số của số đó. Hỏi sau mấy bước thì số đó chỉ còn duy nhất 1 chữ số.

**Input**

Chỉ có duy nhất số nguyên N (không quá 100.000 chữ số)

**Output**

Ghi ra số bước cần thực hiện.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 10 | 1 |
| 919 | 3 |
| 6 | 1 |

### PY01023 - PHÂN TÍCH THỪA SỐ NGUYÊN TỐ

Cho số nguyên dương N. Hãy phân tích N thành tích các thừa số nguyên tố. Kết quả được in ra theo mẫu trong ví dụ, trong đó thêm số thừa số 1 (không phải nguyên tố) ở đầu kết quả phân tích.

**Input**

Dòng đầu ghi số bộ test, mỗi test ghi trên một dòng số nguyên dương N không quá 6 chữ số.

**Output**

Ghi ra kết quả phân tích theo mẫu như trong ví dụ.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  28  100  1234 | 1 \* 2^2 \* 7^1  1 \* 2^2 \* 5^2  1 \* 2^1 \* 617^1 |

### PY01024 - CHẴN - LẺ

Cho số nguyên dương N. Hãy kiểm tra xem N có thỏa mãn đồng thời hai tính chất sau đây hay không?

- Tổng chữ số của N chia hết cho 10
- Các chữ số cạnh nhau đều khác nhau đúng 2 đơn vị
 
**Input**

Dòng đầu ghi số bộ test. Mỗi bộ test ghi trên một dòng số nguyên dương N. N có ít nhất 3 chữ số nhưng không quá 18 chữ số.

**Output**

Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  1353  246864  123435 | NO  YES  NO |

### PY01025 - CHÈN DẤU PHẨY

Khi viết giá trị số nguyên trong Tiếng Anh, người ta thường thêm dấu phẩy để phân tách các nhóm 3 chữ số (tính từ cuối). Ví dụ số 153920529 được viết lại thành 153,920,529.

Cho số nguyên dương N trong phạm vi số int (không quá 2 tỷ). Hãy chèn dấu phẩy vào N theo quy tắc trên.

**Input**

Chỉ có 1 số N

**Output**

Kết quả sau khi đã chèn dầu phẩy

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 153920529 | 153,920,529 |

### PY01026 - SẮP ĐẶT LẠI XÂU KÝ TỰ

Cho hai xâu ký tự s1 và s2. Xâu s2 được gọi là một “sắp đặt lại” của xâu s1 nếu tập ký tự của xâu s2 hoàn toàn giống với xâu ký tự s1, tính cả số lần xuất hiện của từng ký tự.

Ví dụ: s2 = “intestg” là sắp đặt lại của xâu “testing”

Còn xâu “aabbbcccc” không được coi là sắp đặt lại của xâu “abc”.

Nhập 2 xâu s1 và s2 có độ dài không quá 1000 ký tự, chỉ bao gồm các ký tự viết thường, không có khoảng trống. Hãy kiểm tra xem s2 có phải là sắp đặt lại của s1 hay không.

**Input**

Dòng đầu ghi số bộ test, không quá 5000.

Mỗi test ghi trên 2 dòng lần lượt là xâu s1 và s2.

**Output**

Ghi ra thứ tự bộ test, sau đó là YES hoặc NO tùy thuộc kết quả kiểm tra.

Xem ví dụ để hiểu rõ hơn.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 4  testing  intestg  abc  aabbbcccc  abcabcbcc  aabbbcccc  abc  xyz | Test 1: YES  Test 2: NO  Test 3: YES  Test 4: NO |

### PY01027 - SỐ LỘC PHÁT ĐẸP

Ai cũng biết số lộc phát theo quan niệm người Việt là số chỉ chứa các chữ số 6 và/hoặc 8. Người ta định nghĩa thêm “số lộc phát đẹp” là số thỏa mãn tính chất nếu xét từ trái qua phải thì nó được ghép bởi 3 số: 6; 68; 688. Không nhất thiết phải dùng đủ cả 3 số này.

Ví dụ: các số 666666; 668688; 688688688 là các số lộc phát đẹp.

Cho trước một số nguyên dương N không quá 100 chữ số. Hãy kiểm tra xem đó có phải là số lộc phát đẹp hay không.

**Input**

Chỉ có một dòng ghi số N có không quá 100 chữ số

**Output**

Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 666666 | YES |
| 668688 | YES |
| 886236 | NO |

### PY01028 - TÁCH TỪ

Nhập xâu ký tự S có độ dài không quá 100. Một từ được định nghĩa là một dãy ký tự không có khoảng trống.

Hãy tách xâu S thành các từ, mỗi từ in trên một dòng.

**Input:**

Chỉ có một dòng ghi xâu S (độ dài không quá 100)

**Output:**

Ghi ra kết quả.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| Tin hoc co so 2 | Tin  hoc  co  so  2 |

### PY01029 - SỐ ĐẢO NGUYÊN TỐ CÙNG NHAU

Trong toán học, cặp số (a,b) được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất của a và b bằng 1.

Cho số nguyên dương N không quá 9 chữ số. Hãy kiểm tra xem N và số đảo của N có phải là một cặp số nguyên tố cùng nhau hay không.

**Input**

Dòng đầu ghi số bộ test, không quá 20.

Mỗi bộ test ghi trên một dòng số nguyên dương N, không quá 9 chữ số.

**Output**

Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  123  997 | NO  YES |

### PY01030 - NGUYÊN TỐ CÙNG NHAU

Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau nếu a và b có ước chung lớn nhất bằng 1.

Cho hai số nguyên dương N và K trong đó 10 &lt; N &lt; 10000; 1 &lt; K &lt; 6.

Hãy liệt kê các số có K chữ số thỏa mãn nguyên tố cùng nhau với N.

**Input**

Chỉ có một dòng ghi hai số N và K

**Output**

Ghi ra lần lượt các số thỏa mãn theo thứ tự từ nhỏ đến lớn. Mỗi dòng ghi 10 số.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 123 2 | 10 11 13 14 16 17 19 20 22 23  25 26 28 29 31 32 34 35 37 38  40 43 44 46 47 49 50 52 53 55  56 58 59 61 62 64 65 67 68 70  71 73 74 76 77 79 80 83 85 86  88 89 91 92 94 95 97 98 |

### PY01031 - ĐỔI CƠ SỐ

Cơ số từ 2 đến 36 được xây dựng từ 10 chữ số (0 đến 9) và 26 chữ cái Tiếng Anh in hoa (‘A’ đến ‘Z’).

Hãy viết chương trình chuyển một số nguyên dương N trong cơ số 10 sang cơ số b. Trong đó N không quá 100.000, 2 ≤ b ≤ 36.

**Input**

Dòng đầu ghi số bộ test, không quá 10.

Mỗi bộ test ghi 2 số N và b.

Nlà một số nguyên dương N trong cơ số 10, không quá 100.000. 2 ≤ b ≤ 36

**Output**

Với mỗi bộ test ghi ra kết quả đổi cơ số tương ứng.

**Ví dụ**

 | **Input** | **Ouput** |
|---|---|
| 3  10 2  2021 2  31 16 | 1010  11111100101  1F |

### PY01032 - SỐ THUẬN NGHỊCH

Trong hệ cơ số thập phân, một số được gọi là thuận nghịch nếu đọc ngược lại ta vẫn thu được chính số đó. Ví dụ: 12321, 2345432, 111111 …

Chúng ta mở rộng khái niệm như sau: cho hệ cơ số K, giá trị thập phân x được gọi là thuận nghịch trong cơ số K nếu biểu diễn của x trong cơ số K có giá trị giống nhau khi viết xuôi và khi viết ngược. Với giả thiết biểu diễn trong hệ cơ số K bất kỳ (2 ≤ K ≤ 100000) là cách sử dụng chính các giá trị số từ 0 đến K-1 chứ không dùng các chữ cái.

Bài toán đặt ra là cho đoạn \[a,b\] và số M. Hãy đếm các số trong đoạn \[a,b\] là thuận nghịch trong tất cả các cơ số 2 ≤ K ≤ M.

**Input:**

Chỉ có một dòng ghi 3 số a,b,M. 0 ≤ a ≤ b ≤ 2 000 000; 2 ≤ M ≤ 100 000.

**Output:**

Ghi ra số lượng các số thỏa mãn.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 1 356 2 | 36 |
| 18 118 13 | 0 |

### PY01033 - BỘ BA NGUYÊN TỐ CÙNG NHAU

Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau nếu a và b có ước chung lớn nhất bằng 1. Một bộ ba số (a, b, c) được gọi là bộ ba nguyên tố cùng nhau nếu a &lt; b &lt; c và các cặp (a,b), (b,c), (a,c) đều nguyên tố cùng nhau.

Cho hai số nguyên dương L và R (10 &lt; L &lt; R &lt; 200). Hãy viết chương trình liệt kê các bộ ba số nguyên tố cùng nhau trong đoạn \[L, R\].

**Input**

Chỉ có 2 số L và R

**Output**

Ghi ra các bộ ba số nguyên tố cùng nhau, mỗi bộ ba trên một dòng theo định dạng như trong ví dụ.

Các bộ ba được liệt kê theo thứ tự từ điển tăng dần.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 15 20 | (15, 16, 17)  (15, 16, 19)  (15, 17, 19)  (16, 17, 19)  (17, 18, 19)  (17, 19, 20) |

### PY01034 - ĐỔI CHỖ CÁC CHỮ SỐ

Cho một số nguyên không âm N được biểu diễn như một xâu ký tự. Hãy sử dụng nhiều nhất một phép đổi chỗ các chữ số trong N sao cho ta nhận được số lớn nhất nhỏ hơn N. Phép biến đổi có số 0 cho số đầu tiên sẽ không được chấp nhận. Ví dụ số N=354 thì số lớn nhất nhỏ hơn N được tạo ra là 345. Số 100 sẽ không có phép biến đổi vì số 010 có số 0 đứng đầu.

**Input:**

Dòng đầu tiên đưa vào số lượng test T (T≤100).

Những dòng kế tiếp đưa vào các test. Mỗi bộ test là một xâu ký tự bao gồm các ký tự số. Độ dài tối đa là 1000.

**Output:**

Với mỗi test in ra số nguyên lớn nhất tìm được trên một dòng. Nếu không tồn tại đáp án, in ra -1.

**Ví dụ:**

 | **Input:** | **Output:** |
|---|---|
| 4  354  999  100  11101 | 345  -1  -1  11011 |

### PY01035 - HỆ CƠ SỐ 8

Cho một số nhị phân, người ta nhận ra quy tắc đơn giản là chỉ cần xét lần lượt các cụm ba chữ số nhị phân tình từ cuối của số đó, sau đó chuyển lần lượt từng cụm sang giá trị thập phân tương ứng thì kết quả nhận được chính là biểu diễn của số đó trong hệ cơ số 8. Nếu cụm cuối cùng bị thiếu thì bổ sung các chữ số 0 cho đủ 3 chữ số.

Ví dụ:

11001100 =&gt; 011 | 001 | 100 =&gt; 314

Hãy áp dụng tính chất trên để chuyển đổi một số nhị phân (không quá 100 chữ số và luôn bắt đầu bởi chữ số 1) sang hệ cơ số 8.

**Input**

Chỉ có một số nhị phân, không quá 100 chữ số

**Output**

Ghi ra kết quả trong hệ cơ số 8

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 1010 | 12 |
| 11001100 | 314 |

### PY01036 - TÍNH TỔNG PHÂN THỨC

Nhập số nguyên dương N (1 &lt; N &lt; 10000).

Viết chương trình tính tổng:

- S = 1 + 1/3 + 1/5 + … + 1/N nếu N lẻ
- S = 1/2 + 1/4 + 1/6 + … + 1/N nếu N chẵn
 
Kết quả được in ra với 6 chữ số phần thập phân.

**Input**

Dòng đầu ghi số bộ test, không quá 10.

Mỗi test ghi một số N

**Output**

Với mỗi bộ test, ghi ra kết quả trên một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  10  15 | 1.141667  2.021800 |

### PY01037 - SỐ PHẢN NGUYÊN TỐ NHỎ NHẤT

Số nguyên dương N được gọi là phản nguyên tố nếu như số lượng ước số của N lớn hơn số lượng ước số của tất cả các số nguyên dương nhỏ hơn N.

Ví dụ các số phản nguyên tố đầu tiên: 1, 2, 4, 6, 12, 24, …

Cho số nguyên dương X, hãy tìm số phản nguyên tố bé nhất không nhỏ hơn X.

**Input:**

Dòng đầu ghi số bộ test T (không quá 106)

Mỗi test ghi số nguyên dương X (1 ≤ X ≤ 107)

**Output:**

Với mỗi test, ghi ra kết quả tính được trên một dòng.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 1  5 | 6 |

### PY01038 - KIỂM TRA CHIA HẾT CHO 7

Cho một số nguyên dương N. Mỗi bước bạn thực hiện tính tổng của N với giá trị số đảo ngược của N. Bạn sẽ dừng lại khi gặp giá trị chia hết cho 7 hoặc khi đã thực hiện quá 1000 bước lặp.

Hãy tính giá trị chia hết cho 7 tìm được theo thủ tục trên hoặc ghi ra -1 nếu không thể tìm ra đáp án.

**Input:**

Dòng đầu ghi số bộ test (không quá 1000).

Mỗi test ghi số N (1 ≤ N ≤ 1018)

**Output:**

Ghi ra giá trị chia hết cho 7 đầu tiên tìm được. Hoặc số -1 nếu không thể tìm được đáp án.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 5  1  2  3  4  999999 | 77  77  9447438  77  999999 |

Giải thích test 1: 1 à 2 à 4 à 8 à 16 à 77

### PY01039 - KIỂM TRA SỐ ĐẸP

Một số nguyên dương được gọi là đẹp nếu số đó chỉ có hai chữ số khác nhau và các chữ số ở cách nhau 2 vị trí đều bằng nhau. Ví dụ: 121, 1313131, 5656 …

Viết chương trình kiểm tra một số có phải số đẹp hay không?

**Input**

Dòng đầu ghi số bộ test. Mỗi bộ test ghi một số nguyên dương N (lớn hơn 10 và có không quá 18 chữ số) trên một dòng.

**Output**

Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  12121212  343433  78789989 | YES  NO  NO |

### PY01040 - MÃ HÓA 3

Cho một xâu ký tự. Quá trình mã hóa D - R - M sẽ trải qua ba bước Chia (Divide), Xoay (Rotate) và Trộn (Merge). Ví dụ với xâu: EWPGAJRB quá trình này sẽ diễn ra như sau:

- **Devide:** Xâu ban đầu được chia thành 2 nửa: “EWPG” và “AJRB”.
- **Rotate:** Với mỗi nửa, tính toán giá trị xoay của nó bằng cách tính tổng giá trị các ký tự. (A = 0; B = 1; … Z = 25). Giá trị xoay của “EWPG” là 4 + 22 + 15 + 6 = 47. Tiến hành xoay xâu “EWPG” đi 47 ký tự (tính cả bước chuyển từ Z về A nếu cần) ta sẽ được xâu: “ZRKB”. Tương tự, “AJRB” được chuyển thành “BKSC”
- **Merge:** Trong bước này, mỗi ký tự trong xâu thứ nhất sẽ được xoay theo giá trị của ký tự ở vị trí tương ứng trong xâu thứ 2. Trong ví dụ trên, chữ Z trong xâu thứ nhất sẽ xoay theo giá trị B, tức là 1 vị trí. Do đó sẽ chuyển thành chữ A. Tiếp tục thực hiện với các ký tự tiếp theo ta sẽ có kết quả là “ABCD”.
 
Cho một xâu ký tự chỉ bao gồm các chữ cái in hoa với số lượng ký tự là chẵn, bạn hãy tìm xâu mã hóa DRM tương ứng.

**Input**

Dòng đầu ghi số bộ test T (T≤30).

Mỗi bộ test ghi trên một dòng xâu ký tự cần mã hóa, chỉ gồm các chữ cái in hoa, độ dài là chẵn và không quá 15000 ký tự.

**Output**

Với mỗi test in ra trên một dòng kết quả mã hóa DRM tương ứng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  EWPGAJRB  BB  TPQJDRJWSQXGRRIPXFMINTELHBJA | ABCD  E  FIRSTDATAFILEV |

### PY01041 - SỐ TĂNG GIẢM

Một số nguyên dương được gọi là số tăng giảm nếu thỏa mãn các điều kiện:

- Có từ 3 chữ số trở lên
- Tìm ra một vị trí trong dãy chữ số sao cho từ bên trái đến vị trí đó thỏa mãn thứ tự tăng dần (tăng chặt) còn từ vị trí đó đến hết thì thỏa mãn thứ tự giảm dần (giảm chặt).
 
Viết chương trình kiểm tra một số có phải số tăng giảm hay không.

**Input**

Dòng đầu ghi số bộ test. Mỗi bộ test viết trên một dòng số nguyên dương N không quá 18 chữ số

**Output**

Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Ouput** |
|---|---|
| 3  12342  23342  5678961 | YES  NO  YES |

### PY01042 - KIỂM TRA HỆ CƠ SỐ 3

Hệ cơ số 3 chỉ biểu diễn các số sử dụng ba chữ số là 0, 1, 2.

Nhập vào dãy biểu diễn không quá 18 ký tự, hãy kiểm tra xem dãy biểu diễn nào là đúng với hệ cơ số 3.

**Input**

Dòng đầu là số bộ test, mỗi dòng tiếp theo ghi một dãy biểu diễn cần kiểm tra.

**Output**

Nếu đúng in ra YES, nếu sai in ra NO.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  1214AB  10210221  22222222 | NO  YES  YES |

### PY01043 - SỐ THUẬN NGHỊCH CHẴN

Cho số nguyên dương N không quá 6 chữ số.

Hãy liệt kê các số nhỏ hơn N thỏa mãn cả ba điều kiện:

- N là số thuận nghịch
- Tất cả các chữ số của N đều chẵn
- Số chữ số của N cũng là một số chẵn
 
**Input**

Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 &lt; N &lt;106)

**Output**

Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  30  100 | 22  22 44 66 88 |

### PY01044 - XỬ LÝ XÂU KÝ TỰ

Trong lập trình cơ bản, một từ được hiểu là một dãy ký tự liên tiếp không chứa khoảng trống, dấu tab hoặc dấu xuống dòng.

Viết chương trình nhập hai dòng ký tự và hiển thị hợp và giao của hai tập từ tương ứng. Các từ trong tập từ không được phép trùng nhau, mỗi từ chỉ liệt kê một lần và theo đúng thứ tự từ điển. Các từ đều được chuyển hết về chữ viết thường.

**Input**

Chỉ có 2 dòng, mỗi dòng có độ dài không quá 1000 ký tự.

**Output**

Dòng 1 ghi hợp của 2 tập từ theo thứ tự từ điển

Dòng 2 ghi giao của 2 tập từ theo thứ tự từ điển.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| Lap trinh huong doi tuong  Ngon ngu lap trinh C++ | c++ doi huong lap ngon ngu trinh tuong  lap trinh |

### PY01045 - XÂU PALINDROME

Một xâu ký tự là xâu palindrome là một xâu khác rỗng mà nếu lật ngược xâu ấy ta thu được xâu ban đầu. Ví dụ các xâu *abcba*, *dd* là xâu palindrome, trong khi các xâu *abc*, *ptit* thì không phải.

Cho một xâu ký tự A. Tìm cách xoá đi nhiều nhất các kí tự của A để thu được một xâu palindrome.

**Input**

Một dòng duy nhất gồm một xâu kí tự S không quá 10000 ký tự, chỉ có các chữ cái in thường.

**Output:** Số kí tự lớn nhất có thể bỏ đi được để S là xâu palindrome.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| abccba | 5 |

### PY01046 - THÁP HÀ NỘI

Bài toán Tháp Hà Nội đã rất nổi tiểng. Bắt đầu có các đĩa xếp chồng lên cột A theo thứ tự kích thước giảm dần, nhỏ nhất ở trên cùng. Cột B và cột C ban đầu không có đĩa nào cả.

![](./img/PY01046_0.png)

Mục tiêu của bạn là di chuyển toàn bộ các đĩa theo đúng thứ tự về cột C, tuân theo các quy tắc sau:

1. Mỗi lần chỉ có thể di chuyển một đĩa.
2. Mỗi lần di chuyển sẽ lấy đĩa trên từ một trong các cột và đặt nó lên trên một cột khác.
3. Không được đặt đĩa lên trên đĩa nhỏ hơn..
 
**Input:**

Số tự nhiên 0 &lt; N &lt; 10

**Output:**

In ra lần lượt từng bước theo mẫu trong ví dụ. Chú ý giữa các chữ cái và dấu -&gt; có khoảng trống.

**Ví dụ:**

 | **Input** | **Ouput** |
|---|---|
| 3 | A -&gt; C  A -&gt; B  C -&gt; B  A -&gt; C  B -&gt; A  B -&gt; C  A -&gt; C |

### PY01047 - KIỂM TRA NGUYÊN TỐ

Cho số nguyên dương N có không quá 500 chữ số.

Hãy kiểm tra xem 4 chữ số cuối cùng ghép lại có tạo thành một số nguyên tố hay không.

Chú ý: các chữ số 0 ở đầu trong 4 chữ số cuối vẫn được chấp nhận

**Input**

Dòng đầu ghi số bộ test (không quá 20).

Mỗi test viết trên một dòng số nguyên dương N, không quá 500 chữ số.

**Output**

Với mỗi bộ test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  12234323130097  3443354654654654461123  43543543434554659999 | YES  YES  NO |

### PY01049 - CHỮ SỐ NGUYÊN TỐ

Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:

- Số chữ số của nó là một số nguyên tố
- Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
 
Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.

**Input**

- Dòng đầu ghi số bộ test, không quá 20.
- Mỗi bộ test ghi số nguyên dương N, ít nhất 3 chữ số nhưng không quá 500 chữ số
 
**Output**

Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  1234567  22334455667  23400300489898989 | YES  YES  NO |

### PY01050 - KÝ TỰ A – B – C

Hãy liệt kê tất cả các xâu ký tự có độ dài không quá N, chỉ tạo bởi các ký tự A, B, C và thỏa mãn các điều kiện sau:

- Chứa cả ba ký tự A, B, C
- Số ký tự A không nhiều hơn số ký tự B, số ký tự B không nhiều hơn số ký tự C
 
**Input**

Chỉ có một dòng ghi số N, không quá 12.

**Output**

Ghi ra lần lượt các xâu thỏa mãn theo thứ tự độ dài từ ngắn nhất đến dài nhất.

Nếu có cùng độ dài thì ghi theo thứ tự từ điển.

Mỗi xâu ghi trên một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 4 | ABC  ACB  BAC  BCA  CAB  CBA  ABCC  ACBC  ACCB  BACC  BCAC  BCCA  CABC  CACB  CBAC  CBCA  CCAB  CCBA |

### PY01051 - TỔNG CHỮ SỐ THUẬN NGHỊCH

Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.

Hãy kiểm tra xem tổng các chữ số của N có phải là một số thuận nghịch hay không.

*Một số chỉ được coi là thuận nghịch nếu nhiều hơn 1 chữ số và số đảo của nó đúng bằng nó.*

**Input**

Dòng đầu ghi số bộ test (không quá 20).

Mỗi test ghi số N (không quá 500 chữ số)

**Output**

Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  12341  22222222222222222222 | YES  NO |

### PY01052 - TỔNG CHỮ SỐ NGUYÊN TỐ

Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.

Hãy kiểm tra xem tổng các chữ số của N có phải là một số nguyên tố hay không.

**Input**

Dòng đầu ghi số bộ test (không quá 20).

Mỗi test ghi số N (không quá 500 chữ số)

**Output**

Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  12341  22222222222222222222 | YES  NO |

### PY01053 - SỐ CHIA HẾT CHO 3

Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.

Hãy kiểm tra xem N có chia hết cho 3 hay không.

**Input**

Dòng đầu ghi số bộ test (không quá 20).

Mỗi test ghi số N (không quá 500 chữ số)

**Output**

Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  12341  123456789123456789 | NO  YES |

### PY01054 - TÍCH CHỮ SỐ

Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.

Hãy tính tích các chữ số của N. Chú ý bỏ qua các chữ số 0 nếu có.

**Input**

Dòng đầu ghi số bộ test (không quá 20).

Mỗi test ghi số N (không quá 500 chữ số).

**Output**

Với mỗi bộ test, ghi ra kết quả tính được.

Dữ liệu vào đảm bảo kết quả tích các chữ số sẽ không vượt quá 18 chữ số.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  123410  123456789123456789 | 24  131681894400 |

### PY01055 - SỐ XEN KẼ

Một số được gọi là xen kẽ nếu thỏa mãn cả ba tính chất sau:

- Số chữ số là số lẻ
- Chữ số đầu tiên khác chữ số thứ hai.
- Các số ở vị trí đầu tiên, vị trí thứ 3, vị trí thứ 5… và vị trí cuối cùng có giá trị bằng nhau
 
Viết chương trình kiểm tra một số có phải xen kẽ hay không.

**Input**

Dòng đầu ghi số bộ test (không quá 10).

Mỗi bộ test viết trên một dòng số cần kiểm tra, không quá 500 chữ số.

**Output**

Với mỗi bộ test viết ra YES hoặc NO tùy thuộc kết quả kiểm tra

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  2324272921262  13141516 | YES  NO |

### PY01056 - CHẴN – LẺ - NGUYÊN TỐ

Cho một số nguyên dương không quá 500 chữ số.

Hãy kiểm tra xem số đó có thỏa mãn đồng thời ba tính chất sau hay không?

- Vị trí chẵn là chữ số chẵn
- Vị trí lẻ là chữ số lẻ
- Tổng chữ số là một số nguyên tố.
 
**Input**

Dòng đầu ghi số bộ test (không quá 10)

Mỗi bộ test ghi trên một dòng giá trị số nguyên (không quá 500 chữ số)

**Output**

Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  2345678521  1212121212121212121212121 | YES  NO |

### PY01057 - VỊ TRÍ NGUYÊN TỐ

Trong 10 chữ số thập phân thì có 4 chữ số nguyên tố là 2, 3, 5, 7.

Một số nguyên dương được coi là thỏa mãn nguyên tố đúng vị trí nếu thỏa mãn cả hai điều kiện:

- Nếu i là nguyên tố thì vị trí thứ i cũng phải là chữ số nguyên tố.
- Ngược lại nếu i không phải là số nguyên tố thì vị trí thứ i không phải là chữ số nguyên tố.
 
Ví dụ: số **14239567** thỏa mãn nguyên tố đúng vị trí vì các vị trí thứ 2, 3, 5, 7 là các chữ số nguyên tố, các vị trí khác không nguyên tố.

Viết chương trình kiểm tra một số nguyên dương không quá 500 chữ số có thỏa mãn tính chất trên hay không.

**Input**

Dòng đầu ghi số bộ test, không quá 10.

Mỗi bộ test viết trên một dòng số nguyên dương không quá 500 chữ số.

**Output**

Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  14239567  2314514535353 | YES  NO |

### PY01058 - ĐOẠN CUỐI NGUYÊN TỐ

Cho số nguyên dương N có không quá 500 chữ số.

Hãy kiểm tra xem 4 chữ số cuối cùng ghép lại có tạo thành một số nguyên tố hay không.

Chú ý: các chữ số 0 ở đầu trong 4 chữ số cuối vẫn được chấp nhận

**Input**

Dòng đầu ghi số bộ test (không quá 20).

Mỗi test viết trên một dòng số nguyên dương N, không quá 500 chữ số.

**Output**

Với mỗi bộ test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  12234323130097  3443354654654654461123  43543543434554659999 | YES  YES  NO |

### PY01059 - TỔNG CHỮ SỐ - TÍCH CHỮ SỐ

Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số. Xét các vị trí từ trái qua phải (tính từ 0). Hãy tính:

- Tổng các chữ số ở vị trí chẵn
- Tích các chữ số ở vị trí lẻ. – giá trị tích chữ số có thể đến 18 chữ số. Chú ý khi tính tích bỏ qua các chữ số 0, nhưng nếu tất cả các vị trí lẻ đều là giá trị 0 thì tích = 0.
 
**Input**

- Dòng đầu ghi số bộ test (không quá 20)
- Mỗi bộ test ghi trên một dòng số nguyên dương N (ít nhất 2 chữ số và không quá 500 chữ số)
 
**Output**

Với mỗi bộ test, viết trên một dòng hai giá trị: tổng chữ số và tích chữ số tính được.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  12345678  20000  22334455667788 | 16 384  2 0  35 40320 |

### PY01060 - TÍCH CHỮ SỐ - TỔNG CHỮ SỐ

Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số. Xét các vị trí từ trái qua phải (tính từ 0). Hãy tính:

- Tích các chữ số ở vị trí chẵn – giá trị tích chữ số có thể đến 18 chữ số. Chú ý khi tính tích bỏ qua các chữ số 0.
- Tổng các chữ số ở vị trí lẻ
 
**Input**

- Dòng đầu ghi số bộ test (không quá 20)
- Mỗi bộ test ghi trên một dòng số nguyên dương N (ít nhất 2 chữ số và không quá 500 chữ số)
 
**Output**

Với mỗi bộ test, viết trên một dòng hai giá trị: tích chữ số và tổng chữ số tính được.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  12345678  20000  22334455667788 | 105 20  2 0  40320 35 |

### PY01061 - ĐẦU CUỐI NGUYÊN TỐ

Cho số nguyên dương N có ít nhất 4 chữ số và không quá 500 chữ số.

Một số được gọi là số đầu cuối nguyên tố nếu thỏa mãn cả hai điều kiện:

- Ba chữ số đầu ghép lại được một số nguyên tố
- Ba chữ số cuối ghép lại được một số nguyên tố
 
Viết chương trình kiểm tra xem N có phải là đầu cuối nguyên tố hay không?

**Input**

Dòng đầu ghi số bộ test (không quá 20).

Mỗi bộ test viết trên một dòng số N, ít nhất 4 chữ số và không quá 500 chữ số.

**Output**

Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  12743  7337  12345678901234 | YES  YES  NO |

### PY01062 - ƯU THẾ NGUYÊN TỐ

Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:

- Số chữ số của nó là một số nguyên tố
- Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
 
Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.

**Input**

- Dòng đầu ghi số bộ test, không quá 20.
- Mỗi bộ test ghi số nguyên dương N, ít nhất 3 chữ số nhưng không quá 500 chữ số
 
**Output**

Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  1234567  22334455667  23400300489898989 | YES  YES  NO |

### PY01063 - ĐẾM SỐ TRONG XÂU

Cho một ký tự S\[\] chỉ có các chữ số, độ dài không quá 1000, và số nguyên dương N (không quá 9 chữ số). Hãy đếm xem số N xuất hiện bao nhiêu lần trong S\[\].

Chú ý: các ký tự số không được đếm lặp. Tức là mỗi ký tự chỉ được xét một lần.

Ví dụ: S\[\] = “**121**2**121**112211221**121**”, N = **121** thì đáp án là 3.

**Input**

Dòng đầu ghi số bộ test, không quá 20.

Mỗi test gồm hai dòng, dòng đầu là xâu ký tự S\[\], dòng sau là số N.

**Output**

Với mỗi bộ test, ghi ra kết quả tính được trên một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  1212121112211221121  121  2222222222322292  2222 | 3  2 |

### PY01064 - KÝ TỰ THỨ K

Xâu ký tự S được tạo ra bằng cách bổ sung dần các ký tự chữ cái Tiếng Anh in hoa như sau.

- Bước 1: Chỉ có chữ cái A
- Bước 2: Thêm chữ cái B vào giữa 2 chữ A =&gt; S = "ABA"
- Bước 3: Thêm chữ cái C vào giữa 2 xâu đã có ở bước 2: S = "ABACABA"
 
Cứ như vậy cho đến bước thứ N (0 &lt; N &lt; 26)

Hãy xác định ký tự thứ K trong bước biến đổi thứ N là chữ cái gì?

**Input:**

- Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
- Mỗi test gồm số nguyên dương N và K (1 ≤ N ≤ 25, 1 ≤ K ≤ 2N - 1).
 
**Output:**

- Với mỗi test, in ra đáp án trên một dòng.
 
**Ví dụ:**

 | **Input:** | **Output** |
|---|---|
| 2  3 2  4 8 | B  D |

### PY01066 - XÂU “THĂNG BẰNG”

Một xâu ký tự được gọi là **“thăng bằng”** nếu khoảng cách của tất cả các cặp ký tự cạnh nhau trong xâu đó đều đúng bằng khoảng cách của hai vị trí tương ứng trong xâu đảo của nó.

Ví dụ xâu s1 có độ dài N và xâu đảo của nó là s2 thì xâu này sẽ thỏa mãn tính chất thăng bằng nếu:

**|**s1\[i\] – s1\[i-1\]**|** = **|**s2\[i\] – s2\[i-1\]**|** với tất cả giá trị 0 &lt; i &lt; N

Hãy kiểm tra xem một xâu ký tự bất kỳ có phải là xâu “thăng bằng” hay không.

**Input**

Dòng đầu ghi số bộ test. Mỗi bộ test là một xâu ký tự độ dài không quá 100000. Không có khoảng trống.

**Output**

Ghi ra YES hoặc NO.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  acxz  bcxz | YES  NO |

### PY01067 - SỐ 2 ƯU THẾ

Hệ thống máy tính mới chuyển sang sử dụng hệ đếm tam phân với ba chữ số 0, 1, 2.

Do vốn đã quen với hệ đếm nhị phân nên Nam chỉ quan tâm đến các số tam phân thỏa mãn chữ số 2 chiếm ưu thế, tức là số lượng chữ số 2 chiếm nhiều hơn 50% số chữ số của số đó.

Hãy giúp Nam liệt kê N số tam phân mà số 2 chiếm ưu thế đầu tiên (theo thứ tự từ nhỏ đến lớn).

**Input**  
 Dòng đầu ghi số bộ test (không quá 20)

Mỗi bộ test ghi số nguyên dương N (không quá 1000)

**Output**

Với mỗi test, viết trên một dòng N số tam phân ưu thế 2, các số cách nhau một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  5  10 | 2 22 122 202 212  2 22 122 202 212 220 221 222 1222 2022 |

### PY01068 - ĐẶT TÊN

Kỳ thi ICPC có K đội của PTIT tham gia và đội tuyển đang rất đau đầu không biết chọn các cái tên như thế nào cho các đội. Yêu cầu phải đảm bảo tên không có khoảng trống và không được trùng nhau. Sau khi thảo luận, có N cái tên được đề xuất (có thể bị trùng nhau). Với K&lt;15 và 4 &lt; N &lt; 30.

Hãy liệt kê tất cả danh sách các tổ hợp K cái tên khác nhau có thể được tạo ra theo thứ tự từ điển.

**Input**

Dòng đầu ghi 2 số N và K.

Tiếp theo là 1 dòng ghi N cái tên, mỗi cái tên có độ dài không quá 15 và cách nhau một khoảng trống. Tất cả đều là ký tự in hoa.

**Output**

Ghi ra tất cả các tổ hợp tên có thể được lựa chọn theo thứ tự từ điển.

Tức là các tên trong mỗi tổ hợp liệt kê theo thứ tự từ điển và các tổ hợp cũng được liệt kê theo thứ tự từ điển.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 6 2  DONG TAY NAM BAC TAY BAC | BAC DONG  BAC NAM  BAC TAY  DONG NAM  DONG TAY  NAM TAY |

### PY01069 - CHỮ SỐ NGUYÊN TỐ

Chúng ta đều biết chỉ có 4 chữ số nguyên tố là 2, 3, 5, 7. Hãy liệt kê tất cả các số có ít nhất 4 chữ số nhưng không quá N chữ số và thỏa mãn tất cả các điều kiện sau:

- Chỉ có các chữ số 2, 3, 5, 7
- Có đầy đủ 4 chữ số 2, 3, 5, 7
- Không phải là số chẵn.
 
**Input**

Chỉ có 1 dòng ghi số N (3 &lt; N &lt; 10)

**Output**

Ghi ra lần lượt các số thỏa mãn theo thứ tự tăng dần, mỗi số trên một dòng

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 4 | 2357  2375  2537  2573  2735  2753  3257  3275  3527  3725  5237  5273  5327  5723  7235  7253  7325  7523 |

### PY01071 - PYTHON FILE

Một file code Python sẽ có phần mở rộng là .py.

Trong hệ điều hành Windows tên file sẽ không phân biệt chữ hoa, chữ thường. Hãy kiểm tra xem tên file có đúng là file code Python hay không.

**Input**  
 Chỉ có một dòng ghi tên file S (1 ≤ |S| ≤ 128). Tên file chỉ chứa các ký tự ‘a’-‘z’, ‘A’-‘Z’, ‘.’ và dấu ‘\_’.

**Output**  
 In ra "yes" hoặc "no" tùy thuộc kết quả kiểm tra.

 | **Sample Input 1** | **Sample Output 1** |
|---|---|
| abc.py | yes |

 | **Sample Input 2** | **Sample Output 2** |
|---|---|
| abc.bin | no |

### PY01072 - BÀI TOÁN TỔ HỢP

Cho dãy số A\[\] có N phần tử. Hãy liệt kê tất cả các tổ hợp chập K của tập các phần tử khác nhau trong A\[\]. Các tổ hợp cần liệt kê theo thứ tự từ điển (tức là trong mỗi tổ hợp thì giá trị từ nhỏ đến lớn, và tổ hợp sau lớn hơn tổ hợp trước).

**Input**

Dòng đầu ghi hai số N và K.

Dòng thứ 2 ghi N số của mảng A\[\]. Các giá trị không quá 1000.

Dữ liệu đảm bảo số phần tử khác nhau của A\[\] không quá 20 và K không quá 10.

**Output**

Ghi ra lần lượt các tổ hợp tìm được, mỗi tổ hợp trên một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 8 3  2 4 4 3 5 1 3 4 | 1 2 3  1 2 4  1 2 5  1 3 4  1 3 5  1 4 5  2 3 4  2 3 5  2 4 5  3 4 5 |

### PY01073 - HOÁN VỊ KÝ TỰ

Cho xâu ký tự S có không quá 9 ký tự chữ cái in hoa, không có khoảng trống. Các ký tự khác nhau từng đôi một và đã được sắp xếp từ trái sang phải theo thứ tự từ điển. Hãy liệt kê tất cả các hoán vị của xâu ký tự S theo đúng thứ tự từ điển, mỗi hoán vị trên một dòng.

**Input**

Chỉ có một dòng ghi xâu S, độ dài không quá 9

**Output**

Ghi lần lượt các hoán vị theo thứ tự từ điển, mỗi xâu trên một dòng.

Chú ý: hoán vị đầu tiên chính là xâu S.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| XYZ | XYZ  XZY  YXZ  YZX  ZXY  ZYX |

### PY01074 - TỔNG ƯỚC SỐ

Cho N số nguyên. Nhiệm vụ của bạn là phân tích các số nguyên đã cho dưới dạng tích của các thừa số nguyên tố, sau đó tính tổng các ước số nguyên tố này.

**Input:**

Dòng đầu tiên số nguyên N (1 ≤≤ N ≤ 106).

N dòng tiếp theo, mỗi dòng gồm một số nguyên có giá trị không vượt quá 2\*106.

**Output**

In ra một số nguyên là đáp án tìm được.

**Ví dụ**

 | Input: | Output: |
|---|---|
| 5  7  9  10  13  100 | 47 |

*Giải thích test:*

*7 = 7*

*9 = 3 x 3 à 3 + 3 = 6*

*10 = 2 x 5 à 2 + 5 = 7*

*13 = 13*

*100 = 2 x 2 x 5 x 5 à 2+2+5+5 = 14*

*Cộng lại, 7 + 6 + 7 + 13 + 14 = 47.*

### PY01075 - TRÒ CHƠI TRÊN ĐƯỜNG THẲNG

Nam đang chơi một trò chơi. Trong trò này có một đường thẳng dài vô hạn với các điểm có tọa độ nguyên (âm, dương, 0). Lúc đầu Nam đang ở điểm có tọa độ 0.

Ngoài ra, trong trò chơi còn có *n* thẻ, thẻ thứ *i* có hai thuộc tính là *ai* và *ci*. Nếu muốn sử dụng thẻ thứ *i* thì Nam phải trả *ci* VNĐ. Khi đó Nam sẽ có các bước nhảy độ dài *ai*. Tức là từ điểm *x*, anh ấy có thể nhảy đến điểm *(x – ai)* hoặc *(x + ai).*

Nam muốn nhảy đến bất kì điểm nào trên đường thẳng (có thể qua một số điểm trung gian) và cô ấy muốn trả một số tiền ít nhất để mua các thẻ.

Hãy tính toán số tiền tối thiểu mà Nam phải bỏ ra.

**Input**

Dòng đầu chứa một số nguyên *T* - số trò chơi mà Nam chơi.

Mỗi trò chơi được mô tả trên 3 dòng:

- Dòng đầu tiên chứa một số nguyên *n* – số lượng thẻ trong trò chơi (không quá 200).
- Dòng thứ hai gồm *n* số nguyên *ai* (*1 ≤ ai ≤ 109*) - độ dài bước nhảy của thẻ.
- Dòng thứ ba gồm *n* số nguyên *ci* (*1 ≤ ci ≤ 105*) – chi phí của thẻ.
 
**Output**

Với mỗi trò chơi in kết quả trên một dòng. Nếu Nam không thể mua một số thẻ để đi đến bất kì ô nào in ra *-1*. Nếu không, in ra chi phí tối thiểu Nam phải bỏ ra để mua thẻ.

**Ví dụ**

 | **Test 1** | **Test 2** |
|---|---|
| **Input:**  1  3  2 6 4  1 1 1  **Output:**  -1 | **Input:**  1  3  3 4 5  1 2 3  **Output:**  3 |

### PY01076 - SỐ NGUYÊN LỚN

Cho hai số a và b trong đó a≤1012, b≤10250. Nhiệm vụ của bạn là tìm ước số chung lớn nhất của hai số a, b.

**Input:**

- Dòng đầu tiên đưa vào T là số lượng bộ test.
- T dòng tiếp đưa các bộ test. Mỗi bộ test gồm hai dòng: dòng đầu tiên đưa vào số a; dòng tiếp theo đưa vào số b.
- Các số T, a, b thỏa mãn ràng buộc: 1≤T≤100; 1≤a≤1012; 1≤b≤10250;
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
 **Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 1  1221  1234567891011121314151617181920212223242526272829 | 3 |

### PYKT037 - ĐỔI CƠ SỐ

Cơ số từ 2 đến 36 được xây dựng từ 10 chữ số (0 đến 9) và 26 chữ cái Tiếng Anh in hoa (‘A’ đến ‘Z’).

Hãy viết chương trình chuyển một số nguyên dương N trong cơ số 10 sang cơ số b. Trong đó N không quá 100.000, 2 ≤ b ≤ 36.

**Input**

Dòng đầu ghi số bộ test, không quá 10.

Mỗi bộ test ghi 2 số N và b.

Nlà một số nguyên dương N trong cơ số 10, không quá 100.000. 2 ≤ b ≤ 36

**Output**

Với mỗi bộ test ghi ra kết quả đổi cơ số tương ứng.

**Ví dụ**

 | **Input** | **Ouput** |
|---|---|
| 3  10 2  2021 2  31 16 | 1010  11111100101  1F |

### PYKT038 - HỆ CƠ SỐ 8

Cho một số nhị phân, người ta nhận ra quy tắc đơn giản là chỉ cần xét lần lượt các cụm ba chữ số nhị phân tình từ cuối của số đó, sau đó chuyển lần lượt từng cụm sang giá trị thập phân tương ứng thì kết quả nhận được chính là biểu diễn của số đó trong hệ cơ số 8. Nếu cụm cuối cùng bị thiếu thì bổ sung các chữ số 0 cho đủ 3 chữ số.

Ví dụ:

11001100 =&gt; 011 | 001 | 100 =&gt; 314

Hãy áp dụng tính chất trên để chuyển đổi một số nhị phân (không quá 100 chữ số và luôn bắt đầu bởi chữ số 1) sang hệ cơ số 8.

**Input**

Chỉ có một số nhị phân, không quá 100 chữ số

**Output**

Ghi ra kết quả trong hệ cơ số 8

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 1010 | 12 |
| 11001100 | 314 |

### PYKT065 - KIỂM TRA CHIA HẾT

Cho ba số nguyên dương L, R và N. Viết chương trình đếm số lượng các số thỏa mãn cả hai điều kiện:

- Nằm trong đoạn \[L, R\].
- Không chia hết cho bất kỳ số nào trong đoạn \[2, N\].
 
**Input**

Với mỗi bộ test:

- - Dòng đầu gồm 2 số nguyên dương L, R (1 ≤ L, R ≤ 1018).
    - Dòng thứ 2 chứa số nguyên dương N (2 ≤ N ≤ 50).
 
Input kết thúc với một dòng chứa số nguyên -1.

**Output**

Với mỗi bộ test, in ra kết quả trong một dòng.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 1 10  10  2001 2309  50  34 2003  50  -1 | 1  40  289 |

### PYKT080 - THỐNG KÊ DỊCH TỄ

Trước diễn biến phức tạp của dịch bệnh, thành phố đang có chủ chương thống kê dịch tễ các trường hợp liên quan đến bệnh nhân mắc COVID-19.

Thông tin về bệnh nhân được biểu diễn trên ma trận. Bạn hãy thực hiện thống kê nhanh các trường hợp có nguy cơ lây nhiễm. Nguyên tắc tính là đếm các trường hợp xung quanh bệnh nhân đã tiếp xúc (8 ô xung quanh).

**Input:**

Dòng đầu tiên là 2 số M, N là các số nguyên &lt;= 100, cho biết kích thước của ma trận.

Tiếp theo là ma trận M x N, các số nguyên A\[i\]\[j\] có giá trị &lt; 10. Vị trí của mỗi bệnh nhân được đánh số -1. Các ô mang giá trị &gt;= 0 thể hiện số trường hợp có nguy cơ lây nhiễm (không tính các bệnh nhân).

**Output:**

Tổng số các ca có nguy cơ lây nhiễm trên toàn thành phố.

 | **Input:** | **Output:** |
|---|---|
| 4 4    1 1 0 1    2 -1 4 5    0 0 0 0    1 0 2 1 | 8 |

### PYKT081 - ĐỊA CHỈ IP

Địa chỉ IP (IP là viết tắt của từ tiếng Anh: Internet Protocol - giao thức Internet) là một địa chỉ đơn nhất mà những thiết bị điện tử hiện nay đang sử dụng để nhận diện và liên lạc với nhau trên mạng máy tính bằng cách sử dụng giao thức Internet.

Bất kỳ thiết bị mạng nào bao gồm bộ định tuyến, bộ chuyển mạch mạng, máy vi tính, máy chủ hạ tầng (như NTP, DNS, DHCP, SNMP, v.v.), máy in, máy fax qua Internet, và vài loại điện thoại—tham gia vào mạng đều có địa chỉ riêng, và địa chỉ này là đơn nhất trong phạm vi của một mạng cụ thể. Vài địa chỉ IP có giá trị đơn nhất trong phạm vi Internet toàn cầu, trong khi một số khác chỉ cần phải đơn nhất trong phạm vi một công ty.

Ipv4 viết tắt cho Internet Protocol Version 4, dịch ra có nghĩa là giao thức Internet phiên bản thứ 4. Ipv4 đã được bộ quốc phòng Hoa Kỳ chuẩn hóa trong bản MIL-STD-1777. Giao thức Internet IP đã trải qua nhiều phiên bản khác nhau và phiên bản Ipv4 là phiên bản đầu tiên được sử dụng rộng rãi trên toàn thế giới và hiện vẫn còn đang là nòng cốt của Internet trên toàn thế giới.

Để hiểu địa chỉ Ipv4 là gì có thể lấy ví dụ như sau: Giả sử ta có 1 dải số như sau: 172.16.254.1. Dải số này có thể được dùng để đặt tên cho 1 địa chỉ Ipv4 nào đó. Có thể thấy địa chỉ Ipv4 có tổng cộng 4 số và mỗi số phải nằm trong giới hạn từ 0-255.

Cho một danh sách các chuỗi ký tự, hãy kiểm tra xem chuỗi ký tự này có phải địa chỉ IP hợp lệ hay không.

**Input:**

Dòng đầu tiên cho số T là số bộ test

T dòng tiếp theo mỗi dòng là một chuỗi bất kỳ có độ dài &lt; 1000

**Output:**

In ra kết quả theo từng dòng

 | **Input:** | **Output:** |
|---|---|
| 2  192.168.1.1  256.255.255.255 | YES  NO |

### PYKT082 - TÍNH ĐIỂM THI IELTS

Thang điểm IELTS được tính từ 1.0 – 9.0 IELTS (Overall điểm thi IELTS được tính trung bình cộng điểm 4 kỹ năng Reading, Listening, Speaking và Writing).

4 kỹ năng của IELTS cũng tính từ 1.0-9.0 để sau đó tính điểm thi IELTS Overall.

Cả 2 phần thi nghe (Listening) và đọc (Reading) đều có 40 câu hỏi thí sinh cần trả lời. Với một câu trả lời đúng sẽ được 1 điểm, tối đa là 40 điểm và quy đổi sang thang điểm 1.0 – 9.0 dựa trên tổng số câu trả lời đúng.

Dưới đây là bảng điểm quy đổi sẽ giúp cho các bạn hiểu hơn về cách chuyển đổi điểm cho từng phần thi Reading và Listening.

 | Listening/Reading |
|---|
| Correct answers | Band score |
| 39 - 40 | 9.0 |
| 37- 38 | 8.5 |
| 35 - 36 | 8.0 |
| 33 - 34 | 7.5 |
| 30 - 32 | 7.0 |
| 27 - 29 | 6.5 |
| 23 - 26 | 6.0 |
| 20 - 22 | 5.5 |
| 16 - 19 | 5.0 |
| 13 - 15 | 4.5 |
| 10 - 12 | 4.0 |
| 7- 9 | 3.5 |
| 5 - 6 | 3.0 |
| 3 - 4 | 2.5 |

Thang điểm IELTS trên bảng kết quả của thí sinh sẽ thể hiện điểm của từng kỹ năng thi cùng với điểm overall. Phần điểm tổng sẽ được tính dựa trên điểm trung bình cộng của 4 kỹ năng.

Điểm tổng của 4 kỹ năng sẽ được làm tròn số theo quy ước chung như sau: Nếu điểm trung bình cộng của 4 kỹ năng có số lẻ là .25, thì sẽ được làm tròn lên thành .5, còn nếu là .75 sẽ được làm tròn thành 1.0.

Một trung tâm tổ chức thi thử Tiếng Anh cho các học viên. Hãy giúp trung tâm tính điểm overall dựa trên kết quả bài làm của thí sinh nhé.

Input:

Dòng đầu cho số T là số lượng thí sinh

T dòng tiếp theo mỗi dòng cho 4 số là số câu đúng lần lượt của kỹ năng Reading, Listening, điểm kỹ năng speaking, và điểm kỹ năng writing.

Output:

In ra kết quả theo từng dòng.

 | **Input:** | **Output:** |
|---|---|
| 2  15 25 5.0 5.5  22 32 6.0 6.0 | 5.5  6.0 |

### PYKT088 - SỐ CÓ 9 ƯỚC SỐ

Cho số nguyên dương N. Hãy đếm các số nguyên dương không lớn hơn N và có đúng 9 ước số.

**Input**

Chỉ có một dòng ghi số N (1 ≤ N ≤ 109).

**Output**

Ghi ra số lượng các số có 9 chữ số

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 888 | 8 |

## CÂU LỆNH ĐIỀU KHIỂN

### PY01048 - TỔNG LIÊN TIẾP

Một số số nguyên dương có thể được biểu diễn thành tổng của các số nguyên dương liên tiếp.

Ví dụ: 6 = 1 +2 + 3 hoặc 9 = 4 + 5 hoặc 9 = 2 + 3 + 4

Cho số nguyên dương N không quá 9 chữ số. Hãy đếm xem có bao nhiêu cách biểu diễn N thành tổng các số nguyên dương liên tiếp.

**Input**

Dòng đầu ghi số bộ test, không quá 20.

Mỗi bộ test ghi một số nguyên dương N, không quá 9 chữ số.

**Output**

Ghi ra số cách tìm được.

**Ví dụ**

 | **Input** | **Ouput** |
|---|---|
| 3  6  8  9 | 1  0  2 |

### PY01065 - PHÉP TOÁN CƠ BẢN

Cho một biểu thức trong phạm vi hai chữ số với các phép toán cộng trừ nhân chia. *Các toán hạng và kết quả đảm bảo là số nguyên dương có hai chữ số*, *nếu có phép chia thì phải thỏa mãn tính chia hết.*

Người ta có thể ẩn đi một số chữ số hoặc phép toán bằng cách điền dấu chấm hỏi (?). Nhiệm vụ của bạn là khôi phục các dấu chấm hỏi và in ra phép toán chính xác ban đầu. Nếu không thể có kết quả đúng thì ghi ra WRONG PROBLEM!

**Dữ liệu vào**

Dòng đầu ghi số bộ test T (1 ≤ T ≤ 100).

T dòng tiếp theo, mỗi dòng là một biểu thức *có thể* có các dấu ?.

*Dữ liệu vào đảm bảo chỉ có duy nhất một kết quả đúng hoặc không thể có kết quả đúng.*

**Kết quả**

Với mỗi bộ test, ghi ra biểu thức đúng tìm được. Hoặc WRONG PROBLEM!

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2    ?0 ? 12 = 28    40 / ?3 = ?? | 40 - 12 = 28  WRONG PROBLEM! |

### PY01070 - BÀI TOÁN HÌNH HỌC - 1

Cho *N* điểm trên mặt phẳng Oxy. Nhiệm vụ của bạn là xác định xem có tồn tại một đường tròn ngoại tiếp của 3 đỉnh và thỏa mãn có đúng K điểm ***nằm trong*** đường tròn hay không (không tính các điểm nằm trên đường tròn).

**Dữ liệu vào:**

Dòng đầu tiên là số lượng bộ test T (T ≤ 10).

Mỗi test gồm số nguyên *N* (3 ≤ N ≤ 100), là số lượng điểm trên mặt phẳng. Dòng tiếp theo là số nguyên *K (1 ≤ K ≤ 100)*.

*N* dòng tiếp theo, dòng thứ *i* gồm 2 số nguyên xi, y*i* (-1000 ≤ *xi, yi ≤ 1000*).

**Kết quả:**

Với mỗi test, in ra “YES” nếu tìm được đường tròn chứa đúng K điểm. In ra “NO” trong trường hợp ngược lại.

**Ví dụ:**

 | **Input** | **Output** |
|---|---|
| 2  4  1  0 0  5 0  0 5  1 1  5  2  5 5  5 -5  -5 5  -5 -5  0 0 | YES  NO |

### PY02031 - KIỂM TRA NGUYÊN TỐ

Cho ma trận A\[\] cỡ N\*M chỉ bao gồm các số nguyên dương không quá 1000. Hãy kiểm tra các số trong ma trận, nếu giá trị nào là số nguyên tố thì thay thế bằng số 1, không phải thì thay thế bằng số 0.

**Input**

Dòng đầu ghi 2 số N và M là kích thước ma trận (1 &lt; N,M &lt; 20)

N dòng tiếp theo mỗi dòng có M số mô tả ma trận

**Output**

Ghi ra ma trận kết quả

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3 3  1 2 3  4 5 6  7 8 9 | 0 1 1  0 1 0  1 0 0 |

### PY02038 - ĐẾM CẶP ĐỒNG XU

Cho một lưới hình vuông kích thước N\*N. Trên một số ô của lưới người ta đặt các đồng xu (ký hiệu bằng chữ cái C (coin)). Hãy đếm xem có thể lấy ra bao nhiêu cặp đồng xu ở cùng một hàng hoặc cùng một cột.

**Input**

Dòng đầu tiên ghi số N (1 ≤ N ≤ 100)

N dòng tiếp theo mô tả trạng thái của lưới, chữ cái C ứng với vị trí có đồng x, dấu chấm tương ứng với ô trống)

**Output**

Ghi ra số cặp đồng xu đếm được.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 4  CC..  C..C  .CC.  .CC. | 9 |

### PY02049 - ƯỚC SỐ CỦA GIAI THỪA

Cho số tự nhiên N và số nguyên tố P. Nhiệm vụ của bạn là tìm số x lớn nhất để N! chia hết cho px. Ví dụ với N=7, p=3 thì x=2 là số lớn nhất để 7! Chia hết cho 32.

**Input:**

- Dòng đầu tiên đưa vào số lượng bộ test T.
- Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là cặp số N, p được viết cách nhau một vài khoảng trống.
- T, N, p thỏa mãn ràng buộc : 1≤T≤100; 1≤N≤105; 2≤p≤5000;
 
**Output:**

- Đưa ra kết quả mỗi test theo từng dòng.
 
 **Ví dụ:**

 | Input: | Output: |
|---|---|
| 3    62 7    76 2    3 5 | 9    73    0 |

## ĐỐI TƯỢNG

### PY04001 - LỚP POINT

Khai báo lớp Point (điểm trong không gian hai chiều) với hai thuộc tính là tọa độ x và tọa độ y (số thực).

nhập vào hai điểm p1, p2 và tính khoảng cách hai điểm đó.

**Input**

- Dòng đầu ghi số bộ test, không quá 20.
- Mỗi bộ test có 4 số thực lần lượt là tọa độ của 2 điểm A và B, giá trị tuyệt đối không quá 1000.
 
**Ouput**

Với mỗi bộ test, viết ra khoảng cách giữa 2 điểm với 4 chữ số phần thập phân.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  0 0 0 5  0 199 5 6 | 5.0000  193.0648 |

### PY04002 - LỚP RECTANGLE

Khai báo lớp Rectangle với 3 thuộc tính:

- Chiều dài: số nguyên
- Chiều rộng: số nguyên
- Màu sắc: xâu ký tự
 
Nhập vào giá trị độ dài hai cạnh của hình chữ nhật và màu sắc. In ra thông tin về chu vi, diện tích và màu sắc (đã đưa về dạng chuẩn trong đó ký tự đầu viết hoa, các ký tự sau viết thường) của hình chữ nhật đó.

**Input**

Gồm 2 số nguyên là độ dài 2 cạnh hình chữ nhật và một xâu ký tự (không có khoảng trống) mô tả màu sắc.

**Output**

Nếu hình chữ nhật là hợp lệ (các cạnh đều nguyên dương) thì in ra 3 thông tin: chu vi, diện tích, màu sắc, mỗi thông tin cách nhau một khoảng trống.

Nếu dữ liệu không hợp lệ in ra INVALID

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 10 2 RED | 24 20 Red |

### PY04003 - LỚP PHÂN SỐ - 1

Khai báo lớp Phân số gồm hai thuộc tính tử số và mẫu số. Các giá trị đều nguyên dương và không quá 18 chữ số.

Nhập vào một phân số và in ra phân số đó ở dạng tối giản.

**Input**

Có hai số nguyên dương lần lượt là tử số và mẫu số.

**Output**

Ghi ra phân số tối giản như trong ví dụ

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 123 456 | 41/152 |

### PY04004 - LỚP PHÂN SỐ - 2

Khai báo lớp Phân số gồm hai thuộc tính tử số và mẫu số. Các giá trị đều nguyên dương và không quá 18 chữ số.

nhập vào hai phân số p và q. Tính tổng p + q, rút gọn và in ra kết quả.

**Input**

Có bốn số nguyên dương lần lượt là tử số và mẫu số của p rồi đến q.

**Output**

Ghi ra phân số tổng p + q ở dạng tối giản như trong ví dụ

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 123 456 12 34 | 1609/2584 |

### PY04005 - LỚP TRIANGLE - 1

Sử dụng lớp Point đã có trong bài 1, khai báo lớp Triangle với thuộc tính là 3 điểm. Viết các phương thức phù hợp để tính chu vi tam giác.

**Input**

- Dòng đầu ghi số bộ test, không quá 10
- Mỗi bộ test ghi trên 1 dòng 6 số thực có giá trị tuyệt đối không quá 1000 lần lượt là tọa độ của 3 điểm.
 
**Output**

- Nếu 3 điểm không thể tạo thành tam giác thì in ra INVALID
- Nếu 3 điểm tạo thành 1 tam giác thì in ra chu vi của tam giác đó, làm tròn đến 3 chữ số phần thập phân.
 
**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  0 0 0 5 0 199  1 1 1 1 1 1  0 0 0 5 5 0 | INVALID  INVALID  17.071 |

### PY04006 - LỚP TRIANGLE - 2

Sử dụng lớp Point đã có trong bài 1, khai báo lớp Triangle với thuộc tính là 3 điểm. Viết các phương thức phù hợp để tính diện tích tam giác.

*Công thức Heron tính diện tích tam giác khi biết độ dài 3 cạnh là a,b,c:*

![](./img/PY04006_0.png)

**Input**

- Dòng đầu ghi số bộ test, không quá 10
- Mỗi bộ test ghi trên 1 dòng 6 số thực có giá trị tuyệt đối không quá 1000 lần lượt là tọa độ của 3 điểm.
 
**Output**

- Nếu 3 điểm không thể tạo thành tam giác thì in ra INVALID
- Nếu 3 điểm tạo thành 1 tam giác thì in ra diện tích của tam giác đó, làm tròn đến 2 chữ số phần thập phân.
 
**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  0 0 0 5 0 199  1 1 1 1 1 1  0 0 0 5 5 0 | INVALID  INVALID  12.50 |

### PY04007 - LỚP MATRIX - 1

Khai báo lớp Matrix mô tả ma trận các số nguyên với các thuộc tính là kích thước ma trận và mảng hai chiều lưu các phần tử.

Nhập ma trận a cấp n\*m. Hãy viết chương trình tính tích của a với ma trận chuyển vị của a.

**Input:** Dòng đầu tiên ghi số bộ test.

Với mỗi bộ test:

- Dòng đầu tiên ghi hai số n và m là bậc của ma trân a;
- n dòng tiếp theo, mỗi dòng ghi m số của một dòng trong ma trận. n và m đều nguyên dương và nhỏ hơn 50. Các giá trị trong ma trận không vượt quá 100.
 
**Output:** Với mỗi bộ test ghi ra ma trận tích tương ứng, mỗi số cách nhau đúng một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 1  2 2  1 2  3 4 | 5 11  11 25 |

### PY04008 - LỚP MATRIX - 2

Khai báo lớp Matrix mô tả ma trận các số nguyên với các thuộc tính là kích thước ma trận và mảng hai chiều lưu các phần tử.

Nhập ma trận a cấp n\*m. Hãy viết chương trình tính tích của a với ma trận chuyển vị của a.

**Input:** Dòng đầu tiên ghi số bộ test.

Với mỗi bộ test:

- Dòng đầu tiên ghi hai số n và m là bậc của ma trân a;
- n dòng tiếp theo, mỗi dòng ghi m số của một dòng trong ma trận. n và m đều nguyên dương và nhỏ hơn 50. Các giá trị trong ma trận không vượt quá 100.
 
**Output:** Với mỗi bộ test ghi ra ma trận tích tương ứng, mỗi số cách nhau đúng một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 1  2 2  1 2  3 4 | 5 11  11 25 |

### PY04009 - LỚP SỐ PHỨC

Khai báo lớp Số phức với hai thuộc tính là phần thực và phần ảo.

Viết chương trình thực hiện nhập hai số phức A, B và thực hiện các thao tác tính toán trên số phức

- C = (A + B) x A
- D = (A + B)2
 
**Input:**

Dòng đầu tiên là số bộ test T (T &lt;= 100)

T dòng tiếp theo mỗi dòng gồm 4 số lần lượt là a, b, c, d, với -102 &lt; a, b, c, d &lt; 102.

**Output:**

Kết quả của hai phép tính theo định dạng trong ví dụ

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3    1 2 3 4    2 3 4 5    1 -2 5 -6 | -8 + 14i, -20 + 48i    -12 + 34i, -28 + 96i    -10 - 20i, -28 - 96i |

### PY04010 - LỚP THÍ SINH - 1

Viết chương trình khai báo lớp Thí Sinh gồm các thông tin: Họ tên, Ngày sinh, Điểm môn 1, Điểm môn 2, Điểm môn 3 và Tổng điểm.

Đọc thông tin 1 thí sinh từ bàn phím và in ra màn hình 3 thông tin: Họ tên, Ngày sinh, Tổng điểm.

**Input**

Gồm 5 dòng lần lượt, mỗi dòng ghi 1 thông tin: Họ tên, Ngày sinh, Điểm môn 1, Điểm môn 2, Điểm môn 3. Họ tên không quá 50 chữ cái, Ngày sinh viết đúng chuẩn dd/mm/yyyy. Các giá trị điểm là số thực (float).

**Output**

Ghi ra Họ tên, Ngày sinh và Tổng điểm. Mỗi thông tin cách nhau một khoảng trống. Điểm được ghi ra với 1 số sau dấu phẩy.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| Nguyen Hoang Ha  11/10/2001  4.5  10.0  5.5 | Nguyen Hoang Ha 11/10/2001 20.0 |

### PY04011 - LỚN HƠN – NHỎ HƠN

Để kiểm tra tư duy của các thành viên, câu lạc bộ IT PTIT ra một đề toán logic trong đó các tên thành viên trong CLB được sử dụng để đưa vào phép các phép so sánh. Chỉ có hai phép so sánh được sử dụng là *lớn hơn* và *nhỏ hơn*.

Cho trước một dãy các phép so sánh, hãy chỉ ra liệu có thể tất cả các phép so sánh đó đều đúng hay không?

**Dữ liệu vào**

- Dòng đầu ghi số N là số phép so sánh. (1 ≤ N ≤ 105).
- Mỗi phép so sánh gồm 2 tên thành viên và một dấu lớn hơn hoặc nhỏ hơn, mỗi cái tên là một dãy ký tự không quá 20 chữ cái, không có khoảng trống.
 
**Kết quả**

- Ghi ra **“possible”** nếu tất cả phép so sánh đều có thể đúng hoặc **“impossible”** nếu ngược lại.
 
**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  An &gt; Binh  Binh &gt; Cong  An &lt; Cong | impossible |
| 3  An &gt; Binh  Binh &gt; Cong  An &gt; Cong | possible |

### PY04012 - TÍNH ĐIỂM CHUYÊN CẦN

Lớp học phần môn XYZ của trường ABC có không quá 100 sinh viên. Danh sách sinh viên gồm các thông tin: mã sinh viên, họ tên, lớp. Môn học có 10 buổi. Dữ liệu điểm danh với mỗi sinh viên được cho bởi một xâu ký tự gồm 10 ký tự trong đó: x là có mặt, m là đến muộn, v là vắng.

Với điểm chuyên cần tối đa là 10. Giả sử mỗi buổi vắng bị trừ 2 điểm, mỗi buổi đến muộn bị trừ 1 điểm. Hãy tính điểm chuyên cần cho mỗi sinh viên (tất nhiên nếu tính ra điểm âm thì ghi vào bảng điểm vẫn là 0).

Nếu điểm bằng 0 thì in thêm ghi chú KDDK (tức là không đủ điều kiện dự thi hết môn).

**Input**

Dòng đầu ghi số n là số sinh viên. Mỗi sinh viên ghi trên 3 dòng lần lượt là mã sinh viên, họ tên, lớp.

Tiếp theo là n dòng ghi dữ liệu điểm danh. Mỗi dòng gồm mã sinh viên, sau đó là một khoảng trống rồi đến xâu ký tự điểm danh có đúng 10 chữ cái.

**Output**

Ghi ra danh sách điểm chuyên cần (theo đúng thứ tự ban đầu) gồm các thông tin:

- Mã sinh viên
- Họ và tên
- Lớp
- Điểm chuyên cần
- Ghi chú (nếu có)
 
Mỗi thông tin cách nhau một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  B19DCCN999  Le Cong Minh  D19CQAT02-B  B19DCCN998  Tran Truong Giang  D19CQAT02-B  B19DCCN997  Nguyen Tuan Anh  D19CQCN04-B  B19DCCN998 xxxmxmmvmx  B19DCCN997 xmxmxxxvxx  B19DCCN999 xvxmxmmvvm | B19DCCN999 Le Cong Minh D19CQAT02-B 0 KDDK  B19DCCN998 Tran Truong Giang D19CQAT02-B 4  B19DCCN997 Nguyen Tuan Anh D19CQCN04-B 6 |

### PY04013 - TÍNH TOÁN LƯỢNG MƯA

Trong một ngày mưa nhiều, các trạm đo mưa hoạt động hết công suất. Tại mỗi trạm đo, các cơn mưa được ghi nhận thời điểm bắt đầu, thời điểm kết thúc và lượng mưa đo được. Một trạm mưa có thể có nhiều lần mưa trong ngày.

Hãy tính lượng mưa trung bình trong 1 giờ (60 phút) của từng trạm theo đúng thứ tự trong danh sách ban đầu. Chú ý để tính lượng mưa trung bình thì cần tính tất các lần đo mưa tại trạm đó.

**Input**

Dòng đầu ghi số lượt đo lượng mưa.

Thông tin về một lần đo lượng mưa gồm 4 dòng:

- Tên trạm
- Thời điểm bắt đầu mưa (hh:mm)
- Thời điểm kết thúc mưa (hh:mm)
- Lượng mưa đo được
 
Số trạm đo khác nhau nhỏ hơn 10.

**Output**

Ghi ra danh sách các trạm khác nhau trong danh sách đo mưa và lượng mưa trung bình của từng trạm.

Thông tin trên mỗi dòng lần lượt gồm:

- Mã trạm đo (tính từ T01). Chú ý: nếu cùng tên trong danh sách đo thì cũng sẽ cùng mà trạm.
- Tên trạm đo mưa
- Lượng mưa trung bình trong 1 giờ tại mỗi trạm (tính chính xác đến 2 số phần thập phân).
 
Các thông tin ghi cách nhau một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 10  Dong Anh  07:30  08:00  60  Cau Giay  07:45  08:12  50  Soc Son  08:00  09:15  78  Dong Anh  18:50  20:00  88  Cau Giay  19:01  20:00  77  Soc Son  19:06  20:21  66  Dong Anh  21:00  21:40  49  Cau Giay  21:50  22:20  68  Dong Anh  22:15  23:45  30  Cau Giay  22:50  23:45  35 | T01 Dong Anh 59.22  T02 Cau Giay 80.70  T03 Soc Son 57.60 |

### PY04014 - BẢNG ĐIỂM

Trường THCS XYZ lập bảng điểm tổng kết cho học sinh. Có 10 môn học lần lượt gồm: Toán, Tiếng Việt, Ngoại ngữ, Vật lý, Hóa học, Sinh học, Lịch Sử, Địa, Giáo dục công dân và môn Công nghệ. Trong đó môn Toán và Tiếng Việt tính hệ số 2, các môn còn lại hệ số 1.

Học sinh được xếp hạng theo điểm trung bình:

- Từ 9 trở lên: loại XUAT SAC
- Từ 8 đến 8.9: loại GIOI
- Từ 7 đến 7.9: loại KHA
- Từ 5 đến 6.9: loại TB
- Dưới 5: loai YEU
 
Hãy lập bảng điểm tổng kết và sắp xếp theo điểm trung bình giảm dần.

**Input**

Dòng đầu ghi số học sinh (không quá 50).

Thông tin về mỗi học sinh có hai dòng: dòng đầu là họ tên (độ dài không quá 50), dòng thứ 2 gồm 10 số thực trong đoạn \[0..10\] lần lượt là điểm 10 môn theo đúng thứ tự đã mô tả.

**Output**

Danh sách đã sắp xếp được ghi ra bao gồm các thông tin:

- Mã học sinh (tự động gán tăng dần theo thứ tự nhập, bắt đầu là HS01)
- Họ và tên
- Điểm trung bình (với 1 chữ số phần thập phân)
- Xếp loại
 
Trong trường hợp điểm trung bình bằng nhau thì học sinh nào có mã học sinh nhỏ hơn sẽ xếp trên.

**Ví dụ**

 | **Input** |
|---|
| 3  Luu Thuy Nhi  9.3 9.0 7.1 6.5 6.2 6.0 8.2 6.7 4.8 5.5  Le Van Tam  8.0 8.0 5.5 9.0 6.8 9.0 7.2 8.3 7.2 6.8  Nguyen Thai Binh  9.0 6.4 6.0 7.5 6.7 5.5 5.0 6.0 6.0 6.0 |
| **Output** |
| HS02 Le Van Tam 7.7 KHA  HS01 Luu Thuy Nhi 7.3 KHA  HS03 Nguyen Thai Binh 6.6 TB |

### PY04015 - LẬP HÓA ĐƠN - 1

Tiền nước hàng tháng của thành phố ABC được tính theo đơn giá trong bảng sau:

![](./img/PY04015_0.png)

Trong đó, phụ phí được hiểu là số tiền tính thêm (theo phần trăm) trên tổng số tiền nước tiêu thụ.

Cho danh sách khách hàng và chỉ số đồng hộ. Hãy sắp xếp danh sách hóa đơn theo tổng số tiền giảm dần.

**Input**

Dòng đầu ghi số khách hàng (không quá 20).

Mỗi khách hàng viết trên 3 dòng gồm:

- Tên khách hàng (xâu ký tự độ dài không quá 50)
- Chỉ số cũ
- Chỉ số mới
 
Trong đó chỉ số mới lớn hơn hoặc bằng chỉ số cũ, cả hai đều không quá 4 chữ số.

**Output**

Ghi ra danh sách khách hàng đã sắp xếp theo tổng tiền giảm dần gồm các thông tin

- Mã khách hàng (tự động gán tăng dần theo thứ tự nhập, bắt đầu từ KH01)
- Tên khách hàng
- Tổng số tiền (được làm tròn ở dạng số nguyên)
 
**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  Le Thi Thanh  468  500  Le Duc Cong  160  230  Ha Hue Anh  410  612 | KH03 Ha Hue Anh 34545  KH02 Le Duc Cong 8240  KH01 Le Thi Thanh 3264 |

### PY04016 - LẬP HÓA ĐƠN - 2

Khách sạn XYZ có đơn giá (theo ngày) được quy định khác nhau theo từng tầng. Khách hàng đến thuê phòng sẽ được tính tổng số tiền ở theo đơn giá cộng thêm chi phí dịch vụ phát sinh nếu có.

![](./img/PY04016_0.png)

Hãy giúp khách sạn tính tiền phải trả cho từng khách hàng và sắp xếp theo thứ tự tổng tiền giảm dần.

**Input**

Dòng đầu ghi số khách hàng (không quá 20)

Mỗi khách hàng ghi trên 4 dòng gồm:

- Tên khách hàng (xâu ký tự độ dài không quá 100)
- Số phòng
- Ngày nhận phòng (định dạng dd/mm/yyyy)
- Ngày trả phòng (định dạng dd/mm/yyyy)
- Tiền dịch vụ phát sinh (số nguyên dương nhỏ hơn 100)
 
**Output**

Ghi ra danh sách đã được sắp xếp theo tổng tiền giảm dần bao gồm lần lượt các thông tin:

- Mã khách hàng (tự động tăng theo thứ tự nhập, tính từ KH01)
- Tên khách hàng
- Số phòng
- Số ngày ở
- Thành tiền
 
**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  Huynh Van Thanh  103  05/06/2010  05/06/2010  15  Le Duc Cong  106  08/03/2010  01/05/2010  220  Tran Thi Bich Tuyen  207  10/04/2010  21/04/2010  96 | KH02 Le Duc Cong 106 55 1595  KH03 Tran Thi Bich Tuyen 207 12 504  KH01 Huynh Van Thanh 103 1 40 |

### PY04017 - TÍNH VẬN TỐC

Cuộc đua xe đạp bắt đầu từ **6h00** với độ dài quãng đường đua là **120 Km**. Các cua-rơ sẽ được ghi nhận thành tích dựa trên thời điểm đến đích. Hãy xếp hạng theo thứ tự thành tích giảm dần.

**Input**

Dòng đầu ghi số cua-rơ tham gia cuộc đua.

Mỗi cua-rơ ghi trên 3 dòng:

- Họ tên (xâu ký tự độ dài không quá 50)
- Đơn vị (xâu ký tự độ dài không quá 20)
- Thời điểm đến đích theo định dạng h:mm
 
**Output**

Ghi ra danh sách đã sắp xêp theo thành tích, tốt hơn xếp trước, kém hơn xếp sau.

Thông tin mỗi cua-rơ bao gồm:

- Mã (là chữ cái đầu tiên của các từ trong tên đơn vị ghép với chữ cái đầu tiên các từ trong họ tên – xem ví dụ để hiểu rõ hơn)
- Họ tên
- Đơn vị
- Vận tốc trung bình (đã làm tròn ra giá trị nguyên)
 
**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  Tran Vu Minh  Ha Noi  8:30  Vu Ngoc Hoang  Hoa Binh  8:20  Pham Dinh Tan  An Giang  8:45 | HBVNH Vu Ngoc Hoang Hoa Binh 51 Km/h  HNTVM Tran Vu Minh Ha Noi 48 Km/h  AGPDT Pham Dinh Tan An Giang 44 Km/h |

### PY04018 - XÁC ĐỊNH TRÚNG TUYỂN

Trường THPT ACB tuyển giáo viên mới cho ba môn Toán, Lý, Hóa. Theo yêu cầu mới, bài thi tuyển gồm 2 nội dung: Tin học và Chuyên môn. Điểm thi Tin học sẽ được nhân đôi khi tính tổng điểm.

Mỗi GV có thể có điểm ưu tiên được xét theo mã như trong bảng sau:

![](./img/PY04018_0.png)

Mã xét tuyển gồm 2 thành phần. Chữ cái đầu tiên ứng với môn học: A là Toán, B là Lý và C là Hóa; tiếp theo là 1 chữ số thể hiện mã ưu tiên.

Tổng điểm sau khi cộng điểm ưu tiên nếu từ 18 trở lên sẽ được xét TRÚNG TUYỂN, nhỏ hơn sẽ bị LOẠI.

Viết chương trình nhập danh sách điểm thi và sắp xếp GV theo thứ tự tổng điểm giảm dần. Mã GV dự thi được tự động gán theo thứ tự bắt đầu từ 01.

**Input**

Dòng đầu thi số giáo viên đăng ký thi tuyển (không quá 20).

Mỗi GV được viết trên 4 dòng gồm:

- Tên GV (xâu ký tự độ dài không quá 50)
- Mã xét tuyển
- Điểm tin học (số thực trong phạm vi 0 đến 10)
- Điểm chuyên môn (số thực trong phạm vi 0 đến 10)
 
**Output**

Ghi ra danh sách đã sắp xếp. Thông tin mỗi GV gồm: Mã GV, Tên, Môn học, Tổng điểm (1 chữ số phần thập phân), Kết quả. Mỗi thông tin cách nhau một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  Le Van Binh  A1  7.0  3.0  Tran Van Toan  B3  4.0  7.0  Hoang Thi Tam  C2  7.0  6.0 | GV03 Hoang Thi Tam HOA 21.5 TRUNG TUYEN  GV01 Le Van Binh TOAN 19.0 TRUNG TUYEN  GV02 Tran Van Toan LY 16.0 LOAI |

### PY04019 - TUYỂN NHÂN VIÊN

Doanh nghiệp X cần tuyển một số nhân viên mới. Bài thi tuyển có hai phần: lý thuyết và thực hành. Sau khi tính điểm trung bình, các thí sinh sẽ được xếp thành 4 loại:

- Nếu điểm dưới 5 -&gt; TRUOT
- Nếu điểm lớn hơn hoặc bằng 5 nhưng nhỏ hơn 8 -&gt; CAN NHAC
- Nếu điểm từ 8 đến 9.5 -&gt; DAT
- Nếu điểm lớn hơn 9.5 -&gt; XUAT SAC
 
Điểm các bài thi lý thuyết và thực hành đều là số thực trong phạm vi từ 0 đến 10. Tuy nhiên, khi nhập điểm các bài thi, cán bộ tuyển dụng có thể quên mất dấu . phân cách phần nguyên và phần thập phân. Do đó nếu điểm ghi là 78 thì cần được hiểu là 7.8

Hãy sắp xếp danh sách thí sinh đã được xếp loại theo điểm trung bình giảm dần.

**Input**

Dòng đầu ghi số thí sinh. Mỗi thí sinh ghi trên 3 dòng lần lượt là:

- Họ và tên (xâu ký tự độ dài không quá 100)
- Điểm lý thuyết
- Điểm thực hành
 
Mã thí sinh cần được tự động gán theo mẫu TS + số thứ tự (tính từ 01).

**Output**

Ghi ra danh sách thí sinh đã sắp xếp, mỗi thí sinh gồm 4 thông tin: mã thí sinh, họ tên, điểm trung bình (với 2 số phần thập phân) và xếp loại. Mỗi thông tin cách nhau một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  Nguyen Thai Binh  45  75  Le Cong Hoa  4  4.5  Phan Van Duc  56  56 | TS01 Nguyen Thai Binh 6.00 CAN NHAC  TS03 Phan Van Duc 5.60 CAN NHAC  TS02 Le Cong Hoa 4.25 TRUOT |

### PY04020 - LẬP HÓA ĐƠN - 3

Cửa hàng điện máy – điện lạnh cần lập hóa đơn tính tiền cho khách hàng. Mỗi mặt hàng sẽ có đơn giá và một số tiền được gọi là chiết khấu trên tổng hóa đơn. Số tiền phải thanh toán sẽ bằng đơn giá \* số lượng sau đó trừ đi tiền chiết khấu.

Hãy tính tiền cho từng hóa đơn và sắp xếp theo số tiền giảm dần.

**Input**

Dòng đầu ghi số lượng hóa đơn. Không quá 20.

Mỗi thông tin hóa đơn gồm 5 dòng:

- Mã mặt hàng (xâu ký tự độ dài không quá 10, không có khoảng trống)
- Tên mặt hàng (xâu ký tự độ dài không quá 100, có thể có khoảng trống)
- Số lượng mua (không quá 50)
- Đơn giá (số nguyên dương có thể đến 10 chữ số)
- Tiền chiết khấu của hóa đơn (có thể đến 9 chữ số).
 
**Output**

Ghi ra danh sách hóa đơn đã sắp xếp, trong đó mỗi dòng gồm đầy đủ 6 thông tin: mã mặt hàng, tên mặt hàng, số lượng mua, đơn giá, chiết khấu và tổng tiền. Mỗi thông tin cách nhau một khoảng trống.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  ML01  May lanh SANYO  12  4000000  2400000  ML02  May lanh HITACHI  4  2550000000  0  ML03  May lanh NATIONAL  5  3000000  150000 | ML02 May lanh HITACHI 4 2550000000 0 10200000000  ML01 May lanh SANYO 12 4000000 2400000 45600000  ML03 May lanh NATIONAL 5 3000000 150000 14850000 |

### PY04021 - TÍNH TOÁN THỜI GIAN

Quán Game mùa này vắng khách nên chủ quán quyết định tính tiền chi tiết đến từng phút. Dựa trên dữ liệu giờ vào và giờ ra, hãy tính thời gian chơi game của các Game thủ nhé.

**Input**

Dòng đầu của dữ liệu vào ghi số lượng game thủ trong ngày (không quá 20).

Thông tin về một game thủ đến chơi game được ghi lại trên 4 dòng lần lượt là:

- Mã người chơi (xâu ký tự độ dài không quá 10, không có khoảng trống)
- Tên người chơi (xâu ký tự độ dài không quá 100, có thể có khoảng trống).
- Giờ vào (định dạng hh:mm)
- Giờ ra (định dạng hh:mm)
 
**Ouput**

Ghi ra danh sách game thủ đã được sắp xếp theo thời gian chơi game giảm dần.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 3  01T  Nguyen Van An  09:00  10:30  06T  Hoang Van Nam  15:30  18:00  02I  Tran Hoa Binh  09:05  10:00 | 06T Hoang Van Nam 2 gio 30 phut  01T Nguyen Van An 1 gio 30 phut  02I Tran Hoa Binh 0 gio 55 phut |

### PYKT076 - DANH SÁCH PHIM

Trên hệ thống phim của một website có các thông tin bộ phim bao gồm Mã phim, Tên phim, Ngày khởi chiếu, Số tập phim, Thể loại. Mã phim được đánh số tự động từ P001, P002 và tự động tăng dần. Thể loại phim bao gồm thông tin Mã thể loại và Tên thể loại. Mã thể loại được đanh số tự động tăng dần từ TL001, TL002

Cho danh sách các phim trên hệ thống, hãy thực hiện sắp xếp danh sách các bộ phim theo thứ tự ưu tiên ngày khởi chiếu tăng dần, tên phim sắp xếp theo thứ tự từ điển, số tập phim giảm dần.

Input:

Dòng đầu tiên cho 2 số N, M lần lượt là số lượng thể loại và số lượng bộ phim.

N dòng tiếp theo là thông tin tên thể loại. Mã thể loại tự động sinh theo thứ tự nhập vào

M dòng còn lại mỗi dòng là thông tin phim bao gồm Mã thể loại, ngày khởi chiếu (dd/mm/yyyy) tên phim và số tập phim (số nguyên tối đa 10000).

Output:

Danh sách phim đã sắp xếp như mẫu, mỗi phim trên một dòng

Ví dụ:

 | Input | Output |
|---|---|
| 2 3  Hai huoc  Tinh cam  TL001  25/11/2021  Phim so 1  10  TL001  04/12/2021  Phim so 2  15  TL002  25/11/2021  Phim so 3  5 | P001 Hai huoc 25/11/2021 Phim so 1 10    P003 Tinh cam 25/11/2021 Phim so 3 5    P002 Hai huoc 04/12/2021 Phim so 2 15 |

### PYKT077 - LỊCH THI HỌC KỲ

Hệ thống quản lý lịch thi học kỳ cho nhiều Môn học, mỗi môn học có các (Có thông tin Mã môn học, tên môn học) Lịch thi học kỳ bao gồm nhiều thông tin gồm: Mã ca thi, Mã môn học, Ngày thi, Giờ thi, Nhóm thi. Mã ca thi được đánh số từ T001, T002 và tự động tăng dần.

Cho danh sách các ca thi, mỗi môn học có nhiều ca thi, hãy thực hiện sắp xếp danh sách các ca thi theo thứ tự ưu tiên như sau ngày tăng dần, giờ tăng dần, mã môn học tăng dần.

Input:

Dòng đầu tiên cho 2 số N, M lần lượt là số môn học và số ca thi.

N \* 2 dòng tiếp theo là thông tin mã môn học và tên môn học.

M dòng còn lại mỗi dòng là thông tin lịch thi bao gồm Mã môn học, ngày thi (dd/mm/yyyy) giờ thi (hh:mm) và nhóm thi (dạng xâu ký có 2 ký tự bất kỳ).

Output:

Lịch thi đã sắp xếp như mẫu, mỗi lịch thi trên một dòng

Ví dụ:

 | Input | Output |
|---|---|
| 2 10  INT1155  Tin hoc co so 2  INT1339  Ngon ngu lap trinh C++  INT1155 25/11/2021 08:00 01  INT1155 04/12/2021 08:00 02  INT1155 04/12/2021 13:30 03  INT1155 25/11/2021 13:30 04  INT1155 25/11/2021 15:00 05  INT1339 25/11/2021 08:00 01  INT1339 25/11/2021 08:00 02  INT1339 04/12/2021 13:30 03  INT1339 04/12/2021 13:30 04  INT1339 04/12/2021 15:00 05 | T001 INT1155 Tin hoc co so 2 25/11/2021 08:00 01  T006 INT1339 Ngon ngu lap trinh C++ 25/11/2021 08:00 01  T007 INT1339 Ngon ngu lap trinh C++ 25/11/2021 08:00 02  T004 INT1155 Tin hoc co so 2 25/11/2021 13:30 04  T005 INT1155 Tin hoc co so 2 25/11/2021 15:00 05  T002 INT1155 Tin hoc co so 2 04/12/2021 08:00 02  T003 INT1155 Tin hoc co so 2 04/12/2021 13:30 03  T008 INT1339 Ngon ngu lap trinh C++ 04/12/2021 13:30 03  T009 INT1339 Ngon ngu lap trinh C++ 04/12/2021 13:30 04  T010 INT1339 Ngon ngu lap trinh C++ 04/12/2021 15:00 05 |

### PYKT092 - ĐIỂM TUYỂN SINH

Theo quy định mới, điểm tuyển sinh vào trường đại học XYZ sau khi tính tổng sẽ được cộng ưu tiên, cụ thể:

- Thí sinh khu vực 1 ưu tiên 1.5 điểm
- Thí sinh khu vực 2 ưu tiên 1 điểm
- Thí sinh khu vực 3 không ưu tiên
- Thí sinh dân tộc Kinh không ưu tiên
- Thí sinh các dân tộc khác ưu tiên 1.5 điểm
 
Hãy tính tổng điểm đã ưu tiên và xác định tình trạng trúng tuyển. Biết điểm chuẩn của trường năm nay là 20.5 điểm.

**Input**

Dòng đầu ghi số thí sinh.

Mỗi thí sinh ghi trên 4 dòng gồm:

- Họ tên: có thể chưa chuẩn hóa
- Điểm thi: giá trị số thực không quá 30
- Dân tộc
- Khu vực
 
**Output**

Ghi ra danh sách đã sắp xếp theo tổng điểm (đã tính ưu tiên) giảm dần, nếu tổng điểm bằng nhau thì sắp xếp theo mã thí sinh tăng dần. Các thông tin cần liệt kê gồm:

- Mã thí sinh (tính theo thứ tự nhập từ TS01)
- Họ tên đã chuẩn hóa
- Tổng điểm với đúng 1 chữ số phần thập phân
- Trạng thái: Do hoặc Truot
 
**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  Nguyen hong ngat  22  Kinh  1   Chu thi MINh  14  Dao  3 | TS01 Nguyen Hong Ngat 23.5 Do  TS02 Chu Thi Minh 15.5 Truot |

### PYKT093 - TÍNH ĐIỂM TRUNG BÌNH

Nhóm sinh viên PTIT cùng nhau đăng ký 3 môn học trong Học kỳ hè năm 2021 theo đúng thứ tự:

- Môn 1: Lập trình hướng đối tượng: 3 tín chỉ
- Môn 2: Ngôn ngữ lập trình C++: 3 tín chỉ
- Môn 3: Tin học cơ sở 2: 2 tín chỉ
 
Người ta muốn xếp hạng thứ tự các sinh viên trong danh sách theo điểm trung bình giảm dần. Biết rằng điểm trung bình tính đến 2 số phần thập phân và nếu điểm bằng nhau thì thứ hạng cũng bằng nhau.

**Input**

Dòng đầu ghi số sinh viên (không quá 20).

Mỗi sinh viên ghi trên 4 dòng gồm:

- Họ tên: có thể chưa được chuẩn hóa
- Điểm môn 1
- Điểm môn 2
- Điểm môn 3
 
Các giá trị điểm là số nguyên và đảm bảo trong phạm vi từ 0 đến 10.

**Output**

Ghi ra danh sách sinh viên đã tính điểm và sắp xếp theo xếp hạng từ cao nhất đến thấp nhất, gồm các thông tin:

- Mã sinh viên (tự động tăng theo thứ tự nhập, tính từ SV01)
- Họ tên đã chuẩn hóa
- Điểm trung bình với đúng 2 số phần thập phân
- Xếp hạng
 
Chú ý: 2 sinh viên có điểm trung bình bằng nhau thì xếp hạng bằng nhau, và nếu có 2 sinh viên hạng là X thì sinh viên tiếp theo trong danh sách có hạng X+2.

Trong trường hợp xếp hạng bằng nhau thì cần sắp xếp theo mã sinh viên tăng dần.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2   ha Thi kieu anh  7  6  7  Pham THI HAO  6  7  6 | SV01 Ha Thi Kieu Anh 6.63 1  SV02 Pham Thi Hao 6.38 2 |

### PYKT094 - TÍNH LƯƠNG

Công ty XYZ mỗi năm đều cập nhật hồ sơ và gán lại mã cho nhân viên (có đúng 5 ký tự) theo quy tắc sau:

- Ký tự đầu tiên là phân loại nhân viên, có 4 nhóm là A, B, C, D
- Hai chữ số tiếp theo mô tả số năm công tác
- Hai ký tự cuối là mã phòng ban.
 
Dựa trên loại nhân viên và số năm công tác, hệ số nhân để tính lương được cho trong bảng sau:

![](./img/PYKT094_0.png)

Mỗi nhân viên theo hợp đồng sẽ có một giá trị lương cơ bản có thể rất khác nhau. Lương tháng được tính bằng tích của lương cơ bản với số ngày công và hệ số nhân.

Cho trước danh sách phòng ban, gồm mã phòng và tên phòng. Cho trước các thông tin nhân viên gồm mã, tên, lương cơ bản (tính theo ngày – đơn vị nghìn VNĐ) và số ngày công. Hãy tính toán và in ra bảng lương nhân viên trong tháng.

**Input**

Dòng đầu ghi số phòng ban, mỗi phòng ban viết trên một dòng gồm mã phòng và tên phòng.

Tiếp theo là một dòng ghi số nhân viên, mỗi nhân viên ghi trên 4 dòng gồm mã, tên, lương cơ bản (tính theo ngày), số ngày công.

**Output**

Lập bảng lương của nhân viên theo đúng thứ tự nhập. Mỗi nhân viên cần ghi ra các thông tin sau đây trên một dòng:

- Mã nhân viên
- Tên nhân viên
- Phòng ban
- Lương tháng
 
**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2  HC Hanh chinh  KH Ke hoach Dau tu  2  C06HC  Tran Binh Minh  65  25  D03KH  Le Hoa Binh  59  24 | C06HC Tran Binh Minh Hanh chinh 16250000  D03KH Le Hoa Binh Ke hoach Dau tu 11328000 |

### PYKT095 - TÍNH TIỀN ĐIỆN

Các hộ gia đình trong thành phố X được chia thành 3 loại A, B, C với định mức sử dụng điện như sau:

- Loại A: Định mức 100 kWh
- Loại B: Định mức 500 kWh
- Loại C: Định mức 200 kWh
 
Hãy tính toán số tiền phải thanh toán theo quy tắc:

**Tính tiền trong định mức:**

Nếu số điện (Số cuối - Số đầu) nhỏ hơn định mức thì bằng số điện \* 450

Nếu số điện lớn hơn hoặc bằng định mức thì bằng định mức \*450

**Tiền vượt định mức**

Nếu số điện lớn hơn định mức thì bằng (số điện - định mức) \*1000

Ngược lại thì bằng 0

**Thuế VAT** = 5% số tiền vượt định mức.

*Chú ý: tiền thuế VAT cũng là số nguyên dương nên có thể lấy số tiền vượt định mức chia phần nguyên cho 20.*

**Số tiền phải nộp = Tiền trong định mức + Tiền vượt định mức + Thuế VAT**

**Input**

Dòng đầu ghi số khách hàng (không quá 50).

Mỗi khách hàng ghi trên 2 dòng:

- Họ tên: có thể chưa chuẩn hóa
- Loại hộ gia đình, chỉ số đầu, chỉ số cuối. Mỗi thông tin cách nhau một khoảng trống.
 
**Output**

Ghi ra danh sách đã sắp xếp theo tổng số tiền phải trả giảm dần gồm các thông tin:

- Mã khách hàng: tính từ KH01 theo thứ tự nhập
- Họ tên đã chuẩn hóa
- Tiền trong định mức
- Tiền vượt định mức
- Thuế VAT
- Tổng số tiền phải nộp.
 
Dữ liệu đảm bảo không có hai hộ gia đình nào có cùng số tiền nộp bằng nhau.

**Ví dụ**

 | **Input** | **Output** |
|---|---|
| 2   nGuyEn Hong Ngat  C 200 278   Chu thi minh  A 120 160 | KH01 Nguyen Hong Ngat 35100 0 0 35100  KH02 Chu Thi Minh 18000 0 0 18000 |

### PYKT097 - CHUẨN HÓA CÂU

Một câu trong văn bản được hiểu là dãy ký tự (có cả khoảng trống) cho đến khi gặp dấu ngắt câu hoặc xuống dòng (tức là đôi khi người ta quên viết dấu ngắt câu nhưng cứ xuống dòng là sang một câu mới). Các dấu ngắt câu trong bài toán này bao gồm: dấu chấm (.), dấu chấm cảm (!), dấu chấm hỏi (?).

Hãy viết chương trình chuẩn hóa các câu trong dữ liệu vào với các yêu cầu sau:

- Ký tự đầu mỗi câu viết hoa, các ký tự khác viết thường.
- Các từ cách nhau đúng một khoảng trống.
- Tự động điền thêm dấu chấm (.) nếu xuống dòng mà chưa có dấu ngắt câu.
- Dấu ngắt câu phải viết sát ký tự cuối cùng của câu (không tính khoảng trống)
 
**Input**

Một văn bản không quá 100 dòng.

**Output**

Ghi ra các câu đã chuẩn hóa, mỗi câu 1 dòng.

**Ví dụ**

 | **Input** |
|---|
| Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet Ke theo chuan quoc te.  co 03 chuyen nganh la: Cong nghe phan mem, Tri tue nhan tao va An toan thong tin  muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep  moi CAC BAN danG ky thaM giA ! |
| **Output** |
| Chuong trinh dao tao clc nganh cntt duoc thiet ke theo chuan quoc te.  Co 03 chuyen nganh la: cong nghe phan mem, tri tue nhan tao va an toan thong tin.  Muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep.  Moi cac ban dang ky tham gia! |

### PYKT13038 - HÌNH TRÒN - 1

Cho *N* điểm trên mặt phẳng Oxy. Nhiệm vụ của bạn là xác định xem có tồn tại một đường tròn ngoại tiếp của 3 đỉnh và thỏa mãn có đúng K điểm nằm trong đường tròn (không tính các điểm nằm trên đường tròn).

**Input:**

Dòng đầu tiên là số lượng bộ test T (không quá 10).

Mỗi test gồm số nguyên *N (3≤N≤100)*, là số lượng điểm trên mặt phẳng. Dòng tiếp theo là số nguyên *K (1≤K≤100)*.

*N* dòng tiếp theo, dòng thứ *i* gồm 2 số nguyên ![](file:///C:/Users/Dell/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png) (trị tuyệt đối không quá 1000).

**Output:**

Với mỗi test, in ra “YES” nếu tìm được đường tròn chứa đúng K điểm. In ra “NO” trong trường hợp ngược lại.

**Ví dụ:**

 | Input | Output |
|---|---|
| 2  4  1  0 0  5 0  0 5  1 1  5  2  5 5  5 -5  -5 5  -5 -5  0 0 | YES  NO |

### PYKT13039 - HÌNH TRÒN - 2

Bắt đầu từ một hình tròn lớn nội tiếp tam giác vuông (hình 1) người ta thử vẽ thêm các hình tròn nhỏ hơn tiếp xúc với cạnh huyền, cạnh góc vuông của tam giác và tiếp xúc với đường tròn lớn ban đầu (hình 2).

![](./img/PYKT13039_0.png)

Hình 1: Hình tròn nội tiếp tam giác vuông

![](./img/PYKT13039_1.png)

Hình 2: Vẽ thêm hình tròn thứ 2 tiếp xúc hình tròn thứ nhất và hai cạnh của tam giác

Tiếp tục theo cách như vậy người ta có thể vẽ vô hạn hình tròn nhỏ hơn nữa. Khi số lượng hình tròn đã rất lớn (tiến đến vô hạn), người ta muốn tính xem diện tích được bao phủ bởi các hình tròn bằng bao nhiêu phần diện tích của tam giác vuông.

**Input**

Chỉ có một dòng ghi hai cạnh góc vuông của tam giác vuông (là hai số nguyên dương khác nhau, không quá 105).

**Output**

Ghi ra tỉ lệ diện tích của tất cả các hình tròn trên diện tích tam giác (tính chính xác đến 4 số sau dấu phẩy).

**Ví dụ**

 | **Input 1** | **Output 1** |
|---|---|
| 3 4 | 0.7171 |
| **Input 2** | **Output 2** |
| 12 16 | 0.7171 |

### PYKT13040 - HÌNH TRÒN - 3

Với 8 hình tròn có kích thước bằng nhau, người ta có thể xếp 8 hình tròn này vào một hình vuông theo cách như hình dưới đây.

![](./img/PYKT13040_0.png)

Bài toán đặt ra là cho trước kích thước hình vuông, hãy tính **độ dài bán kích lớn nhất có thể** của 8 hình tròn bằng nhau có thể xếp vào hình vuông đó.

**Input**

Chỉ có một số thực với 4 số phần thập phân cho biết diện tích hình vuông ban đầu.

**Output**

Ghi ra độ dài bán kính lớn nhất có thể của hình tròn, tính chính xác đến 4 số sau dấu phẩy.

**Ví dụ**

 | **Input 1** | **Output 1** |
|---|---|
| 0.3438 | 0.1000 |
| **Input 2** | **Output 2** |
| 1.3753 | 0.2000 |