import pandas as pd
from selenium import webdriver
from xpinyin import Pinyin
pd.options.display.expand_frame_repr=False

def fun_list_to_str(list):
    result = ''
    if len(list) == 1:
        return list[0]
    else:
        for i in range(len(list)):
            if i == 0:
                result = list[i]
            else:
                result = result + '/' + list[i]
    return result

def fun_get_text_byxpath(browser,xpath):
    return list(map(lambda x: x.text, browser.find_elements_by_xpath(xpath)))

def fun_get_info_from_page_imdb(browser):
    df = pd.DataFrame(index=range(1),
                      columns=['name', 'release_date', 'director(s)', 'main_actors/actresses',
                               'average_rating_score', 'number_of_rating_people', 'brief_introduction'])
    # Movie name
    name_xpath = "//*[@id='title-overview-widget']/div[1]/div[2]/div/div[2]/div[2]/h1"
    # Release date
    date_xpath = "//*[@id='title-overview-widget']/div[1]/div[2]/div/div[2]/div[2]/div/a[@title='See more release dates']"
    # Directors
    director_xpath = "//*[@id='title-overview-widget']//div[@class='plot_summary_wrapper']/div[1]/div[2]/a"
    # Main_actors/actresses
    actors_xpath = "//*[@id='title-overview-widget']//div[@class='plot_summary_wrapper']/div[1]/div[4]/a[position()<=3]"
    # Average rating score
    score_xpath = "//*[@id='title-overview-widget']/div[1]/div[2]/div/div[1]/div[1]/div[1]/strong/span"
    # Number_of_rating_people
    people_xpath = "//*[@id='title-overview-widget']/div[1]/div[2]/div/div[1]/div[1]/a/span"
    xpath = [name_xpath, date_xpath, director_xpath, actors_xpath, score_xpath, people_xpath]
    for i in range(df.columns.__len__() - 1):
        df.iloc[0, i] = fun_list_to_str(fun_get_text_byxpath(browser, xpath[i]))

    # Brief_introduction
    try:  # If the brief is not complete, we need to open the whole page of introduction
        element = browser.find_element_by_xpath("//*[@id='title-overview-widget']/div[2]/div[2]/div[1]/div[1]/a")
        browser.get(element.get_attribute("href"))
        brief_xpath = "//*[@id='plot-summaries-content']/li/p"
        brief = fun_list_to_str(fun_get_text_byxpath(browser, brief_xpath))
        df['brief_introduction'] = brief
        return df
    except:
        brief_xpath = "//*[@id='title-overview-widget']//div[@class='plot_summary_wrapper']/div[1]/div[1]"
        brief = fun_list_to_str(fun_get_text_byxpath(browser, brief_xpath))
        df['brief_introduction'] = brief
        return df

def fun_single_movie_IMDb(browser,url_form,movie):

    movie = Pinyin().get_pinyin(movie,'+').replace(" ","+")
    url = url_form.format(movie)
    browser.get(url) # Open searching result page
    element = browser.find_element_by_xpath("//*[@id='main']/div/div[2]/table/tbody/tr[1]/td")
    element.click() # Open movie information page

    return fun_get_info_from_page_imdb(browser)

