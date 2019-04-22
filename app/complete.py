from flask import (Blueprint, redirect, render_template, request, session, url_for)
from .io import save_anon_data
from .utils import gen_code

## Initialize blueprint.
bp = Blueprint('complete', __name__)

@bp.route('/complete')
def complete():
    """Present completion screen to participant."""
    return render_template('complete.html', value=session['complete'])

@bp.route('/datadump', methods = ['POST'])
def datadump():
    """Save jsPsych data to disk."""

    if request.is_json:

        ## Retrieve jsPsych data.
        JSON = request.get_json()

        ## Save jsPsch data to disk.
        save_anon_data(JSON, session['TASK'], session['DATA_DIR'])

    ## Generate completion code.
    session['complete'] = gen_code(16)

    return redirect(url_for('complete.complete'))
