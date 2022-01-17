from app import app, job_queue

from app.api import test_job

from fastapi.responses import HTMLResponse

@app.get('/', response_class=HTMLResponse)
def index():

    task = job_queue.enqueue(test_job)
    n = len(job_queue.jobs)

    html = '<center><br /><br />'
    for job in job_queue.jobs:
        html += f'<a href="job/{job.id}">{job.id}</a><br /><br />'
    html += f'Total {n} Jobs in queue </center>'
    return f"{html}"


@app.get('/job/<job_id>', response_class=HTMLResponse)
def getJob(job_id):

    res = job_queue.fetch_job(job_id)

    if not res.result:
        return f'<center><br /><br /><h3>The job is still pending</h3><br /><br />ID:{job_id}<br />Queued at: {res.enqueued_at}<br />Status: {res._status}</center>'

    return f'<center><br /><br /><img src="{res.result}" height="200px"><br /><br />ID:{job_id}<br />Queued at: {res.enqueued_at}<br />Finished at: {res.ended_at}</center>'