def fun_single_movie_db(browser,url_form,movie):
    df = pd.DataFrame(index=range(1),
                      columns=['name', 'release_date', 'director(s)', 'main_actors/actresses',
                               'average_rating_score', 'number_of_rating_people', 'brief_introduction'])
    movie = movie.replace(" ", "+")
    url = url_form.format(movie)
    browser.get(url)
    i = 1
    while 'subject' not in browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[1]/div["+ str(i) +"]//a").get_attribute('href'):
        i += 1
    else:
        element = browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div[1]/div["+ str(i) +"]//a")
    element.click()
    try:
        element = browser.find_element_by_xpath("// *[ @ id = 'link-report'] / span[1] / a")
        element.click()
    except:
        pass
    # Movie name
    name_xpath = "//*[@id='content']/h1/span[1]"
    # Release date
    date_xpath = "//*[@id='info']/span[@property='v:initialReleaseDate']"
    # Directors
    director_xpath = "//*[@id='info']/span[1]/span[@class='attrs']/a"
    # Main_actors/actresses
    actors_xpath = "//*[@id='info']/span[@class='actor']/span[@class='attrs']/span[position()<=5]/a"
    if fun_list_to_str(fun_get_text_byxpath(browser,actors_xpath))=='':
        actors_xpath = "//*[@id='info']/span[3]/span[@class='attrs']/a[position()<=5]"
    # Average rating score
    score_xpath = "//*[@id='interest_sectl']/div[1]/div[2]/strong"
    # Number_of_rating_people
    people_xpath = "//*[@id='interest_sectl']/div[1]/div[2]/div/div[2]/a/span"
    # Brief_introduction
    brief_xpath = "//*[@id='link-report']/span"

    xpath = [name_xpath,date_xpath,director_xpath,actors_xpath,score_xpath,people_xpath,brief_xpath]
    for i in range(df.columns.__len__()):
        df.iloc[0,i] = fun_list_to_str(fun_get_text_byxpath(browser,xpath[i]))
    return df

def fun_main(web,browser,movies):
    if web.upper() == 'DOUBAN':
        url_form = "https://movie.douban.com/subject_search?search_text={}&cat=1002"
        func = fun_single_movie_db
    elif web.upper() =='IMDB':
        url_form = 'https://www.imdb.com/find?q={}&s=tt&ttype=ft&ref_=fn_ft'
        func = fun_single_movie_IMDb
    else:
        print('Web info is wrong!')
    results = []
    for movie in movies:
        try:
            results.append(func(browser,url_form,movie))
        except:
            print ('Fail in getting information of ' + movie)
            continue
    result = pd.concat(results)
    result.to_csv('Movies_info_'+ web.upper() +'.csv',encoding='utf_8_sig')
    return result

def fun_get_top_250_db():
    '''
    Just get the list of Top 250
    :return:
    '''
    url_form = 'https://movie.douban.com/top250?start={}&filter='
    root_xpath = '//*[@id="content"]/div/div[1]/ol'
    list_250_db = []
    for i in range(10):
        url = url_form.format(str(i*25))
        browser.get(url)
        for j in range(25):
            name_xpath = root_xpath + '/li['+str(j+1)+']/div/div[2]/div[1]/a/span[1]'
            list_250_db.append(fun_get_text_byxpath(browser,name_xpath)[0])
    return list_250_db

def fun_get_top_250_imdb():
    '''
    Get the info of top 250
    :return:
    '''
    url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250_6'
    browser.get(url)
    df_imdb_250 = []
    root_xpath= '//*[@id="main"]/div/span/div/div/div[3]/table/tbody'
    for j in range(250):
        name_xpath = root_xpath + '/tr[' + str(j + 1) + ']/td[2]/a'
        element = browser.find_element_by_xpath(name_xpath)
        element.click()
        df_imdb_250.append(fun_get_info_from_page_imdb(browser))
        browser.get(url)
        if j % 10 == 0: print (j)
    result = pd.concat(df_imdb_250)
    return result

if __name__ == '__main__':
    my_path = r"C:\Users\zzliv\Downloads\chromedriver_win32\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=my_path)  # webdriver.Chrome for chromedriver
    browser.maximize_window()
    # Test movies
    movies = ['天龙八部','肖申克的救赎','羞羞的铁拳','最后的武士','请叫我英雄','英雄','枪火','影']
    # Test results
    df_db = fun_main('Douban',browser,movies)
    df_imdb = fun_main('IMDB', browser, movies)

    #Bonus 1
    list_250_db = fun_get_top_250_db()
    df_db_250 = fun_main('Douban',browser,list_250_db)
    df_db_250.to_csv('Top_250_Douban.csv',encoding='utf_8_sig')

    df_imdb_250 =  fun_get_top_250_imdb()
    df_imdb_250.to_csv('Top_250_IMDb.csv')






