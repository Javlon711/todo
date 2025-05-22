from django.http import HttpResponse

def task_create(request):
    html_response = """
    <form>
      <h2>Vazifalar Ro'yxati</h2>
      <h3>Yangi vazifa qo'shish</h3><br>

      <label for="name">Vazifa nomi:</label>
      <input type="text" id="fname" name="fname"><br><br>

      <label for="desc">Tavsif:</label>
      <textarea name="desc" rows="4" cols="30"></textarea><br><br>

      <label for="importance">Muhimlik darajasi:</label>
      <select name="importance" id="importance">
        <option value="Yuqori">Yuqori</option>
        <option value="O‘rta">O‘rta</option>
        <option value="Past">Past</option>
      </select><br><br>

      <label for="due_dat">Muddati:</label>
      <input type="date" id="due_dat"><br><br>

      <button type="submit">Vazifa qo'shish!</button><br><br><br>

      <h3>Mavjud vazifalar</h3>

      <table style="border-collapse: collapse;">
        <tr>
          <th style="padding: 8px;">Vazifa</th>
          <th style="padding: 8px;">Tavsif</th>
          <th style="padding: 8px;">Muhimlik</th>
          <th style="padding: 8px;">Muddati</th>
          <th style="padding: 8px;">Holat</th>
        </tr>
        <tr>
          <td style="padding: 8px;">Hisobot tayyorlash</td>
          <td style="padding: 8px;">Oylik moliyaviy hisobotni tayyorlash va topshirish</td>
          <td style="padding: 8px;">Yuqori</td>
          <td style="padding: 8px;">2023-05-31</td>
          <td style="padding: 8px;">Bajarilmoqda</td>
        </tr>
        <tr>
          <td style="padding: 8px;">Mijoz bilan uchrashuv</td>
          <td style="padding: 8px;">Yangi loyiha bo‘yicha mijoz bilan muzokaralar o‘tkazish</td>
          <td style="padding: 8px;">O‘rta</td>
          <td style="padding: 8px;">2023-05-25</td>
          <td style="padding: 8px;">Rejalashtirilgan</td>
        </tr>
        <tr>
          <td style="padding: 8px;">Prezentatsiya tayyorlash</td>
          <td style="padding: 8px;">Yangi mahsulot uchun taqdimot slaydlarini tayyorlash</td>
          <td style="padding: 8px;">Past</td>
          <td style="padding: 8px;">2023-06-05</td>
          <td style="padding: 8px;">Boshlanmagan</td>
        </tr>
        <tr>
          <td style="padding: 8px;">Xodimlar uchun trening</td>
          <td style="padding: 8px;">Yangi dasturiy ta’minot bo‘yicha xodimlarga qo‘llanma berish</td>
          <td style="padding: 8px;">O‘rta</td>
          <td style="padding: 8px;">2023-06-10</td>
          <td style="padding: 8px;">Rejalashtirilgan</td>
        </tr>
        <tr>
          <td style="padding: 8px;">Loyiha hujjatlarini yangilash</td>
          <td style="padding: 8px;">Joriy loyihaning texnik hujjatlarini yangilash va arxivlash</td>
          <td style="padding: 8px;">Past</td>
          <td style="padding: 8px;">2023-06-15</td>
          <td style="padding: 8px;">Boshlanmagan</td>
        </tr>
      </table>
    </form>
    """
    return HttpResponse(html_response)
