

function moveQB(btn) {
    var name = $(btn).closest('tr').find('td:eq(0)').text();
    var salary = $(btn).closest('tr').find('td:eq(2)').text();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap - playerSalary;

    if (newSalaryCap < 0) {
        alert('You have exceeded the salary cap!');
        return;
    }
    $('#qbInput').val(name + " (" + salary + ")");
    $(btn).closest('tr').remove();
    $('#salaryCap').text('$' + newSalaryCap);

}


function moveRB(btn) {
    var name = $(btn).closest('tr').find('td:eq(0)').text();
    var salary = $(btn).closest('tr').find('td:eq(2)').text();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap - playerSalary;

    if (newSalaryCap < 0) {
        alert('You have exceeded the salary cap!');
        return;
    }

    if ($('#rbInput').val() == '') {
        $('#rbInput').val(name + " (" + salary + ")");
    } else if ($('#rb2Input').val() == '') {
        $('#rb2Input').val(name + " (" + salary + ")");
    }
    $(btn).closest('tr').remove();
    $('#salaryCap').text('$' + newSalaryCap);
}

function moveWR(btn) {
    var name = $(btn).closest('tr').find('td:eq(0)').text();
    var salary = $(btn).closest('tr').find('td:eq(2)').text();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap - playerSalary;

    if (newSalaryCap < 0) {
        alert('You have exceeded the salary cap!');
        return;
    }

    if ($('#wrInput').val() == '') {
        $('#wrInput').val(name + " (" + salary + ")");
    } else if ($('#wr2Input').val() == '') {
        $('#wr2Input').val(name + " (" + salary + ")");
    }
    $(btn).closest('tr').remove();
    $('#salaryCap').text('$' + newSalaryCap);
}


function moveTE(btn) {
    var name = $(btn).closest('tr').find('td:eq(0)').text();
    var salary = $(btn).closest('tr').find('td:eq(2)').text();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap - playerSalary;

    if (newSalaryCap < 0) {
        alert('You have exceeded the salary cap!');
        return;
    }
    $('#teInput').val(name + " (" + salary + ")");
    $(btn).closest('tr').remove();
    $('#salaryCap').text('$' + newSalaryCap);

}

function moveK(btn) {
    var name = $(btn).closest('tr').find('td:eq(0)').text();
    var salary = $(btn).closest('tr').find('td:eq(2)').text();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap - playerSalary;

    if (newSalaryCap < 0) {
        alert('You have exceeded the salary cap!');
        return;
    }
    $('#kInput').val(name + " (" + salary + ")");
    $(btn).closest('tr').remove();
    $('#salaryCap').text('$' + newSalaryCap);

}

function moveD(btn) {
    var name = $(btn).closest('tr').find('td:eq(0)').text();
    var salary = $(btn).closest('tr').find('td:eq(2)').text();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap - playerSalary;

    if (newSalaryCap < 0) {
        alert('You have exceeded the salary cap!');
        return;
    }
    $('#dInput').val(name + " (" + salary + ")");
    $(btn).closest('tr').remove();
    $('#salaryCap').text('$' + newSalaryCap);

}

function moveBack() {
    var name = $('#qbInput').val().match(/^[^(]+/)[0].trim();
    var salary = $('#qbInput').val().match(/\(([^)]+)\)/)[1].replace(/,/g, '').trim();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap + playerSalary;

    $('#nav-qb tbody').append('<tr id="nav-qb1"><td>' + name + '</td><td>QB</td><td>' + salary + '</td><td><button type="submit" class="btn btn-primary" onclick="moveQB(this);">+</button></td></tr>');
    $('#qbInput').val('');
    $('#salaryInput').val('');
    $('#salaryCap').text('$' + newSalaryCap);
}

function moveBackRB() {
    var name = $('#rbInput').val().match(/^[^(]+/)[0].trim();
    var salary = $('#rbInput').val().match(/\(([^)]+)\)/)[1].replace(/,/g, '').trim();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap + playerSalary;

    $('#nav-rb tbody').append('<tr id="nav-rb1"><td>' + name + '</td><td>RB</td><td>' + salary + '</td><td><button type="submit" class="btn btn-primary" onclick="moveRB(this);">+</button></td></tr>');
    $('#rbInput').val('');
    $('#salaryInput').val('');
    $('#salaryCap').text('$' + newSalaryCap);
}

