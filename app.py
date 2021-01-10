from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def average_main():
    if request.method=="POST":
        resp = request.form
        student_name = resp.get('nm')
        a = resp.get('first')
        b = resp.get('second')
        c = resp.get('third')
        d = resp.get('fourth')
        e = resp.get('fifth')

        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        result = ((a+b+c+d+e)/5)

        return render_template("result.html", abc=result, first=a, second=b, third=c, fourth=d, fifth=e, nm=student_name)
    else:
        return render_template("input.html")

if __name__ == '__main__':
    app.run(debug=True)
