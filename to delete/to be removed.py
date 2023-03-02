
#todo deprecated remove it
def tool_steps(tooldata,d_website):
    result=""
    for counter, (key, d_step) in enumerate(tooldata.items()):
        if callable(key):
            d_step=key()

        onestep=get("component_tool_step.html").format(**{
            "stepnumber":counter+1,
            "steptitle": d_step["steptitle"],
            "stepdescription":d_step["stepdescription"],
            "stepcontent":d_step["stepcontent"],
        })
        result+=onestep
    result = pformat(result, d_website)
    return result


#todo deprecated remove it
def tool_faq(tooldata,d_website):
    result = ""
    #get the generla QA
    d_all_AQ={**tooldata, **d_general_faq}
    for counter, (question,answer) in enumerate(d_all_AQ.items()):
        oneQA = get("component_tool_faq.html").format(**{
            "faq_number": counter+1,
            "faq_question": question,
            "faq_answer": answer,
        })
        result += oneQA
    result = pformat(result, d_website)
    return result



def c_input(steptitle="Input", stepdescription="Copy paste your table here.",stepcontent='<div id="table1"></div>'):
    return {"steptitle":steptitle,
             "stepdescription":stepdescription,
             "stepcontent":stepcontent,
             }

def c_configure(steptitle="Configure",stepdescription="Configure the options.",stepcontent="empty todo"):
    return {"steptitle":steptitle,
              "stepdescription":stepdescription,
              "stepcontent":stepcontent,
              }

def c_download(steptitle="Download",stepdescription="Copy or Download your result in CSV.",tableid="table2"):
    return {
        "steptitle": steptitle,
        "stepdescription": stepdescription,
        "stepcontent": f'<div id="{tableid}"></div><button id="download" type="button" class="btn btn-primary width50" style="display:inline-block;width:100%;margin:0px;" > Download</button>',
        }


def c_slider(label="Last n Rows"):
    return {
        "steptitle": "Configure",
        "stepdescription": "Configure your options",
        "stepcontent": f"""
        <div class="form-group">
      <label class="control-label col" for="n">{label}:</label>
      <div class="col">
       <input id="n" type="range" class="form-range" min="1" max="100">
        </div>
    </div>""",
    }