function moveBackRB2() {
    var name = $('#rb2Input').val().match(/^[^(]+/)[0].trim();
    var salary = $('#rb2Input').val().match(/\(([^)]+)\)/)[1].replace(/,/g, '').trim();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap + playerSalary;

    $('#nav-rb tbody').append('<tr id="nav-rb1"><td>' + name + '</td><td>RB</td><td>' + salary + '</td><td><button type="submit" class="btn btn-primary" onclick="moveRB(this);">+</button></td></tr>');
    $('#rb2Input').val('');
    $('#salaryInput').val('');
    $('#salaryCap').text('$' + newSalaryCap);
}

function moveBackWR() {
    var name = $('#wrInput').val().match(/^[^(]+/)[0].trim();
    var salary = $('#wrInput').val().match(/\(([^)]+)\)/)[1].replace(/,/g, '').trim();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap + playerSalary;

    $('#nav-wr tbody').append('<tr id="nav-wr1"><td>' + name + '</td><td>WR</td><td>' + salary + '</td><td><button type="submit" class="btn btn-primary" onclick="moveWR(this);">+</button></td></tr>');
    $('#wrInput').val('');
    $('#salaryInput').val('');
    $('#salaryCap').text('$' + newSalaryCap);
}

function moveBackWR2() {
    var name = $('#wr2Input').val().match(/^[^(]+/)[0].trim();
    var salary = $('#wr2Input').val().match(/\(([^)]+)\)/)[1].replace(/,/g, '').trim();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap + playerSalary;

    $('#nav-wr tbody').append('<tr id="nav-wr1"><td>' + name + '</td><td>WR</td><td>' + salary + '</td><td><button type="submit" class="btn btn-primary" onclick="moveWR(this);">+</button></td></tr>');
    $('#wr2Input').val('');
    $('#salaryInput').val('');
    $('#salaryCap').text('$' + newSalaryCap);
}

function moveBackTE() {
    var name = $('#teInput').val().match(/^[^(]+/)[0].trim();
    var salary = $('#teInput').val().match(/\(([^)]+)\)/)[1].replace(/,/g, '').trim();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap + playerSalary;

    $('#nav-te tbody').append('<tr id="nav-te1"><td>' + name + '</td><td>TE</td><td>' + salary + '</td><td><button type="submit" class="btn btn-primary" onclick="moveTE(this);">+</button></td></tr>');
    $('#teInput').val('');
    $('#salaryInput').val('');
    $('#salaryCap').text('$' + newSalaryCap);
}

function moveBackK() {
    var name = $('#kInput').val().match(/^[^(]+/)[0].trim();
    var salary = $('#kInput').val().match(/\(([^)]+)\)/)[1].replace(/,/g, '').trim();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap + playerSalary;

    $('#nav-k tbody').append('<tr id="nav-k1"><td>' + name + '</td><td>K</td><td>' + salary + '</td><td><button type="submit" class="btn btn-primary" onclick="moveK(this);">+</button></td></tr>');
    $('#kInput').val('');
    $('#salaryInput').val('');
    $('#salaryCap').text('$' + newSalaryCap);
}

function moveBackD() {
    var name = $('#dInput').val().match(/^[^(]+/)[0].trim();
    var salary = $('#dInput').val().match(/\(([^)]+)\)/)[1].replace(/,/g, '').trim();
    var currentSalaryCap = parseInt($('#salaryCap').text().replace('$', ''));
    var playerSalary = parseInt(salary.replace('$', ''));
    var newSalaryCap = currentSalaryCap + playerSalary;

    $('#nav-d tbody').append('<tr id="nav-d1"><td>' + name + '</td><td>D</td><td>' + salary + '</td><td><button type="submit" class="btn btn-primary" onclick="moveD(this);">+</button></td></tr>');
    $('#dInput').val('');
    $('#salaryInput').val('');
    $('#salaryCap').text('$' + newSalaryCap);
}


$(document).ready(function() {
    $('#move-qb-btn').click(function() {
        var name = $(this).closest('tr').find('td:eq(0)').text();
        $('#qbInput').val(name);
    });
});